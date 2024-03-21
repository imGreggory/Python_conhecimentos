dic = {}
for i in range (0,3):
    aluno = input("Digite o nome do aluno: ")
    altura = float(input("Digite a altura do aluno: "))
    idade = int(input("Digite a idade do aluno: "))
    dic[aluno] = {"Altura":altura, "Idade":idade}
print(dic)