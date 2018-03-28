#!/bin/usr/python
#coding = utf-8

import psycopg2

class BancoDeDados():
	"""
		Operações relacionadas ao banco de dados.

		Essa classe realiza todas as aquisições no 
		banco de dados(DDL e DML)

		Attributes:
			host: IP do servidor
			dbname: nome do banco de dados
			user: usuário de conexão
			password: senha para se conectar ao bd
	"""

	def __init__(self, _host, _dbname, _user, _pass):
		"""
			Construtor
		"""
		self._host = _host
		self._dbname = _dbname
		self._user = _user
		self._password = _password

	def __init__(self):
		"""
			Sobrecarga de construtor
		"""
		self._host = 'localhost'
		self._dbname = 'ptoeletr'
		self._user = 'postgres'
		self._pass = 'postgres'

	def connect(self):
		'''
			Conexão com o banco de dados
		'''

		conn = None

		try:
			conn = psycopg2.connect('host={} dbname={} \
				user={} password={}'.format(self._host, self._dbname,self._user, self._pass))
		except (Exception, psycopg2.DatabaseError) as error:
			return 'Error ao se conectar com o banco de dados!'

		return conn

	def vrfUser(self, conn, usr, pwd):
		res = None

		sql = "SELECT usuario, senha FROM funcionario WHERE usuario='"+ usr +"'" #comando sql que sera executado

		try:
			cur = conn.cursor() #iniciando o cursor do db
			cur.execute(sql)
			res = cur.fetchall()
		except:
			return 'Error na execução!'

		if len(res) == 0 or (res[0][0] != usr or res[0][1] != pwd): #verificando se não teve retorno ou senha e usuario não baterem
			return 'Usuário ou senha inválidos!'

		return None

	def lastRegister(self, conn):
		sql = "SELECT max(matricula) FROM funcionario"

		try:
			cur = conn.cursor()
			cur.execute(sql)
			res = cur.fetchone()
		except:
			return '<h1>Error de execução<h1>'

		if res == None:
			return 0
		else:
			return res[0]

	def dmlIUD(self, conn, sql, vls):
		'''
			Metódo para ser usado comandos DML(Insert, Update e Delete)

			Args:
				conn: conexão com o banco de dados
				sql: comando para ser executado
				vls: lista com todos os valores
		'''
		try:
			cur = conn.cursor()
			cur.execute(sql, vls)
			cur.close()
			conn.commit()
		except:
			return 'Erro na operação!'

		return 0

	def dmlS(self, conn, sql, vls=None):
		'''
			Metódo para ser usado com SELECT

			Args:
				conn: conexão com o banco de dados
				sql: comando para ser executado
		'''
		try:
			cur = conn.cursor()
			if vls != None:
				cur.execute(sql, vls)
			else:
				cur.execute(sql)
			res = cur.fetchall()
		except:
			return 1

		return res


	def conclose(self, conn):
		conn.close()