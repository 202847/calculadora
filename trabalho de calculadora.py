'''
Aluno:BRUNO HENRIQUE
Data:16/05
SAO 4 OPÇOES (+, -, *, /)
'''

print("1 adição")
print("2 subtração")
print("3 multiplicação")
print("4 divisão")
print("X sair")

escolha = ""
while True:
  print()
  escolha = input("digite uma escolha: ") #Recebe valor de usuario
  
  soma = 0

  match escolha.upper(): #Escolhe o que vai ser feito aqui
    case "1":
      while True:
        NUMERO = input("aperte um numero / P para parar: ")
        if NUMERO.upper() == "P":
          print(f"A conta deu", soma)
          break

        soma = soma + float(NUMERO) # aqui converte para float, para fazer o calculo
    case "2":
      while True:
        NUMERO = input("aperte um numero / P para parar: ")
        if NUMERO.upper() == "P":
          print(f"A conta deu", soma) # Exibe a conta
          break
        
        '''
          if necessario porque ele tem que ver se nao é o primeiro numero aqui que digitou 
        '''
        if soma != 0:
          soma = soma - float(NUMERO)
        else:
          soma = float(NUMERO)
    case "3":
      while True:
        NUMERO = input("aperte um numero / P para parar: ")
        if NUMERO.upper() == "P":
          print(f"A conta deu", soma) # Exibe a conta
          break
        
        if soma != 0:
          soma = soma * float(NUMERO)
        else:
          soma = float(NUMERO)
    case "4":
      while True:
        NUMERO = input("aperte um numero / P para parar: ")
        if NUMERO.upper() == "P":
          print(f"A conta deu", soma) # Exibe a conta
          break
        
        if soma != 0:
          soma = soma / float(NUMERO)
        else:
          soma = float(NUMERO)
      
    case "X": # Caso queira sair
      break
    case _: # Caso nada ser valido
      print("Insira um numero valido!")
      
  soma = 0
  escolha = ""