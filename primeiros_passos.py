import os, re
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
print('digite ano, mês e dia, não sendo necessário colocar 0 na frende de dias e meses menores que 10.')
#a = int(input('qual o ano '))
#b = int(input('mes '))
#c = int(input('dia '))
a2 =int(input('ano final :'))
b2 =int(input('mes final :'))
c2 =int(input('dia final :'))
a = a2-3
b = 1
c = 1
ação_analisada = input('digite a sigla da ação da mesma forma que está no site do yahoo finance: ')
maga = yf.Ticker(str(ação_analisada))
main_list = []
ano_inicial = a

def cria_listas(listas):

    for i in range(0, len(listas)):
        i = i*8
        yield listas[i:i+8]

def remove_dalista(lista):
    if 'Open' in lista:
        lista.remove('Open')
    if 'High' in lista:
        lista.remove('High')
    if 'Low' in lista:
        lista.remove('Low')
    if 'Close' in lista:
        lista.remove('Close')
    if 'Volume' in lista:
        lista.remove('Volume')
    if 'Dividends' in lista:
        lista.remove('Dividends')
    if 'Stock' in lista:
        lista.remove('Stock')
    if 'Splits' in lista:
        lista.remove('Splits')
    if 'Date' in lista:
        lista.remove('Date')

def resolve_data(data):
    if data > 9:
        pass
    else :
        data = '0' + str(data)


