# Projeto organizador automático de arquivos baseado em extensão
#Esta versão pergunta qual a pasta de origem dos arquivos e também o caminho das novas pastas a serem criadas.
#Também pergunta se os arquivos vão ser Copiados ou Movidos para as novas pastas.

#Este código foi feito a partir do código original, postado no Linkedin, por Felipe Torres. O código original pode ser visto neste link: https://shre.ink/MLHq


import os
import shutil

#Inserir caminho onde estão os arquivos.
org = input('Pasta dos arquivos? ')
origem = r'{}'.format(org)

categorias = {
	'imagens': ('.jpg', '.png', '.jpeg'),
	'documentos': ('.pdf', '.docx', '.txt', '.epub'),
	'audios': ('.mp3', '.mp4', '.wav'),
	'programas': ('.rpm', '.deb', '.exe'),
	'scripts': ('.py', '.ipynb', '.sh')
	}

arquivos = os.listdir(origem)
print("\nArquivos encontrados:", arquivos)

pst = input('\nCaminho para as pastas a serem criadas? ')

#Define se vamos [C]opiar ou [M]over os arquivos
op = input('\n[C]opiar ou [M]over os arquivos? ')
while op.lower() != 'c' and op.lower() != 'm':
	op = input('\nEscolha [C]opiar ou [M]over?')
if op.lower() == 'c':
	acao = True
else:
	acao = False

for pasta in ['imagens', 'documentos', 'audios', 'programas', 'scripts']:
	pasta1 = pst + '/' + pasta
	os.makedirs(pasta1, exist_ok = True)
	print(f'\nPasta {pasta} criada com sucesso!')

for arquivo in arquivos:
	caminho_origem = os.path.join(origem, arquivo)

	for pasta, extensoes in categorias.items():
		if acao:
			if arquivo.lower().endswith(extensoes):
				pasta1 = pst + '/' + pasta
				shutil.copy(caminho_origem, os.path.join(pasta1, arquivo))
			print(f'\nArquivo "{arquivo}" copiado para {pasta1}/')
		else:
			if arquivo.lower().endswith(extensoes):
				pasta1 = pst + '/' + pasta
				shutil.move(caminho_origem, os.path.join(pasta1, arquivo))
				print(f'\nArquivo "{arquivo}" movido para {pasta1}/')
if acao:
    print('\nTodos os arquivos foram copiados.')
else:
    print('\nTodos os arquivos foram movidos.')
print('\nFim do programa')
