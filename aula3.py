# Quantificadores
# Meta caracteres: ^ $ \ ()
# * 0 ou n
# + 1 ou m {1,}
# ? 0 ou 1
# {min, max} 
# {10,}10 ou mais
# {,10} De zero a 1
# {10} Espeficamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+
import re

texto = '''
João trouxe   flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhas, todos adultos atualmente.
maria, hoje sua esposa, ainda fez aquela café com pão de queijo nas tarde de
domingo. Também né! Ssendo a boa mineira que é, nunca esqueceu seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Jooooooooooãoooooooo, o café tá prontinho aqui, veeemm veeem"!
'''

# Exemplo: +
print(re.findall(r'jo+ão+', texto, flags=re.I)) # O quantificado é aplicado a coisa e estiver a esquerda do quantificador
print(re.findall(r'j[a-zA-Z]+ão+', texto, flags=re.I))

# Exemplo: {1,}
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))

#print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I)) # Substituição de joão para felipe
#print(re.sub(r'jo{1,}ão{1,}', 'Felipe', texto, flags=re.I)) # Esse quantificado vai dizer que pode repetir 1 ou mais vezes

#Exemplo: {10} Especificamente 10
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall(r'ama', texto2, flags=re.I))

#Exemplo usando []
print(re.findall(r'ama[do]', texto2, flags=re.I)) # Dessa forma irá puxar ama + d pois esta lendo um letra apenas (d)
print(re.findall(r'ama[do]{2}', texto2, flags=re.I)) # Dessa forma vai fazer a leitura 2x, ou seja, 1 letra D 2 letra O

# Exemplo usando *
print(re.findall(r'ama[do]*', texto2, flags=re.I)) # Vai está retornando os dois ama e amado
print(re.findall(r'ama[do]{0,2}', texto2, flags=re.I))