while a <= a2 :

    if a == a2:
        c = 1
        while b <= b2:
            if b ==b2:
                while c < c2:
                    k = c + 10
                    if k > c2:
                        resolve_data(c)
                        resolve_data(b)
                        k = c2
                        resolve_data(k)
                        h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(c2), interval = '1d')
                        h = str(h)
                                                
                    else:
                        resolve_data(c)
                        resolve_data(b)
                        h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-' +str(k), interval = '1d')
                        h = str(h)

                    j = h.split()
                    remove_dalista(j)
                    j = list(cria_listas(j))
                    main_list = main_list + j
                    c = c+ 10
            

                    
            if b < b2:
                if b == 1 or b==3 or b==5 or b ==7 or b == 8 or b==10 or b == 12:
                    while c <= 31:
                        k = c + 10
                        b1 = b
                        if k > 31:
                            b = b + 1
                            k = k - 31
                            resolve_data(c)
                            resolve_data(b)
                            resolve_data(k)
                            h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                            h = str(h)
                            b = b1
                         
                        else :
                            resolve_data(c)
                            resolve_data(b)
                            h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-' +str(k), interval = '1d')
                            h = str(h)
                        
                        j = h.split()
                        remove_dalista(j) 
                        j = list(cria_listas(j))
                        main_list = main_list + j
                        c = c + 10
                if b == 4 or b==6 or b==9 or b ==11 :
                    while c <=30:
                        b1 = b
                        k = c + 10
                        if k > 30:
                            b= b + 1
                            resolve_data(c)
                            resolve_data(b)
                            k = k - 30
                            resolve_data(k)
                            h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                            h = str(h)
                            b = b1
                        
                        else :
                            resolve_data(c)
                            resolve_data(b) 
                            h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                            h = str(h)

                        j = h.split()
                        remove_dalista(j)
                        j = list(cria_listas(j))
                        main_list = main_list + j
                        c = c + 10
                if b ==2:
                    if a%4==0:
                        while c<=29:
                            b1 = b
                            k = c + 10
                            if k > 29:
                                b= b + 1
                                resolve_data(c)
                                resolve_data(b)
                                k = k - 29
                                resolve_data(k)
                                h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-' +str(k), interval = '1d')
                                h = str(h)
                                b= b1
                               
                            else :
                                resolve_data(c)
                                resolve_data(b)
                                h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                                h = str(h)

                            j = h.split()                               
                            remove_dalista(j)                               
                            j = list(cria_listas(j))
                            main_list = main_list + j
                            c = c + 10
                    else:
                        while c <= 28:
                            b1 = b
                            k = c + 10
                            if k > 29:
                                b= b + 1
                                k = k - 29
                                resolve_data(c)
                                resolve_data(b)
                                resolve_data(k)
                                h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-' +str(k), interval = '1d')
                                h = str(h)
                                b = b1
                        
                            else :
                                resolve_data(c)
                                resolve_data(b)
                                h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                                h = str(h)
                            
                            j = h.split()   
                            remove_dalista(j)    
                            j = list(cria_listas(j))
                            main_list = main_list + j
                            c = c + 10
                
            c = 1
            b = b + 1
        

                    
                

        
    if a < a2:
        while b <=12 :
            if b == 1 or b==3 or b==5 or b ==7 or b == 8 or b==10:
                while c <= 31:
                    b1 = b
                    k = c + 10
                    if k > 31: 
                        b= b + 1                      
                        resolve_data(c)
                        resolve_data(b)
                        k = k - 31
                        resolve_data(k)
                        h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                        h = str(h)
                        b = b1
                     
                    else :
                        resolve_data(c)
                        resolve_data(b)
                        h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                        h = str(h)
                    j = h.split()
                    remove_dalista(j)
                    j = list(cria_listas(j))
                    main_list = main_list + j
                        

                    c = c + 10
            
                
            if b == 4 or b==6 or b==9 or b ==11 :
                while c <=30:
                    b1 = b
                    k = c + 10
                    if k > 30:
                        b= b + 1
                        resolve_data(c)
                        resolve_data(b)
                        k = k - 30
                        resolve_data(k)
                        h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                        h = str(h)
                        b = b1
                    
                    else :
                        resolve_data(c)
                        resolve_data(b)
                        h = maga.history(start = str(a) + "-" + str(b) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                        h = str(h)
                    j = h.split()
                    remove_dalista(j)
                    j = list(cria_listas(j))
                    main_list = main_list + j
                    c = c + 10
            if b ==12:
                while c<=31:
                    a1 = a
                    b1 = b
                    k = c + 10
                    if k > 31:
                        a = a +1
                        b= 1
                        resolve_data(c)
                        resolve_data(b)
                        k = k - 31
                        resolve_data(k)
                        h = maga.history(start = str(a1) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                        h = str(h)
                        b = b1
                        a = a1
                    else :
                        resolve_data(c)
                        resolve_data(b)
                        h = maga.history(start = str(a) + "-" + str(b) + '-'+str(c), end = str(a) + "-" + str(b) + '-' +str(k), interval = '1d')
                        h = str(h)
                    j = h.split()
                    remove_dalista(j)
                    j = list(cria_listas(j))
                    main_list = main_list + j
                    c = c + 10

            if b ==2:
                if a%4==0:
                    while c<=29:
                        b1 = b
                        k = c + 10
                        if k > 29:
                            b= b + 1
                            resolve_data(c)
                            resolve_data(b)
                            k = k - 29
                            resolve_data(k)
                            h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                            h = str(h)
                            b = b1
                        
                        else :
                            resolve_data(c)
                            resolve_data(b)
                            h = maga.history(start = str(a) + "-" + str(b) + '-'+str(c), end = str(a) + "-" + str(b) + '-' +str(k), interval = '1d')
                            h = str(h)
                        j = h.split()
                        remove_dalista(j)
                        j = list(cria_listas(j))
                        main_list = main_list + j
                        c = c + 10
                else:
                    while c <= 28:
                        b1 = b
                        k = c + 10
                        if k > 28:
                            b= b + 1
                            resolve_data(c)
                            resolve_data(b)
                            k = k - 28
                            resolve_data(k)
                            h = maga.history(start = str(a) + "-" + str(b1) + '-'+ str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                            h = str(h)
                            b = b1
                         
                        else :
                            resolve_data(c)
                            resolve_data(b)
                            h = maga.history(start = str(a) + "-" + str(b) + '-' +str(c), end = str(a) + "-" + str(b) + '-'+ str(k), interval = '1d')
                            h = str(h)
                        j = h.split()
                        remove_dalista(j)
                        j = list(cria_listas(j))
                        main_list = main_list + j
                        c = c + 10
            
            b = b + 1
            c = 1

        b = 1             
    a = a + 1

#############################################################################main_list[4].plot(title = 'MGLU3.SA')
##########################################################
#é necessário fazer um algoritimo que vai ler a data a cada 10 dias
#cada intervalo será uma lista que deve ser adicionado a todas as s anteriores
#a partir da segunda lista, é necessário apagar o cabeçalho
#lembre-se dos meses com dias diferentes e dos anos bissexto
#########################################################
##########################################################################plt.show(   )
for i in range(len(main_list)):
    if [] in main_list:
        main_list.remove([])
    if ['Close,', 'Volume]', 'Index:', '[]'] in main_list:
        main_list.remove(['Close,', 'Volume]', 'Index:', '[]'])
    if ['Empty', 'DataFrame', 'Columns:', '[Open,', 'High,', 'Low,', 'Close,', 'Adj'] in main_list:
        main_list.remove(['Empty', 'DataFrame', 'Columns:', '[Open,', 'High,', 'Low,', 'Close,', 'Adj'])
for k in range(len(main_list)):
    for i in range(8):
        if i == 0:
            pass
        else :
            main_list[k][i] = float(main_list[k][i])
            j = round(main_list[k][i], 2)
            main_list[k][i] = j
for i in range(1, len(main_list)-10):
    if main_list[i][0] == main_list[i -1][0] :
        main_list.remove(main_list[i-1])


s = []
for i in main_list:
    if i not in s:
        s.append(i)
main_list = s
s = [['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']]
main_list = s + main_list
#print(main_list)
# a primeira parte de minerar a data está feita(aparentemente, funcionando perfeitamente)
#agora, é necessário descobrir as datas
#a variação de preço no ano
#a variação de preço desde o início
#a variação de preço desde o início do mês
#as 2 maiores baixas
#o maior período de baixa
#os 2 maiores picos de alta em um intervalo de 1 ano dias
#gráficom com o preço desde a análise
#gráfico com a variação de preço do ano inteiro dos 3 últimos anos
#gráfico com os valores mais baixos
#1: variação de preço no ano
#lembre da ordem : Date-Open-High-low-close
preço_início = 0
for i in range(len(main_list)):
    if main_list[i][0] == str(a2) + '-01-01' :
        preço_início = main_list[i][1]
        break                                                              #aqui está feito a parte 1
    if main_list[i][0] == str(a2) + '-01-02' :
        preço_início = main_list[i][1]
        break
    if main_list[i][0] == str(a2) + '-01-03' :
        preço_início = main_list[i][1]
        break
preço_final = main_list[len(main_list)-1][4]
variação_preço = float(preço_final) - float(preço_início)
variação_percentual = ((float(preço_final)-float(preço_início))/(float(preço_início)))*100
#2: variação de preço desde o início
preço_início_2 = main_list[1][1]
variação_preço_2 = float(preço_final) - float(preço_início_2)
variação_percentual_2 = ((float(preço_final)-float(preço_início_2))/(float(preço_início_2)))*100
if variação_percentual_2 < 0:
    variação_percentual_2 = (-1)*variação_percentual_2                                    #aqui está feita a parte 2
#3: variação de preço desde o início do mês
for i in range(len(main_list)):
    if main_list[i][0] == str(a2) + '-' + str(b2) + '-01' :
        preço_início_mês = main_list[i][1]
        break                                                              #aqui está feito a parte 3
    if main_list[i][0] == str(a2) + '-' + str(b2) + '-02' :
        preço_início_mês = main_list[i][1]
        break
    if main_list[i][0] == str(a2) + '-' + str(b2) + '-03' :
        preço_início_mês = main_list[i][1]
        break
variação_preço_mês = float(preço_final) - float(preço_início_mês)                               
variação_percentual_mês = ((float(preço_final)-float(preço_início_mês))/(float(preço_início_mês)))*100
#4: as maiores baixas de cada mês nos últimos dois anos
w= re.compile(str(a2) + r'[-][0][123456]')
primeiro_semestre_a2 = []
for i in range(len(main_list)):
  for y in main_list[i][0]:                                                          #aqui já consegui divir a lista em anos de interesse
    z = w.findall(main_list[i][0])
    if len(z) > 0:
      primeiro_semestre_a2.append(main_list[i])
      break
w= re.compile(str(a2) + r'[-][0][789]')                        #|[-][1][0]|[-][1][2]|[-][1][1]
w1 = re.compile(str(a2) + r'[-][1][0]')
w2 = re.compile(str(a2) + r'[-][1][1]')
w3 = re.compile(str(a2) + r'[-][1][2]')
segundo_semestre_a2 = []
for i in range(len(main_list)):
  for y in main_list[i][0]:                                                           #aqui já consegui divir a lista em anos de interesse
    z = w.findall(main_list[i][0])
    if len(z) > 0:
      segundo_semestre_a2.append(main_list[i])
      break
    z = w1.findall(main_list[i][0])                                                 # já separamos cada semestre do primeiro ano
    if len(z) > 0:
      segundo_semestre_a2.append(main_list[i])
      break
    z = w2.findall(main_list[i][0])
    if len(z) > 0:
      segundo_semestre_a2.append(main_list[i])
      break
    z = w3.findall(main_list[i][0])
    if len(z) > 0:
      segundo_semestre_a2.append(main_list[i])
      break
segundo_semestre_ano_anterior = []
primeiro_semestre_ano_anterior = []
if a2-1 >= ano_inicial:
    w= re.compile(str(a2-1) + r'[-][0][123456]')
    for i in range(len(main_list)):
      for y in main_list[i][0]:                                                          
        z = w.findall(main_list[i][0])
        if len(z) > 0:
          primeiro_semestre_ano_anterior.append(main_list[i])
          break
    w= re.compile(str(a2-1) + r'[-][0][789]')                        
    w1 = re.compile(str(a2-1) + r'[-][1][0]')
    w2 = re.compile(str(a2-1) + r'[-][1][1]')
    w3 = re.compile(str(a2-1) + r'[-][1][2]')
    for i in range(len(main_list)):
        for y in main_list[i][0]:                                                           
            z = w.findall(main_list[i][0])
            if len(z) > 0:
              segundo_semestre_ano_anterior.append(main_list[i])
              break
            z = w1.findall(main_list[i][0])                                                 
            if len(z) > 0:
              segundo_semestre_ano_anterior.append(main_list[i])
              break
            z = w2.findall(main_list[i][0])
            if len(z) > 0:
              segundo_semestre_ano_anterior.append(main_list[i])
              break
            z = w3.findall(main_list[i][0])
            if len(z) > 0:
              segundo_semestre_ano_anterior.append(main_list[i])
              break
#print(primeiro_semestre_ano_anterior)
#print(len(primeiro_semestre_ano_anterior))
#print(segundo_semestre_ano_anterior)
#print(len(segundo_semestre_ano_anterior))
#agora já temos as listas de cada semestre dos últimos 2 anos
#achando os 2 maiores valores do primeiro ano
k = primeiro_semestre_a2[0][3]
for i in range(len(primeiro_semestre_a2)):
    if primeiro_semestre_a2[i][3] < k:
        y = primeiro_semestre_a2[i][0]
        k = primeiro_semestre_a2[i][3]
        y5=y
        k5=k
z = segundo_semestre_a2[0][3]
for i in range(len(segundo_semestre_a2)):
    if segundo_semestre_a2[i][3] < z:
        y = segundo_semestre_a2[i][0]
        z = segundo_semestre_a2[i][3]
        y7=y
        z7 = z
k = primeiro_semestre_ano_anterior[0][3]
for i in range(len(primeiro_semestre_ano_anterior)):
    if primeiro_semestre_ano_anterior[i][3] < k:
        y = primeiro_semestre_ano_anterior[i][0]
        k = primeiro_semestre_ano_anterior[i][3]
        y1=y
        k1=k
z = segundo_semestre_ano_anterior[0][3]
for i in range(len(segundo_semestre_ano_anterior)):
    if segundo_semestre_ano_anterior[i][3] < z:
        y = segundo_semestre_ano_anterior[i][0]
        z = segundo_semestre_ano_anterior[i][3]
        y3=y
        z3=z
#agora os maiores valores
k = primeiro_semestre_a2[0][3]
for i in range(len(primeiro_semestre_a2)):
    if primeiro_semestre_a2[i][3] > k:
        y = primeiro_semestre_a2[i][0]
        k = primeiro_semestre_a2[i][3]
        y6 = y
        k6=k
z = segundo_semestre_a2[0][3]
for i in range(len(segundo_semestre_a2)):
    if segundo_semestre_a2[i][3] > z:
        y = segundo_semestre_a2[i][0]
        z = segundo_semestre_a2[i][3]
        z8=z
        y8=y
k = primeiro_semestre_ano_anterior[0][3]
for i in range(len(primeiro_semestre_ano_anterior)):
    if primeiro_semestre_ano_anterior[i][3] > k:
        y = primeiro_semestre_ano_anterior[i][0]
        k = primeiro_semestre_ano_anterior[i][3]
        y2=y
        k2=k
z = segundo_semestre_ano_anterior[0][3]
for i in range(len(segundo_semestre_ano_anterior)):
    if segundo_semestre_ano_anterior[i][3] > z:
        y = segundo_semestre_ano_anterior[i][0]
        z = segundo_semestre_ano_anterior[i][3]
        y4=y
        z4=z
#agora só precisamos colocar o gráfico e passar tudo para um arquivo word
#criando gráfico da análise desde o início
print('a maior baixa do primeiro semestre de ' +  str(a2 -1) + ' foi em: ' + y1 + '. No valor de : ', k1)
print('o maior valor do primeiro semestre de ' + str(a2 -1)+ ' foi em: ' + y2 + '. No valor de : ', k2)
print('a maior baixa do segundo semestre de ' +  str(a2 -1)+  ' foi em: ' + y3 + '. No valor de : ', z3)
print('o maior valor segundo semestre de ' + str(a2 -1) + ' foi em: ' + y4 + '. No valor de : ', z4)
print('a maior baixa do primeiro semestre de ' +  str(a2) +' foi em: ' + y5 + '. No valor de : ', k5)
print('o maior valor do primeiro semestre de ' + str(a2 )+ ' foi em: ' + y6 + '. No valor de : ', k6)
print('a maior baixa do segundo semestre de ' +  str(a2) +' foi em: ' + y7 + '. No valor de : ', z7)
print('o maior valor do segundo semestre de ' + str(a2 ) + ' foi em: ' + y + '. No valor de : ', z)



def cria_eixo(nova_lista, lista, coluna):
    for i in range(len(lista)):
        nova_lista.append(lista[i][coluna])

def acha_index(lista, ano):
    x = re.compile(str(ano)+ r'[-][01][123456789][-][01][0123456789]')
    k = 0
    for i in range(len(lista)):
        j = x.findall(lista[i])
        if len(j)>0 and k == 0 :
            w = j
            k = k + 1
            return w
eixo_x = []
cria_eixo(eixo_x, main_list, 0)
k = acha_index(eixo_x, a2-2)
k = eixo_x.index(k[0])

eixo_y = []
eixo_y1 = []
eixo_y2 = []
cria_eixo(eixo_y, main_list, 3)
cria_eixo(eixo_y1, main_list, 1)
cria_eixo(eixo_y2, main_list, 2)
del eixo_x[0:k]
del eixo_y[0:k]
del eixo_y1[0:k]
del eixo_y2[0:k]
fig, ax =plt.subplots()
ax.plot(eixo_x, eixo_y, 'r',  label = 'maior baixa do dia')
#ax.plot(eixo_x, eixo_y1)
ax.plot(eixo_x, eixo_y2, 'b', label = 'maior alta do dia')
lista_grf =[]
i = 2
x=0
while i >=0:
    j = acha_index(eixo_x, a2 -i)
    lista_grf.append(j)                                #já temos o gráfico com os preços mais 
    
    i = i - 1
    x= x+1

s = []
for i in lista_grf:
    for item in i:
        s.append(item)
s.append(main_list[len(main_list)-1][0])
lista_grf = s
ax.set_xticks(lista_grf)
plt.show()
print('x')

