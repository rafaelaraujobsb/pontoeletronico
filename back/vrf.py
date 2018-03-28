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