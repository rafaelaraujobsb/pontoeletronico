#!/bin/usr/python
#coding = utf-8

from back.login import TelaLogin
from back.db import BancoDeDados
from back.vrf import Verificacao
from flask import Flask, render_template, request, redirect, url_for, session
from back.alone import * # ARRUMAR UM LOCAL PARA ESSA COISINHA AQUI!!!!!!!!!!!

app = Flask(__name__)
app.secret_key = 'b9bac6755292f37ae16b82c7b1337987cb3a4b0ebb24b2fc9ea9893f9a61dbfa' #key para session 
vrf = Verificacao()
db = BancoDeDados()

'''def main():
	bd = BancoDeDados()
	conn = bd.conecta()
	cur.execute('SELECT * FROM acesso')
	for r in cur:
		print(r)
		log = TelaLogin()
	log.imprime()
'''
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	#recuperando os dados da página
	btn = request.form['submit']
	usr = request.form['user']
	pwd = request.form['pass']

	if btn == 'entrar': #verificando o botão que executou ação
		error = vrf.nullSpace('Preencha todos os campos!', user=usr, password=pwd)

		
		if error: #verificar se os campos foram preenchidos
			return render_template("index.html", error=error)
		else: #verificando usuário e senha
			pwd = cryptmd5(pwd) #LEMBRAR DE ALTERAR AQUI QUANDO ACHAR UM LUGAR PARA ALONE!!!!!
			conn = db.connect()
			error = db.vrfUser(conn, usr, pwd)

			if error:#verificando se houve algum erro de verificação ou não
				db.conclose(conn)
				return render_template("index.html", error=error)

		#Usuário encontrado e validado
		session['username'] = usr
		return redirect(url_for('home')) #encaminha para a home
	else:
		return render_template("index.html")


"""
 Parte onde só usuário com login tem acesso
"""
@app.route('/home')
def home():
	return "<h1>"+ session['username'] +"</h1>"

if __name__ == '__main__':
	app.run(debug=True, port=8080) #rodar o servidor no modo debug na porta 8080
