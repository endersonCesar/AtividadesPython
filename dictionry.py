# aceita chave e valor 
# duplicado não é permitdido 

cod_uf={
    
    21:'piaui',
    22:'Campo grande'
}

print(type(cod_uf))
print(cod_uf.values())
print(cod_uf.keys())
print(cod_uf.get(21))
print(cod_uf)
cod_uf[29] = 'ola'
print(cod_uf)
