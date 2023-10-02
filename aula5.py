# Grupos e Retrovisores

# Quantificadores
# Meta caracteres: ^ $ \ ()
# * 0 ou n
# + 1 ou m {1,}
# ? 0 ou 1

import re
from pprint import pprint
texto='''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> </div>1</div>
'''
#cpf = '147.852.963-12'
#print(re.findall(r'[0,9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))

#print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto)) 

#tags = re.findall(r'(<([dpiv]{1,3})>(.*?)<\/\2>)', texto)
#pprint(tags)

print(re.sub(r'(<(.*?)>)(.*?)(<\/\2>)', r'\1 Mais \3 Coisas \4', texto))

#for tag in tags:
#    um, dois, tres = tag
#    print(tres)
