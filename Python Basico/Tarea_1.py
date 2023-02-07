#Materia: Data Analisis. Tarea 1. Sergio Arturo Meza Miguel Huerta
#
import pandas as pd 
from pandas import ExcelWriter
archivo = 'C:/Users/SAMMH/Documents/Universidad/Analisis de Datos DCI/Python Basico/lista_correos.xlsx'
df = pd.read_excel(archivo,sheet_name='Hoja1')

print(df)
vocales = ['a', 'e','i','o', 'u']

LC = df['Correos'].to_numpy().tolist()
Dominios = []
for i in range(len(LC)):
    tempstr = LC[i]
    arroba =  tempstr.find('@')
    l = len(LC[i])
    a = arroba + 1
    while a < (l):
        if a == (arroba+1):
            StrDominio = tempstr[a]
            
        else:    
            StrDominio = StrDominio + tempstr[a]
        a+=1
    Dominios.append(StrDominio)
print(Dominios)

#Buscamos Dominios unicos
Dominios = list(set(Dominios))
print(Dominios)

#Buscamos vocales
NumVocal = []
for i in range(len(LC)):
    tempstr = LC[i]
    Contador = 0
    for j in range(len(vocales)):
        Contador = tempstr.count(vocales[j]) + Contador
    NumVocal.append(Contador)

UserVocals = df
UserVocals.insert(loc = 1, column='Vocales', value=NumVocal)
print(UserVocals)

#Exportamos a Excel 
Write = ExcelWriter('C:/Users/SAMMH/Documents/Universidad/Analisis de Datos DCI/Python Basico/Usuario_y_Vocales.xlsx')
UserVocals.to_excel(Write, 'Usuario_y_Vocales.xlsx', index= False)
Write.save()