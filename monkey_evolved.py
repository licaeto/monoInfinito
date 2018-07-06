#!/usr/bin/env python
#! -*- encoding: utf8 -*-

import pickle
import sys
import random

def generar_frase(dic):
	"""
	Esta funcion genera una frase aleatoriamente ponderando las palabras siquientes por la frecuencia 
	de aparicion en el documento original 
	"""
	sentence=['$']
	
	for n in range(40):
		frec = dic[sentence[-1]][0]
		siguientes = dic[sentence[-1]][1]
		num = random.randint(1,frec)
		x = 0
		for i in siguientes:
			if num <= x+i[1]:
				word=i[0]
				break
			else:
				x+=i[1]
		sentence.append(word)
		if word == '$':
			break
	return ' '.join(sentence).replace('$','')
			
		

def monoevo(dic,n):
	"""
	Esta funcion devuelve un string con n frases generadas aleatoriamente	
	"""
	res=''
	for i in range(int(n)):
		res+=generar_frase(dic)+'\n'
	return res
	

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print ("Numero de argumentos incorrecto")
	else:
		my_dic=pickle.load(open(sys.argv[1],'rb'))
		print(onoevo(my_dic,sys.argv[2]))
