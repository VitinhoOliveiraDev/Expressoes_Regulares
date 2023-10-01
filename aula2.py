# Meta caracteres: . ^ $ * + ? {} [] \ | ()
# | OU
# . Qualquer caractere (com exceção de quebra de linha)
# [] conjunto de caracteres
import re

texto = '''
João trouxe   flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhas, todos adultos atualmente.
maria, hoje sua esposa, ainda fez aquela café com pão de queijo nas tarde de
domingo. Também né! Ssendo a boa mineira que é, nunca esqueceu seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Jooooooooooãoooooooo, o café tá prontinho aqui, veeeem"!
'''

print(re.findall(r'João|Maria|adultos', texto)) # Selecionar o nome João ou Maria
# Exemplo: .
print(re.findall(r'João|Maria|ad....s', texto))
# Exemplo: []
print(re.findall(r'João|joão|Maria|', texto))
print(re.findall(r'[Jj]oão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'[a-z]aria', texto)) # Selecionando de a-z minúsculo
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto)) # Selecionando de a-z minúsculo e maiúsculo, e de 0 a 9
print(re.findall(r'jOãO|mAriA', texto, flags=re.I)) # Retornar os resultado com letras minúsculo e maiúsculo




