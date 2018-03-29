#!/bin/usr/python
#coding = utf-8

from back.login import TelaLogin
from back.db import BancoDeDados
from back.vrf import Verificacao
from flask import Flask, render_template, request, redirect, url_for, session
from back.alone import * # biblioteca com funções diversas

app = Flask(__name__)
app.secret_key = 'b9bac6755292f37ae16b82c7b1337987cb3a4b0ebb24b2fc9ea9893f9a61dbfa' #key para session 
vrf = Verificacao()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['submit'] == 'entrar': #verificando o botão que executou ação
			#recuperando os dados da página
			usr = request.form['user']
			pwd = request.form['pass']

			error = vrf.nullSpace('Preencha todos os campos!', user=usr, password=pwd)

			
			if error: #verificar se os campos foram preenchidos
				return render_template("index.html", error=error)
			else: #verificando usuário e senha
				pwd = cryptmd5(pwd)
				db = BancoDeDados()
				conn = db.connect()
				error = db.vrfUser(conn, usr, pwd)
				db.conclose(conn)

				if error:#verificando se houve algum erro de verificação ou não
					return render_template("index.html", error=error)

			#Usuário encontrado e validado
			session['username'] = usr
			return redirect(url_for('home')) #encaminha para a home
		else:
			return redirect(url_for('ponto')) #encaminha para ponto 
	else:
		return redirect(url_for('index'))

"""
 Parte onde só usuário com login tem acesso
"""
@app.route('/home')
def home():
	if 'username' in session:
		db = BancoDeDados()

		sql = "SELECT*FROM viewreg"

		conn = db.connect()
		res = db.dmlS(conn, sql)
		db.conclose(conn)

		return render_template('home.html', lista=res)
	
	return render_template('index.html', error="Login não foi realizado!")

'''@app.route('/pesquisa', methods=['GET'])
def pesq_func():
	if 'username' in session:
		mtrc = request.form['matric'] # pegando o valor de pesquisa

		if mtrc == "":
			redirect(url_for('home'))

		db = BancoDeDados()

		sql="SELECT data, matricula, loc, to_char(hora, 'HH24:MI'), cod_tipo FROM ponto WHERE matricula =%s"

		conn = db.connect()
		res = db.dmlS(conn, sql, mtrc)
		db.conclose(conn)
	return render_template('home.html', lista=res)'''

@app.route('/cad_funcionario', methods=['GET', 'POST'])
def cad_func():
	mtrc = gerarmtrc() #informar a matrícula do próximo funcionário

	if request.method == 'POST': #indica que se quer cadastrar um usuário no banco de dados
		#reuperar dados
		nomeFunc = request.form['nomeFunc']
		usr = request.form['user']
		pwd = request.form['pass']
		ch = request.form['cargahr'] # carga horária
		p = request.form['pin'] # pin
		
		# verificando os dados digitados
		error = vrf.nullSpace('Preencha os campos marcados com *', nome=nomeFunc, user=usr, password=pwd, \
			cargahr=ch, pin=p)

		if error:
			return render_template('cad_func.html', error=error, matricula=mtrc, nome=nomeFunc, user=usr, \
			cargahr=ch, pin=p) # retorna para a página de login com os dados informados
		else:
			error = vrf.validateData(nome=nomeFunc, user=usr, cargahr=ch) #validando os tipo dos dados

			if error:
				return render_template("cad_func.html", error=error, matricula=mtrc,nome=nomeFunc, user=usr, \
			cargahr=ch, pin=p) # retorna para a página de login com os dados informados

		pwd = cryptmd5(pwd) #criptografando a senha

		#cadastrando o funcionario no banco de dados
		db = BancoDeDados()

		sql = "INSERT INTO funcionario(nome, usuario, senha, pin, carga_horaria, cod_acesso) VALUES (%s, %s, %s, %s, %s, 2)"

		v = [nomeFunc, usr, pwd, int(p), int(ch)] #lista com os valores

		conn = db.connect()
		error = db.dmlIUD(conn, sql, v)
		db.conclose(conn)

		if error: #verificar se aconteceu algum erro
			return render_template("cad_func.html", error=error, matricula=mtrc,nome=nomeFunc, user=usr, \
			cargahr=ch, pin=p)


		return redirect(url_for('qrcode_func'), code=307) #redirecionando com o POST
		
	else:
		gpin = gerarpin() #informar o pin do próximo funcionário

		return render_template("cad_func.html", pin=gpin, matricula=mtrc)

