#!/usr/bin/env python
#! -*- encoding: utf8 -*-

import pickle
import sys

def getKey(item):
	return item[1]

def monoinf(fText):
	"""
	Esta funcion toma como parametro una lista de las palabras que forman el texto y devuelve
	un indice indicando para cada palabra la frecuencia y una lista con las palabras 
	siguientes ordenadas por su frecuencia.
	"""
	res=''
	dic = {}
	for i in range(len(fText)-1):
		if fText[i] in dic:
			dic[fText[i]][0]=dic.get(fText[i])[0]+1
			siguientes = dic[fText[i]][1]
			if fText[i+1] in siguientes:
				siguientes[fText[i+1]]=siguientes.get(fText[i+1])+1
			else:
				siguientes[fText[i+1]]=1
		else:
			dic[fText[i]]=[1,{fText[i+1]:1}]

	for i in dic:
		dic[i][1] = sorted(dic[i][1].items(),key=getKey,reverse=True)

	return dic

"""Aplicación que toma un texto como parametro y devuelve un diccionario en el que para cada
palabra se muestra su frecuencia y una lista con las palabras siguientes mas frecuentes

Argumentos
	Fichero a procesar
	Fichero donde volcar el resultado"""	
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print ("Numero de argumentos incorrectos")
	else:
		punt=[';','.','?','!']
		en = open(sys.argv[1],'r')
		text = "$ " + en.read()
		text = text.replace('\n',' ').replace(',','')
		for i in punt:
			text = text.replace(i," $ ")
		text = text+' $'
		fText = text.strip().lower().split()
		one_dic = monoinf(fText)
		print(one_dic)
		pickle.dump(one_dic,open(sys.argv[2],'wb'))
		
		
			


