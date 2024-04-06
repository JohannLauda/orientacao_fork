from Animal import Animal, Cachorro

capivara = Animal(4)

print(capivara.numero_de_patas)
capivara.fazer_barulho()
#print(capivara.fazer_barulho())

doguinho = Cachorro(4, 'caramelo')

print(doguinho.numero_de_patas, "\n" + doguinho.cor)
doguinho.fazer_barulho()

dogao = Cachorro(4, 'preto')
print(dogao.numero_de_patas, "\n" + dogao.cor)
dogao.fazer_barulho()