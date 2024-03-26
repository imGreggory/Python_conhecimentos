#Listas,tuplas,sets e dicionários.
#Exercicio 12
#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
def media_anual(medias):
    return sum(medias) / len(medias)

medias = []
dic_medias_acima = {}
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for mes in meses:
    media_mes = float(input(f"Digite a média do mês de {mes}: "))
    medias.append(media_mes)

media_anual_final = media_anual(medias)

for i, media_mes in enumerate(medias):
    if media_mes > media_anual_final:
        dic_medias_acima[meses[i]] = media_mes

print(f"A média anual das temperaturas é: {media_anual_final:.2f}")
print("Temperaturas acima da média anual:")
for mes, temperatura in dic_medias_acima.items():
    print(f"{mes}: {temperatura :.2f}")





