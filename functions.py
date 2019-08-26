# PROJETO 1 | FUNDAMENTO DA PROGRAMACAO | ENCRIPTACAO DE MENSAGENS

# 86372 | ALEXANDRE GALAMBAS


'''
A partir de um tuplo de 25 caracteres, gerar uma chave formada por 1 tuplo de 5 tuplos com 5 elementos cada.
Os 25 caracteres formam uma tabela em que cada tuplo forma uma linha e cada elemento desse tuplo pertence a uma coluna.
'''
def gera_chave1(letras):
	return letras[:5], letras[5:10], letras[10:15], letras[15:20], letras[20:]

'''
Para realizar a encriptacao, cada caractere e substituido por dois caracteres.
O primeiro para o numero da linha e o segundo para o numero da coluna.
'''
def obtem_codigo1(car, chave):
	# As linhas sao numeradas de 0 a 4 (inclusive)
	for linha in range(5):
		if car in chave[linha]:
			# As colunas sao numeradas de 0 a 4 (inclusive)
			for coluna in range(5):
				if car == chave[linha][coluna]:
					return str(linha) + str(coluna)

'''
Utilizando a funcao anterior, uma cadeia de caracteres e transformada no codigo correspondente.
'''
def codifica1(cad, chave):
	if cad == '':
		return ''
	else:
		return obtem_codigo1(cad[0], chave) + codifica1(cad[1:], chave)

'''
Para desencriptar realiza-se o processo contrario.
Cada 2 caracteres, sao substituidos 1 unico.
O primeiro caracter refere-se a linha da tabela (um dos 5 tuplos que constituem a chave) e o segundo a coluna (um dos 5 elementos de cada tuplo).
'''
def obtem_car1(cod, chave):
	# linha = int(cod[0])
	# coluna = int(cod[1])
	return chave[ int(cod[0]) ][ int(cod[1]) ]

'''
Utilizando a funcao anterior, uma cadeia de caracteres em codigo e transformada na cadeia descodificada correspondente.
'''
def descodifica1(cad_codificada, chave):
	if cad_codificada == '':
		return ''
	else:
		return obtem_car1(cad_codificada, chave) + descodifica1(cad_codificada[2:], chave)

'''
A partir de um tuplo de um numero qualquer de caracteres, gerar uma chave formada por 1 tuplo de tuplos.
O ultimo tuplo pode ser mais curto que os restantes.
Os caracteres formam uma tabela em que cada tuplo forma uma linha e cada elemento desse tuplo pertence a uma coluna.
'''
def gera_chave2(letras):

	def chave(letras, colunas):
		if len(letras) <= colunas:
			return (letras,)
		else:
			return (letras[:colunas],) + chave(letras[colunas:], colunas)
	
	# O numero de tuplos e a raiz quadrada do menor quadrado perfeito nao inferior ao numero de caracteres.
	# linhas --> numero de tuplos da chave
	linhas = 1
	while linhas*linhas < len(letras):
		linhas = linhas + 1
	
	# Considerando o numero de tuplos e igual ao numero de elemetos de cada tuplo.
	# Se o numero de elementos de todos os tuplos (menos o ultimo) for maior ou igual ao numero total de elementos:
	# Decresce-se o numero de elementos por tuplo
	if linhas*(linhas-1) >= len(letras):
		# colunas --> numero de elementos de cada tuplo (menos do ultimo que pode ser mais curto).
		colunas = linhas - 1
	else:
		colunas = linhas
	return chave(letras, colunas)

'''
Para realizar a encriptacao, cada caractere e substituido por dois caracteres.
O primeiro para o numero da linha e o segundo para o numero da coluna.
Caso o caracter nao se encontre na chave, e codificado como 'XX'.
'''
def obtem_codigo2(car, chave):
	# As linhas sao numeradas do 0 ate ao comprimento da chave
	for linha in range( len(chave) ):
		if car in chave[linha]:
			# As colunas sao numeradas do 0 ate ao comprimento da chave
			for coluna in range( len(chave[linha]) ):
				if car == chave[linha][coluna]:
					return str(linha) + str(coluna)
	return 'XX'

'''
Utilizando a funcao anterior, uma cadeia de caracteres e transformada no codigo correspondente.
'''
def codifica2(cad, chave):
	if cad == '':
		return ''
	else:
		return obtem_codigo2(cad[0], chave) + codifica2(cad[1:], chave)

'''
Para desencriptar realiza-se o processo contrario.
Cada 2 caracteres, sao substituidos 1 unico.
O primeiro caracter refere-se a linha da tabela (tuplos que constituem a chave) e o segundo a coluna (elementos de cada tuplo).
Se o codigo for 'XX', e substituido por '?'.
'''
def obtem_car2(cod, chave):
	if cod == 'XX':
		return '?'
	else:
		# linha = int(cod[0])
		# coluna = int(cod[1])		
		return chave[ int(cod[0]) ][ int(cod[1]) ]

'''
Utilizando a funcao anterior, uma cadeia de caracteres em codigo e transformada na cadeia descodificada correspondente.
'''
def descodifica2(cad_codificada, chave):
	if cad_codificada == '':
		return ''
	else:
		return obtem_car2(cad_codificada[:2], chave) + descodifica2(cad_codificada[2:], chave)
