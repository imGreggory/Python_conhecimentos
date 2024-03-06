quantidade_passos = int(input("Escreva um numero:"))
if quantidade_passos >=0:
  if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")
  else:
    for i in range (1,quantidade_passos+1):
      if i == 1:
        print(f"Explorador: 1 passo")
      else:
        print(f"Explorador: {i} passos")