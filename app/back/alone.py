#!/bin/usr/python
#coding = utf-8

import hashlib, random
from back.db import BancoDeDados
import urllib.request
import requests
from datetime import datetime 

def cryptmd5(password):
	return hashlib.md5(password.encode()).hexdigest()

def gerarpin():
	return random.randint(1000,9999)

def gerarmtrc():
	db = BancoDeDados()
	conn = db.connect()

	mtrc = db.lastRegister(conn)

	db.conclose(conn)

	return mtrc+1

def qrcdwn(mtrc, nome):
	urllib.request.urlretrieve("https://api.qrserver.com/v1/create-qr-code/?data="+str(mtrc)+"%0A"+nome, \
		"static/qrcode/"+str(mtrc)+nome+".jpg")

def apiqrcode(file):
	req = requests.request('POST', 'http(s)://api.qrserver.com/v1/read-qr-code/',data=file)
	print(req)

def date():
	d = datetime.now()
	df = "{}-{}-{}".format(d.year, d.month, d.day)
	print(df)
	return df

def apiLoc(lat, lon):
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