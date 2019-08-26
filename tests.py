from <o nome do ficheiro do seu projecto> import *

chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.'))
cad = 'FUNDAMENTOS DA PROGRAMACAO'
cad_encriptada = codifica1(cad, chave)
print("teste-codifica1-1")
if cad_encriptada == '1040230300220423342433200300203032241132002200020024':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), (' ', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'x', 'z', '.'))
cad = 'fundamentos da programacao'
cad_encriptada = codifica1(cad, chave)
print("teste-codifica1-2")
if cad_encriptada == '1040230300220423342433200300203032241132002200020024':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'w', 'v', 'x', 'z'))
cad = 'whatisthecodedphrase'
cad_encriptada = codifica1(cad, chave)
print("teste-codifica1-3")
if cad_encriptada == '4112003413333412040224030403301232003304':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('L', 'M', 'N', 'O', 'P'), ('Q', 'R', 'S', 'T', 'U'), ('V', 'X', 'Z'))
cad = 'FUNDAMENTOS DA PROGRAMACAO'
cad_encriptada = codifica2(cad, chave)
print("teste-codifica2-1")
if cad_encriptada == '1034220300210422332332XX0300XX2431231131002100020023':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z'))
cad = 'FUNDAMENTOS DA PROGRAMACAO'
cad_encriptada = codifica2(cad, chave)
print("teste-codifica2-2")
if cad_encriptada == '1040230300220423342433200300203032241132002200020024':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',))
cad = 'FUNDAMENTOS DA PROGRAMACAO'
cad_encriptada = codifica2(cad, chave)
print("teste-codifica2-3")
if cad_encriptada == '11XX300300231030XX31XXXX0300XX3240311240002300020031':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'w', 'v', 'x', 'z'))
cad = ''
cad_encriptada = codifica2(cad, chave)
print("teste-codifica2-4")
if cad_encriptada == '':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.'))
cad_encriptada = '1040230300220423342433200300203032241132002200020024'
cad_desencriptada = descodifica1(cad_encriptada, chave)
print("teste-descodifica1-1")
if cad_desencriptada == 'FUNDAMENTOS DA PROGRAMACAO':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), (' ', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'x', 'z', '.'))
cad_encriptada = '1040230300220423342433200300203032241132002200020024'
cad_desencriptada = descodifica1(cad_encriptada, chave)
print("teste-descodifica1-2")
if cad_desencriptada == 'fundamentos da programacao':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'w', 'v', 'x', 'z'))
cad_encriptada = '4112003413333412040224030403301232003304'
cad_desencriptada = descodifica1(cad_encriptada, chave)
print("teste-descodifica1-3")
if cad_desencriptada == 'whatisthecodedphrase':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('L', 'M', 'N', 'O', 'P'), ('Q', 'R', 'S', 'T', 'U'), ('V', 'X', 'Z'))
cad_encriptada = '1034220300210422332332XX0300XX2431231131002100020023'
cad_desencriptada = descodifica2(cad_encriptada, chave)
print("teste-descodifica2-1")
if cad_desencriptada == 'FUNDAMENTOS?DA?PROGRAMACAO':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z'))
cad_encriptada = '1040230300220423342433200300203032241132002200020024'
cad_desencriptada = descodifica2(cad_encriptada, chave)
print("teste-descodifica2-2")
if cad_desencriptada == 'FUNDAMENTOS DA PROGRAMACAO':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',))
cad_encriptada = '11XX300300231030XX31XXXX0300XX3240311240002300020031'
cad_desencriptada = descodifica2(cad_encriptada, chave)
print("teste-descodifica2-3")
if cad_desencriptada == 'F?NDAMEN?O??DA?PROGRAMACAO':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',))
cad_encriptada = ''
cad_desencriptada = descodifica2(cad_encriptada, chave)
print("teste-descodifica2-4")
if cad_desencriptada == '':
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', '.')
chave = gera_chave1(letras)
print("teste-gera_chave1-1")
if chave == (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.')):
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', ' ', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z', '.')
chave = gera_chave1(letras)
print("teste-gera_chave1-2")
if chave == (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), (' ', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'x', 'z', '.')):
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z')
chave = gera_chave1(letras)
print("teste-gera_chave1-3")
if chave == (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('K', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'W', 'X', 'Z')):
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'z')
chave = gera_chave1(letras)
print("teste-gera_chave1-4")
if chave == (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'w', 'v', 'x', 'z')):
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', '.')
chave = gera_chave2(letras)
print("teste-gera_chave2-1")
if chave == (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.')):
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z')
chave = gera_chave2(letras)
print("teste-gera_chave2-2")
if chave == (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('L', 'M', 'N', 'O', 'P'), ('Q', 'R', 'S', 'T', 'U'), ('V', 'X', 'Z')):
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' ', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z')
chave = gera_chave2(letras)
print("teste-gera_chave2-3")
if chave == (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z')):
	print("PASSOU")
else:
	print("FALHOU")
print()
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R')
chave = gera_chave2(letras)
print("teste-gera_chave2-4")
if chave == (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',)):
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.'))
cod = '31'
car = obtem_car1(cod , chave)
print("teste-obtem_car1-1")
if car == 'Q':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), (' ', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'x', 'z', '.'))
cod = '00'
car = obtem_car1(cod , chave)
print("teste-obtem_car1-2")
if car == 'a':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'w', 'v', 'x', 'z'))
cod = '44'
car = obtem_car1(cod , chave)
print("teste-obtem_car1-3")
if car == 'z':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('L', 'M', 'N', 'O', 'P'), ('Q', 'R', 'S', 'T', 'U'), ('V', 'X', 'Z'))
cod = '30'
car = obtem_car2(cod, chave)
print("teste-obtem_car2-1")
if car == 'Q':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('L', 'M', 'N', 'O', 'P'), ('Q', 'R', 'S', 'T', 'U'), ('V', 'X', 'Z'))
cod = 'XX'
car = obtem_car2(cod, chave)
print("teste-obtem_car2-2")
if car == '?':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z'))
cod = '40'
car = obtem_car2(cod, chave)
print("teste-obtem_car2-3")
if car == 'U':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z'))
cod = 'XX'
car = obtem_car2(cod, chave)
print("teste-obtem_car2-4")
if car == '?':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',))
cod = '40'
car = obtem_car2(cod, chave)
print("teste-obtem_car2-5")
if car == 'R':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',))
cod = 'XX'
car = obtem_car2(cod, chave)
print("teste-obtem_car2-6")
if car == '?':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.'))
car = 'Q'
cod = obtem_codigo1(car, chave)
print("teste-obtem_codigo1-1")
if cod == '31':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), (' ', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'x', 'z', '.'))
car = 'a'
cod = obtem_codigo1(car, chave)
print("teste-obtem_codigo1-2")
if cod == '00':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'w', 'v', 'x', 'z'))
car = 'z'
cod = obtem_codigo1(car, chave)
print("teste-obtem_codigo1-3")
if cod == '44':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.'))
car = 'Q'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-1")
if cod == '31':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z', '.'))
car = 'W'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-2")
if cod == 'XX':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('L', 'M', 'N', 'O', 'P'), ('Q', 'R', 'S', 'T', 'U'), ('V', 'X', 'Z'))
car = 'Q'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-3")
if cod == '30':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), ('L', 'M', 'N', 'O', 'P'), ('Q', 'R', 'S', 'T', 'U'), ('V', 'X', 'Z'))
car = '?'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-4")
if cod == 'XX':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z'))
car = 'Z'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-5")
if cod == '43':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D', 'E'), ('F', 'G', 'H', 'I', 'J'), (' ', 'L', 'M', 'N', 'O'), ('P', 'Q', 'R', 'S', 'T'), ('U', 'V', 'X', 'Z'))
car = 'W'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-6")
if cod == 'XX':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',))
car = 'R'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-7")
if cod == '40':
	print("PASSOU")
else:
	print("FALHOU")
print()
chave = (('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'L', 'M'), ('N', 'O', 'P', 'Q'), ('R',))
car = 'W'
cod = obtem_codigo2(car, chave)
print("teste-obtem_codigo2-8")
if cod == 'XX':
	print("PASSOU")
else:
	print("FALHOU")
print()