@app.route('/qrcode_func', methods=['POST','GET'])
def qrcode_func():
	if request.method == 'POST':
		db = BancoDeDados()

		sql = "SELECT matricula, nome FROM funcionario WHERE matricula = (SELECT max(matricula) FROM funcionario)"

		conn = db.connect()
		res = db.dmlS(conn,sql)
		db.conclose(conn)

		if res == 1:
			return "<h2>Não foi possível encontrar o funcionário!</h2>"

		mtrc = res[0][0] # matricula
		nomeFunc = res[0][1]

		qrcdwn(mtrc, nomeFunc) # download do qrcode

		return render_template('gnqrcode.html', nome=nomeFunc, matricula=mtrc)
	else:
		return redirect(url_for('index'))

@app.route('/qrcode', methods=['GET', 'POST']) # leitura do qr code para bater o ponto
def ponto():
	if request.method == 'POST':
		#f = request.files['file'] recebdno o arquivo

		# res = apiqrcode(f) SEM FUNCIONAR

		# print(f)

		mtrc = request.form['matricula']
		p = request.form['pin']
		lat = request.form['latitude']
		lon = request.form['longitude']

		error = vrf.validateData(matricula=mtrc)

		if error:
			return render_template('btponto.html', error=error)

		db = BancoDeDados()

		sql = "SELECT nome FROM funcionario WHERE matricula=%s and pin=%s"

		conn = db.connect()
		res = db.dmlS(conn, sql, [int(mtrc), int(p)])
		db.conclose(conn)

		if res == 1:
			return "<h2>Não foi possível encontrar o funcionário!</h2>"

		if res == []:
			return render_template('btponto.html', error='Pin ou matricula incorreto!', latitude=lat,longitude=lon) 

		if lat != "" and lon != "":
			endc = apiLoc(lat, lon)
		else:
			endc="Não foi possível acessar localização!"
			
		return redirect(url_for('info_ponto', matricula=mtrc, nome=res[0][0], endereco=endc), code=307)
	else:
		return render_template('btponto.html')

@app.route('/info_ponto', methods=['POST']) # realizar o registro do ponto
def info_ponto():
	if request.method == 'POST':
		mtrc = request.args['matricula']
		nome = request.args['nome']
		edc = request.args['endereco']

		db = BancoDeDados()

		mtrc = request.form['matricula']
		p = request.form['pin']

		#verificar os tipos de pontos que a pessoa pode bater
		data = date()

		sql = "SELECT ponto.cod_tipo FROM ponto WHERE matricula=%s and data=%s"

		conn = db.connect()
		res = db.dmlS(conn, sql, [int(mtrc), data])
		db.conclose(conn)

		tipos = {1:'Entrada', 2:'Saída Almoço', 3:'Volta Almoço', 4:'Saída'}
			
		if res != []:
			for r in res:
				if r[0] == 1:
					del tipos[1]
				elif r[0] == 2:
					del tipos[2]
				elif r[0] == 3:
					del tipos[3]
				elif r[0] == 4:
					del tipos[4]

		if tipos == {}:
			return render_template('index.html', tipo=1)
				
		return render_template('infoponto.html', matricula=mtrc, nome=nome, tipo=tipos, endereco=edc) 
	else:
		return redirect(url_for('index'))

@app.route('/reg_ponto', methods=['POST']) # realizar o registro do ponto
def reg_ponto():
	tipo = request.form['tipo']
	mtrc = request.form['matricula']
	edc = request.form['local']

	db = BancoDeDados()

	sql = "INSERT INTO ponto(loc, matricula, cod_tipo) VALUES (%s, %s, %s)"

	v = [edc, int(mtrc), int(tipo)]

	conn = db.connect()
	res = db.dmlIUD(conn, sql, v)
	db.conclose(conn)

	if res:
		return render_template('index.html', error="Falha ao registrar ponto!") # retornando o usuário para login e informando o erro do ponto


	return render_template('index.html', success=1) # avisando que o ponto foi registrado

@app.route('/logout')
def logout():
	# remover a sessão do usuário
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True, port=8080) #rodar o servidor no modo debug na porta 8080
