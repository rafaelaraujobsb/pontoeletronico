#!/bin/usr/python
#coding = utf-8

class Verificacao():
	'''
		Verificação dos dados.

		Essa classe realiza a verificação dos dados informados e 
		seus metódos retornam uma mensagem de erro personalizada

		* não possui atributos
	'''

	def nullSpace(self, error, **args):
		'''
			Metódo que verifica se os argumentos fornecidos estão vázios

			Args:
				error: Recebe uma mensagem personalizada
				**args: recebe mais de um argumento para ser verificado
		'''

		for value in args.values():
			if value == '':
				return error

		return None

	def validateData(self, **args):
		'''
			Metódo para verificar se os argumentos estão no
			paradrão do banco de dados

			Args:
				**args: recebe mais de um argumento para ser verificado
		'''
		error = ""

		for key, value in args.items():
			if key == 'nome':
				if len(value) > 40:
					error += "*O nome passou de 40 caracteres<br>"
			elif key == 'user':
				if len(value) > 10:
					error += "*O usuário passou de 10 caracteres<br>"
			elif key == 'cargahr':
				try:
					int(value)
				except:
					error += "*A carga horária não é um inteiro<br>"
			elif key == 'matricula':
				try:
					int(value)
				except:
					error += "*A matrícula não é um inteiro<br>"
					
		return error