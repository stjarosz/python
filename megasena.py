resultados = [[10,27,40,46,49,58], # 2009
              [ 2,10,34,37,43,50], # 2010
              [ 3, 4,29,36,45,55], # 2011
              [14,32,33,36,41,52], # 2012
              [20,30,36,38,47,53], # 2013
              [ 1, 5,11,16,20,56], # 2014
              [ 2,18,31,42,51,56], # 2015
              [ 5,11,22,24,51,53], # 2016
              [ 3, 6,10,17,34,37], # 2017
              [ 5,10,12,18,25,33], # 2018
              [ 3,35,38,40,57,58], # 2019
              [17,20,22,35,41,42], # 2020
              [12,15,23,32,33,46]] # 2021

# vetor inicializado com 0 representando cada possivel dezena
distribuicao = [0 for i in range(60)]

tamanho = len(resultados)
primeiro = 2009

# imprimindo os resultados
for i in range(tamanho):
   ano = primeiro + i
   print (str(ano) + ": " + str(resultados[i]))

# calculando   
for i in range(tamanho):
   for j in range(6):
       distribuicao[resultados[i][j]-1] += 1
       
print("--------------------------------------")

for k in range(60):
    print(str(k+1) + ": " + str(distribuicao[k]))
