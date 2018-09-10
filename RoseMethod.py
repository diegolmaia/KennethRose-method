import sys
import math
import numpy as np
import os

#!/usr/bin/python
# -*- coding: utf-8 -*-

file = open("file.txt", "w")


def crie_matriz(n_linhas, n_colunas, valor):
	    ''' (int, int, valor) -> matriz (lista de listas)
	    Cria e retorna uma matriz com n_linhas linha e n_colunas
	    colunas em que cada elemento é igual ao valor dado.
	    '''
	    matriz = [] # lista vazia
	    for i in range(n_linhas):
	        # cria a linha i
	        linha = [] # lista vazia
	        for j in range(n_colunas):
	            linha.append(valor)
	
	        # coloque linha na matriz
	        matriz.append(linha)
	
	    return matriz


def valor_decimal(matriz, n_linhas, soma):   #Calcula o valor decimal relativo (última coluna da matriz)
	for i in range(0,n_linhas):
		matriz[i][n_linhas+1]= round(matriz[i][n_linhas]/soma,2) #soma da linha/soma total O round reduz casa decimal
	return matriz


##def de matrizes
cli=[]  
nec=[]  
PPnec = []

######################### Inserir Clientes ######################
file.writelines('Clientes\n')
aux = input("Quantos Clientes? ")
ncli = int(aux)
for i in range(0,ncli):
	cli.append(input("Cliente %s: " %(i)))
	file.writelines("C%s:"%(i)+str(cli[i])+'\n')

Pcli=crie_matriz(ncli,ncli+2,0)   # Cria  a matriz de Prioridade de Cliente
#print(Pcli)


######## Insere valores na matriz prioridade de CLiente ###########
print("Responda qual a prioridade de um cliente em relação ao outro de acordo a escala.\n" 
		"10 - Muito mais importante\n "
		"5	- Pouco mais importante\n "
		"1  - Indiferente\n "
		"0,2 - Pouco menos importante\n "
		"0,1 - Muito menos importante\n ")

soma=0
file.writelines('\n*Ultima coluna é a importancia do Cliente (em dec.)\n#Prioridade de Clientes\n')
for i in range(0,ncli):
	for j in range(0,ncli):
		if i!=j:
			Pcli[i][j]= float (input("C%s em relação C%s: " %(i,j)))
	Pcli[i][ncli]=round(sum(Pcli[i]),3)  #Calcula a soma da linha
	soma=soma+Pcli[i][ncli]   # Calcula soma da coluna
	#file.writelines("C%s:"%(i)+str(Pcli[i])+'\n')
	#print(Pcli)

Pcli=valor_decimal (Pcli,ncli, soma)

#salvando no arquivo a matriz Prioridade de Clientes
for i in range(0,ncli):
	file.writelines("C%s:"%(i)+str(Pcli[i])+'\n')
	


################# Inserir Necessidades ######################
file.writelines('\nNecessidades\n')
aux = input("Quantas Necessidades? ")
nn = int(aux)
for i in range(0,nn):
	nec.append(input("Necessidade %s: " %(i)))
	file.writelines("N%s:"%(i)+str(nec[i])+'\n')

Pbalance=crie_matriz(nn,ncli+1,0) # +2 pra sobrar espaço pra soma e classificação

######## Insere valores na matriz prioridade das Necessidade ###########
print("Responda qual a prioridade de uma Necessidade em relação a outra (Pra cada cliente)\n"
		" de acordo a escala. \n" 
		"10 - Muito mais importante\n "
		"5	- Pouco mais importante\n "
		"1  - Indiferente\n "
		"0,2 - Pouco menos importante\n "
		"0,1 - Muito menos importante\n ")

for k in range(0,ncli):  # Roda uma vez pra cada Cliente 
	print("Priorização das Necessidades p/ Cliente %s" %(k))
	Pnec=crie_matriz(nn,nn+2,0)   # Cria  a matriz de Prioridade de Necessidade
	soma=0
	for i in range(0,nn):  
		for j in range(0,nn):
			if i!=j:
				Pnec[i][j]= float (input("N%s em relação N%s: " %(i,j)))
		Pnec[i][nn]=round(sum(Pnec[i]),3)  #Calcula a soma da linha
		soma=soma+Pnec[i][nn]   # Calcula soma da coluna

	Pnec=valor_decimal (Pnec,nn, soma)
	#print("\n PNECESSIDADE")
	#print(Pnec)

	###Matriz de balanço###
	for i in range(0,nn):
		Pbalance[i][k]=round(Pcli[k][ncli+1]*Pnec[i][nn+1],3)
	PPnec.append(Pnec)
	#print("\n Pbalance")
	#print(Pbalance)

file.writelines('\n*Ultima coluna é a importancia da Necessidade (em dec.)\n#Priorização Balanceada das Necessidades\n')

#### soma da linha da Matriz balanco
for i in range(0,nn):
	Pbalance[i][ncli]=round(sum(Pbalance[i]),3)
	file.writelines("N%s:"%(i)+str(Pbalance[i])+'\n')
	
file.close()