import numpy as np 

#indexação de array 
x = np.linspace(start =10,stop = 100,num = 10)
print('x: ',x)
print('shape',x.shape)

#extração de elementos 
print('segundo elemento ',x[1])
print('ultimo elemento ',x[-1])

# slicing: extração de subarray 1D :
print('dois primeiros elementos ',x[0:2])
print('dois primeiros elementos ',x[:2])
print('dois ultimos elementos ',x[-2:])

## slicing: extração de subarray 2D :

x = x.reshape(2,5) # remodela para um array de 2 linhas com 5 colunas 
print('x:\n',x)


#extração de elementos 2d 
print('primeira linha, segunda coluna ',x[0,2])
print('primeira linha,ultima coluna ',x[0,4])


#operação slicing 2d
print('primeira linha inteira:  ',x[0,:])
print('primeira linha,segunda e quarta coluna: ',x[0,1:4])
print('ultima coluna inteira: ',x[:,[-1]])
print('pegando o valor 20 e 30: ',x[0, 1:3])



# atenção com compartilamento de memória em subarrays 
x = np.array([1,2,3])
print('x antes:  ',x)
y =x[:2]
y[0]=-100 # alteração de y também altera x
print('x depos: ',x) 



# como evitar
x = np.array([1,2,3])
print('x antes:  ',x)
y =x[:2].copy()
y[0]=-100 # alteração de y também altera x
print('x depos: ',x) 