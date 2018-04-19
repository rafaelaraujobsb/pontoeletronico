#!/bin/usr/python
#coding = utf-8

import hashlib, random
from back.db import BancoDeDados
import urllib.request
import requests
from datetime import datetime 
import matplotlib.pyplot as plt
import pandas

def cryptmd5(password):
	return hashlib.md5(password.encode()).hexdigest()

def gerarpin():
	return random.randint(1000,9999)

def gerarmtrc(): #geradora de matricula
	db = BancoDeDados()
	conn = db.connect()

	mtrc = db.lastRegister(conn)

	db.conclose(conn)

	return mtrc+1

def qrcdwn(mtrc, nome): #gerador e download de qrcode
	nome = nome.replace(' ','+')
	urllib.request.urlretrieve("https://api.qrserver.com/v1/create-qr-code/?data="+str(mtrc)+"%0A"+nome, \
		"static/qrcode/"+str(mtrc)+nome+".jpg")

'''
def apiqrcode(file): # leitor de qrcode
	req = requests.request('POST', 'http(s)://api.qrserver.com/v1/read-qr-code/',data=file)
	print(req)
'''

def date(): # gerar data do dia
	d = datetime.now()
	df = "{}-{}-{}".format(d.year, d.month, d.day)
	print(df)
	return df

def apiLoc(lat, lon): # api que retorna o endereço da sua geolocalização
	key = "AIzaSyAPs2W2gV4-yXkFfiRYP0q-i2X31DNYXjU"
	latlon = lat+","+lon # concatenar lattitude e longitude
	url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+latlon+"&key="+key
	res = requests.get(url)
	info = res.json() #transformando em json o resultado
	info = info['results']

	add = info[0]['address_components'] 
	num = add[0]['short_name']# pegando o lote

	end = add[1]['short_name'] # pegando o endereco

	loc = end + " " + num #juntando a informação com espaço

	return loc

def graph(conn):
	df = pandas.read_sql('SELECT*FROM viewgraph', conn, index_col=['hora'])
	ax = df.plot(kind='bar', title ="Horário e tipo ponto", figsize=(5, 6), legend=True, fontsize=8)
	ax.set_xlabel("Horário", fontsize=8)
	ax.set_ylabel("Tipo do ponto", fontsize=8)
	plt.savefig('static/graph.png')