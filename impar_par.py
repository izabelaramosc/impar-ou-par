
entrada = input ('Digite um numero: ')

try:

 entrada = int(entrada)
 par_impar = entrada % 2 == 0
 par_impar_texto = 'impar'

 if par_impar: 
    par_impar_texto = 'par'

    print (f'o numero {entrada} é {par_impar_texto}')

except:
    print ('Voce não digitou um numero inteiro')
