## não são ordenados , não aceita duplicada, não pode ser modificado


cidade ={'belo', 'horizonte','natal','natal'}

cidade2 ={'campo grande ', '2','3','4'}

print (type(cidade))

print (cidade)

print('belo' in cidade)

print('feio' in cidade)

cidade.add('ola')

print(cidade)
cidade.update(cidade2)
print(cidade)