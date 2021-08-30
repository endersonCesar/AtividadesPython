def imc(peso,altura):
    imc  = peso/(altura**2)
    if imc<18.5:
        print('baum')
    elif imc<20.1:
        print('ruim')
    else:
        print('fudeu')
    return

peso = int(input('digite o peso: '))
altura = int(input('digite a altura: '))
imc(peso,altura)