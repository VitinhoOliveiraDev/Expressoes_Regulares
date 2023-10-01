import re

# findall = (Localizar) search = (Procurar) sub = (Substituir)
# compile = (compilar)

string = "Este é um teste de expressões teste regulares."
print(
    re.search(r"teste", string)
)  # Search vai encontrar dentro da expressão regulara a palavra teste
print(
    re.findall(r"teste", string)
)  # Findall vai retornar quantas palavras teste possui na expressão
print(re.sub(r"teste", "ABCD", string))  # Será trocado os teste para ABCD
print(
    re.sub(r"teste", "ABCD", string, count=1)
)  # Será trocado apenas 1 vez o teste para ABCD

# Compile
regexp = re.compile(r"teste")
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub("DEF", string))