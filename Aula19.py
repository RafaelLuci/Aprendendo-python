'''
Interpolação de strings, tipo linguagem C

s - string
d , i - int
f - float
x , X - hexadecimal (ABCDF0123456789)

'''
nome = 'rafael'
preco = 1000.9876544
variavel ='%s, o preço total foi %.2f '% (nome,preco)
print(variavel)