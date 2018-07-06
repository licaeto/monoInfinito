#!/usr/bin/env python
#! -*- encoding: utf8 -*-

import pickle
import sys

def getKey(item):
	return item[1]

def monoinf(fText,n):
	"""
	Esta funcion toma como parametro una lista de las palabras que forman el texto y devuelve
	un indice indicando para cada palabra la frecuencia y una lista con las palabras 
	siguientes ordenadas por su frecuencia.
	"""
	res=''
	dic = {}
	n=int(n)
	for i in range(len(fText)-n):
		aux = ' '.join(fText[i:i+n-1])
		if aux in dic:
			dic[aux][0]=dic.get(aux)[0]+1
			siguientes = dic[aux][1]
			if fText[i+n-1] in siguientes:
				siguientes[fText[i+n-1]]=siguientes.get(fText[i+n-1])+1
			else:
				siguientes[fText[i+n-1]]=1
		else:
			dic[aux]=[1,{fText[i+n-1]:1}]

	for i in dic:
		dic[i][1] = sorted(dic[i][1].items(),key=getKey,reverse=True)

	return dic
	
if __name__ == "__main__":
	if len(sys.argv) != 4:
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
		one_dic = monoinf(fText,sys.argv[3])
		pickle.dump(one_dic,open(sys.argv[2],'wb'))
		
		
			


