#Greedy e non-greedy (lazy)

# Quantificadores
# Meta caracteres: ^ $ \ ()
# * 0 ou n
# + 1 ou m {1,}
# ? 0 ou 1

import re
texto='''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>

<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>Frase </div>
'''


print(re.findall(r'<[pdiv]{1,3}>.+<\/[pdiv]{1,3}>', texto)) # Considerado como comportamento guloso
print(re.findall(r'<[pdiv]{1,3}>.+<\/[pdiv]{1,3}>', texto)) # Para que o comportamento seja não guloso