# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import matplotlib.pyplot as plt

#%% 11
matriz_1x1 = np.array([7,1,7])
matriz_2x3 = np.array([[4,6,3],[4,6,3]])
matriz_zeros_3x3 = np.zeros((3,3))

print(matriz_1x1)
print(matriz_1x1.shape)
print(matriz_2x3)
print(matriz_2x3.shape)
print(matriz_zeros_3x3)
print(matriz_zeros_3x3.shape)

#%% 12
matriz_identidad_5x5 = np.identity(5)
print(f"matriz_identidad_5x5\n {matriz_identidad_5x5}")

matriz_aleatoria_3x3 = np.random.random((3,3))
print(f"matriz_aleatoria_3x3\n {matriz_identidad_5x5}")
#%% 13

enteros1 = np.random.randint(0, 101,(2,2))
enteros2 = np.random.randint(0, 101,(2,2))

print("enteros1: \n", enteros1)
print("enteros2: \n", enteros2)
print("suma \n", enteros1 + enteros2)
print("multiplicacion \n", enteros1 * enteros2)

#%% 14
import numpy as np

enteros100 = np.random.randint(0, 101,(5,5))
max = np.max(enteros100)
min = np.min(enteros100)
mean = np.mean(enteros100)
print("Valor max: \n", max)
print("Valor min: \n", min)
print("Valor medio: \n", mean)

#%%matpltlib
import matplotlib.pyplot as plt
x= [1,2,3,4]
y = [10,20,25,30]
plt.plot(x,y,marker = 'o')
plt.title("Ejemplo de grafico")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.show()


fig, axs = plt.subplots(2, 2, figsize=(8,4))
axs[0,0].plot(x,y,marker = 'o')
axs[0,0].set_title("linea")
axs[0,1].bar(x,y, color = 'orange')
axs[0,1].set_title('barras')
axs[1,0].scatter(x,y, color = 'orange')
axs[1,0].set_title('dispersion')
axs[1,1].hist(y, bin=4, color ='purple')
axs[1,0].set_title('histograma')


#%% 15
x = [1,2,3,4]
y = [10,20,25,30]
plt.plot(x,y,marker = 'o', color= 'blue')
plt.title("Grafico con marker y color")
plt.xlabel("eje x")
plt.show()


meses = ["enero", "febrero", "marzo"]
ventas = [1000, 1500, 2000]
plt.plot(meses,ventas,marker = 'o', color= 'green')
plt.xlim(0.5)
plt.ylim(10.5)


fig, axs = plt.subplots(1, 2, figsize=(8,3))
axs[0].plot(x,y,linestyle = '--', color= 'blue')
axs[1].plot(meses, ventas, marker = '*', color= 'magenta')



#%% pandas
import pandas as pd
ruta = r"C:\Users\Mañana\Documents\santi\unsdg_2002_2021.csv"
df = pd.pandas.read_csv(ruta, sep=',')

print( df.head() )
print("-----------------------------\n")
print( df.info() )
print("-----------------------------\n")
print( df.describe() )
print("-----------------------------\n")
'''
print( df.colums.values )
print("-----------------------------\n")
print( df.index() )
print("-----------------------------\n")
'''

print(df.sort_values("dt_year", ascending=True))

print(df.drop_duplicates)
print(df.drop_duplicates(subset='dt_year'))

#%%
import pandas as pd
ruta = r"C:\Users\Mañana\Documents\santi\unsdg_2002_2021.csv"
df = pd.pandas.read_csv(ruta, sep=',')

print("mostrar los nombres de las columnas")
print( df.columns )
print("-----------------------------\n")

print("mostrar las 5 primeras filas")
print( df.head() )
print("-----------------------------\n")

print("eliminar los registros duplicados")
print(df.drop_duplicates)
print("-----------------------------\n")

print("mostrar la fila 3 completa")
print(df.iloc[2])

print("mostrar todos los registros del año 2010")
print( df.loc[df['dt_year']==2010] )

#%% simpleImputer and StandardScaler
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

#cargar el dataset
df = pd.read_csv(r"C:\Users\Mañana\Documents\santi\unsdg_2002_2021.csv")

#seleccionar categoria y crear dataset
dfObjetivo = df[["country", "level_of_development"]]
dfObjetivo = dfObjetivo.drop_duplicates()
print("prueba con df normal------")
print(df.head())
print("\n\nprueba con dfObjetivo========")
print(dfObjetivo.head())

dfCaracteristicas = df.drop(columns=["dt_year", "dt_date", "region"])
print("\n\nprueba con dfCaracteristicas========")
#agrupar por pais y calcular la media
dfCaracteristicas = dfCaracteristicas.groupby("country").mean(numeric_only=True)
print(dfCaracteristicas)

imputador = SimpleImputer(missing_values = np.nan, strategy="most_frequent")
dfImputado = imputador.fit_transform(dfCaracteristicas)
#convertirlo a dataframe
dfImputado = pd.DataFrame(dfImputado,
                          index=dfCaracteristicas.index,
                          columns=dfCaracteristicas.columns)

print("\n\nprueba con dfImputado========")
print(dfImputado.head())

#estandarizar los datos
escalador = StandardScaler()
dfEstandarizado = escalador.fit_transform(dfImputado)
#convertirlo a dataframe
X = pd.DataFrame(dfEstandarizado,
                 index=dfCaracteristicas.index,
                 columns=dfCaracteristicas.columns)

#preparamos la variable objetivo Y
Y = dfObjetivo.set_index("country")

#mostramos result
print("\n\n------X (caracteristicas estandarizadas)")
print(X.head())
print("\n\n------Y (nivel de desarrollo)")
print(Y.head())
print("\n\n------dfObjetivo será como Y pero con otro index")
print(dfObjetivo)

#prueba con train_test_split()
from sklearn.model_selection import train_test_split
X = X.loc[Y.index]
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=99
)

print("\n-------TAMAÑOS de los conjuntos")
print("\n-------X_train", X_train.shape)
print("\n-------X_test", X_test.shape)
print("\n-------Y_train", Y_train.shape)
print("\n-------Y_test", Y_test.shape)
# print("\n-------Y TEST", Y_test)
# print("\n-------Y TRAIN", Y_train)
# print("\n-------X_train", X_train)

#%%1
import pandas as pd

#cargar el dataset
df = pd.read_csv(r"C:\Users\Mañana\Documents\santi\unsdg_2002_2021.csv")

#crear un nuevo dataset
df_salud = df[["country", "mortality_rate_perc", "annual_growth_rate_perc"]]
df_salud.drop_duplicates()

print(df_salud.head())

#%%2
import pandas as pd

#cargar el dataset
df = pd.read_csv(r"C:\Users\Mañana\Documents\santi\unsdg_2002_2021.csv")

df_caracteristicas = df.drop(columns=["dt_year", "dt_date", "region"])
#Agrupar por country y calcular la media .mean
df_grouped = df_caracteristicas.groupby("country").mean(numeric_only=True)

print(df_grouped)

#%%3
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

#cargar el dataset
df = pd.read_csv(r"C:\Users\Mañana\Documents\santi\unsdg_2002_2021.csv")

df_caracteristicas = df.drop(columns=["dt_year", "dt_date", "region"])
#Agrupar por country y calcular la media .mean
df_grouped = df_caracteristicas.groupby("country").mean(numeric_only=True)
#----------------------------------------------------------------------

#imputar valores faltantes NaN
imputador = SimpleImputer(missing_values = np.nan, strategy="most_frequent")
#remplaza los NaN (la salida es un numpy)
df_imputado = imputador.fit_transform(df_grouped)
#convertirlo a dataframe
df_imputado = pd.DataFrame(df_imputado,
                          index=df_grouped.index,
                          columns=df_grouped.columns)

print(df_imputado.head())


#%%4
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

#cargar el dataset
df = pd.read_csv(r"C:\Users\Mañana\Documents\santi\unsdg_2002_2021.csv")

df_caracteristicas = df.drop(columns=["dt_year", "dt_date", "region"])
#Agrupar por country y calcular la media .mean
df_grouped = df_caracteristicas.groupby("country").mean(numeric_only=True)
#----------------------------------------------------------------------

#imputar valores faltantes NaN
imputador = SimpleImputer(missing_values = np.nan, strategy="most_frequent")
#remplaza los NaN (la salida es un numpy)
df_imputado = imputador.fit_transform(df_grouped)
#convertirlo a dataframe
df_imputado = pd.DataFrame(df_imputado,
                          index=df_grouped.index,
                          columns=df_grouped.columns)
#--------------------------------------------------------------

#estandarizar los datos

escalador = StandardScaler()

df_estandarizado = escalador.fit_transform(df_imputado)


#convertirlo a dataframe
X = pd.DataFrame(df_estandarizado,
                 index=df_imputado.index,
                 columns=df_imputado.columns)

Y = df[["country", "mortality_rate_perc"]].drop_duplicates
Y = Y.set_index("country")


print(X.head())
print(Y.head())


#%%
#% Cargar conjuntos de datos de Scikit-learn
from sklearn import datasets
import pandas as pd
# Cargar datasets
datos_diabetes = datasets.load_diabetes()
#datos_boston = datasets.load_boston()
datos_iris = datasets.load_iris()
datos_cancer = datasets.load_breast_cancer()
datos_vinos = datasets.load_wine()
datos_olivetti = datasets.fetch_olivetti_faces()
datos_digits = datasets.load_digits()

# Elegir dataset a explorar
datos = datos_iris
print(datos.keys()) # claves del dataset
print("\n Nombres de características (columnas X) =====")
print(datos.feature_names)
print("\n Nombres del objetivo (clases Y) =====")
print(datos.target_names)
print("\n DESCR: descripción del dataset =====")
print(datos.DESCR)

'''
df_X = pd.DataFrame(datos.data,
                    columns = datos.feature_names,
                    index=datos.index)
'''


#%%
from sklearn import datasets
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

# Cargar el dataset breast_cancer
datos_cancer = datasets.load_breast_cancer()

# Crear el DataFrame de pandas
dfCancer = pd.DataFrame(data=datos_cancer.data, columns=datos_cancer.feature_names)

# Mostrar las cinco primeras filas del DataFrame
print("### 1. Cinco primeras filas del DataFrame dfCancer ###")
print(dfCancer.head())

#-----2

from sklearn.impute import SimpleImputer
import numpy as np


dfImputar = dfCancer.replace(0.0, np.nan)

# Inicializar y configurar el SimpleImputer con la estrategia "most_frequent"
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

# Ajustar y transformar los datos
# fit_transform devuelve un array de numpy, no un DataFrame
datos_imputados = imputer.fit_transform(dfImputar)

# Guardar el resultado en un nuevo DataFrame llamado dfImputado
dfImputado = pd.DataFrame(data=datos_imputados, columns=dfCancer.columns)

# Mostrar el DataFrame resultante
print("\n### 2. Primeras filas del DataFrame dfImputado (después de imputar) ###")
print(dfImputado.head())

#-----3

# Crear una copia del dfImputado
dfCancerModificado = dfImputado.copy()

# Eliminar la columna "worst symmetry"
dfCancerModificado = dfCancerModificado.drop(columns=["worst symmetry"])

# Ordenar el DataFrame por la columna "mean texture" en orden ascendente
dfCancerModificado = dfCancerModificado.sort_values(by="mean texture", ascending=True)

# Mostrar las primeras filas del DataFrame modificado y ordenado
print("\n### 3. Primeras filas de dfCancerModificado (columna eliminada y ordenado) ###")
print(dfCancerModificado.head())

# Mostrar la lista de columnas para verificar que "worst symmetry" ha sido eliminada
print("\nColumnas restantes:")
print(dfCancerModificado.columns.tolist())


#%% practica viii walmart
import pandas as pd
import random
 
dfDatos = pd.DataFrame()
 
def cargarDatos():
    dfDatos = pd.read_csv(r"C:\Users\Mañana\Documents\santi\walmart.csv")
    valoresPosiblesWeeklyRain =["Ninguna","Pocas","Medias","Muchas"]
    weekly_Rains= []
    for i in range(dfDatos.shape[0]):
        weekly_Rains.append(valoresPosiblesWeeklyRain[random.randint(0,3)])
    dfDatos['Weekly_Rains'] = weekly_Rains
    valoresPosiblesWeeklyDiscounts = ["Carnes","Pescados","Restos"]
    weekly_Discounts = []
    for i in range(dfDatos.shape[0]):
        weekly_Discounts.append(valoresPosiblesWeeklyDiscounts[random.randint(0,2)])
    dfDatos["Weekly_Discounts"] = weekly_Discounts
    dfDatos = dfDatos[dfDatos.Store == 1]
    return dfDatos
 
 
dfDatos = cargarDatos()
print(dfDatos.shape[0])
print("\n\nTipo de datos:")
print(type(dfDatos))
print("\n\nDataframe dfDatos----------:\n")
print(dfDatos)
print("\n\nVer si hay algun null----------:\n")
print(dfDatos.isnull())
print("\n\nLa suma de cuantos null hay----------:\n")
print(dfDatos.isnull().sum())
 
 
dfDatos = dfDatos.dropna(subset=['Store', 'Date', 'Weekly_Sales'])
dfDatos = dfDatos.reset_index(drop=True)
print("\n\n\ndataframe dfDatos tras dropna---\n")
print(dfDatos)

#imputaciones
dfDatos['Holiday_Flag'] = dfDatos['Holiday_Flag'].fillna(0)
media_temp = dfDatos['Temperature'].mean()
dfDatos['Temperature'] = dfDatos['Temperature'].fillna(media_temp)
mediana_fuel = dfDatos['Fuel_Price'].median()
dfDatos['Fuel_Price'] = dfDatos['Fuel_Price'].fillna(mediana_fuel)
moda_cpi = dfDatos['CPI'].mode()[0]
dfDatos['CPI'] = dfDatos['CPI'].fillna(moda_cpi)
q1_unemployment = dfDatos['Unemployment'].quantile(0.25)
dfDatos['Unemployment'] = dfDatos['Unemployment'].fillna(q1_unemployment)

print("\nNulos tras imputacion\n")
print(dfDatos.isnull().sum())
print(moda_cpi)
print(mediana_fuel)
print(media_temp)

from sklearn.model_selection import train_test_split
df_X = pd.DataFrame(dfDatos, columns=[
    'Store', 'Date', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 
    'Unemployment', 'Weekly_Rains', 'Weekly_Discounts'
])

df_Y = pd.DataFrame(dfDatos, columns=['Weekly_Sales'])
df_X_train, df_X_test, df_Y_train, df_Y_test = train_test_split(
    df_X, df_Y, test_size=0.2, random_state=100)

print("\nCantidad de filas y columnas de X:\n")
print(df_X.shape)
print(df_Y.shape)

print("\nCantidad de filas y columnas de X_train",df_X_train.shape)
print("Cantidad de filas y columnas de X_test",df_X_test.shape)

print("\nCantidad de filas y columnas de Y_train",df_Y_train.shape)
print("Cantidad de filas y columnas de Y_test",df_Y_test.shape)

print("\nDataframe de df_X:")
print(df_X)
print("\nDataframe de df_X_train:")
print(df_X_train)
print("\nDataframe de df_X_test:")
print(df_X_test)


#---------11/12/25-----------
from sklearn.preprocessing import OrdinalEncoder

df_datos = cargarDatos()
categorias_weekly_rains = [['Ninguna', 'Pocas', 'Medias', 'Muchas']]
#crear codificador
codificador_ordinal = OrdinalEncoder(categories = categorias_weekly_rains)
#ojo doble corchete
codificar_ordinal = codificador_ordinal.fit_transform(df_datos[['Weekly_Rains']])
#convertimos a df
df_nuevas_columnas_ordinal = pd.DataFrame(
    codificador_ordinal,
    columns = ['Weekly_Rains_Cod'],
    index = df_datos.index)

#añadir la columna codificada al df origen
df_datos = df_datos.join(df_nuevas_columnas_ordinal)
print('---df_datos ordinal Encoder---\n')
print(df_datos.head())


from sklearn.preprocessing import OneHotEncoder
import pandas as pd  # Se asume que pd es pandas

# cargamos df original 
df_datos = cargarDatos() 

# Usaremos un DataFrame de ejemplo para que el código sea ejecutable
data = {'Weekly_Discounts': ['carnes', 'pescados', 'carnes', 'restos', 'pescados'],
        'Otra_Columna': [10, 20, 30, 40, 50]}
df_datos = pd.DataFrame(data)


# creamos el objeto OneHotEncoder (convierte texto en column binarias 0/1)
codificador_oneHot = OneHotEncoder(sparse_output=False)

# transformamos column categorica en matriz numerica, ojo doble [[]]
codificar_oneHot = codificador_oneHot.fit_transform(df_datos[['Weekly_Discounts']])

# crear los nombres de las nuevas columnas OneHot
# categories_[0] contiene la lista de valores ['carnes', 'pescados', 'restos']
arr_nombre_nuevas_columnas = 'Weekly_Discounts_' + codificador_oneHot.categories_[0]

# convertimos la codificacion a DF
df_nuevas_columnas_oneHot = pd.DataFrame(
    codificar_oneHot,
    columns=arr_nombre_nuevas_columnas,
    index=df_datos.index
)

# hacemos el join al DF original
df_datos = df_datos.join(df_nuevas_columnas_oneHot)

print("---df_datos OneHotEncoder---")
print(df_datos.head())

# Normalizar con MinMaxScaler (escalado entre 0 y 1)
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt # Esta importación está en la imagen, pero no se usa en el fragmento
import pandas as pd  # Necesario para DataFrame, asumo que es pd

df_datos = cargarDatos() # Esta línea depende de una función no definida aquí

# Usaremos un DataFrame de ejemplo para que el código sea ejecutable
data = {'Fuel_Price': [2.8, 3.5, 4.1, 3.2, 3.9],
        'CPI': [211.0, 212.5, 210.1, 213.0, 211.5]}
df_datos = pd.DataFrame(data)


# seleccionamos solo columnas numericas a normalizar
columnas_a_normalizar = ['Fuel_Price', 'CPI']

# creamos el escalador y lo ajustamos + transformamos
minmax_scaler = MinMaxScaler()
arr_normalizado = minmax_scaler.fit_transform(df_datos[columnas_a_normalizar])

# convertimos de nuevo a DF
df_normalizado = pd.DataFrame(
    arr_normalizado,
    columns=['Fuel_Price_normaliz', 'CPI_normaliz'],
    index=df_datos.index
)

print("---DataFrame Normalizado---")
print(df_normalizado.head())

print('\n' + 'mínimo de Fuel_Price normalizado: \n', df_normalizado['Fuel_Price_normaliz'].min())
print('\n' + 'MAXIMO de CPI normalizado: \n', df_normalizado['CPI_normaliz'].max())

#añadimos las columans al df origen
df_datos = df_datos.join(df_normalizado)
df_datos[['Fuel_Price', 'Fuel_Price_normaliz']].hist(bins=30)
df_datos[['CPI', 'CPI_normaliz']].hist(bins=30)
plt.show()



from sklearn.preprocessing import StandardScaler
#media = 0 y desviacion tipica 1
scaler_std = StandardScaler()

#fir calcula media y desviacion tipica -transform aplica la estandarizacion
arr_estandarizado = scaler_std.fit_transform(df_datos[['Fuel_Price', 'CPI']])
df_estandarizado = pd.DataFrame(
    arr_estandarizado,
    columns = ['Fuel_Price_std', 'CPI_std'],
    index = df_datos.index)
print('MEDIA fuel price estandarizado:   ')
print(df_estandarizado['Fuel_Price_std'].mean())
print('Desviacion tipica fuel price:   ')
print(df_estandarizado['Fuel_Price_std'].std())

df_datos[['Fuel_Price', 'CPI']].hist(bins=30)
plt.suptitle('ORIGINAL')
plt.show()
df_estandarizado[['Fuel_Price_std', 'CPI_std']].hist(bins=30)
plt.suptitle("ESTANDARIZADO")
plt.show()
#%%

import pandas as pd
import random

dfDatos = pd.DataFrame()

#ejrcicio 1 -> 2 columnas
def cargarDatos():
    dfDatos = pd.read_csv(r"C:\Users\Mañana\Documents\santi\walmart.csv")
    
    valores_posibles_customer_flow = ["Bajo", "Medio", "Alto", "Muy_Alto"]
    customer_flow = []
    for i in range(dfDatos.shape[0]):
        customer_flow.append(valores_posibles_customer_flow[random.randint(0,3)])   
    dfDatos['customer_flow'] = customer_flow

    valores_posibles_socio = ["Si", "No"]
    socio = []
    for i in range(dfDatos.shape[0]):
        socio.append(valores_posibles_socio[random.randint(0,1)])
        
    dfDatos['socio'] = socio
    
    return dfDatos

#ejercicio 2
def insertarColumnas():
    # Cargar el DataFrame base con las nuevas columnas categóricas
    df_temp = cargarDatos()
    
    # Filtrar el DataFrame para obtener solo los datos de la 'Store' número 2
    df_store2 = df_temp[df_temp.Store == 2].copy()
    
    print("## 📊 DataFrame de la Tienda 2 (df_store2):")
    print(df_store2)
    print("\n-------------------------------------------")
    return df_store2

#ejecutar
dfDatos = cargarDatos()

print(dfDatos.shape[0])
print("\n\nTipo de datos:")
print(type(dfDatos))
print("\n\nDataframe dfDatos----------:\n")
print(dfDatos)
print("\n\nVer si hay algun null----------:\n")
print(dfDatos.isnull())
print("\n\nLa suma de cuantos null hay----------:\n")
print(dfDatos.isnull().sum())


# Ejecutar el ejercicio 2 y almacenar el resultado
dfDatos_Store2 = insertarColumnas()

# 3. Verifica que tu dataFrame no tiene ningún dato nulo
print("## ✅ Verificación de Datos Nulos:")
print(f"Número de filas y columnas del DataFrame (Filas, Columnas): {dfDatos_Store2.shape}")
print("\nVer si hay algún null:\n")
print(dfDatos_Store2.isnull())
print("\nSuma de null por columna (debe ser 0 para todas):\n")
print(dfDatos_Store2.isnull().sum())


#%%

import pandas as pd
import random
from sklearn.model_selection import train_test_split
 
dfTiendas = pd.DataFrame()
 
def cargarDatos():
    dfTiendas = pd.read_csv(r"C:\Users\Mañana\Documents\santi\walmart.csv")
    dfTiendas = dfTiendas.dropna(subset=['Store', 'Weekly_Sales', 'Fuel_Price'])
    dfTiendas = dfTiendas.reset_index(drop=True)
    return dfTiendas


dfTiendas = cargarDatos()
print(dfTiendas.shape[0])

#-----Ejercicio2-----------------

dfTiendas['Holiday_Flag'] = dfTiendas['Holiday_Flag'].fillna(1)

moda_cpi = dfDatos['CPI'].mode()[0]
dfTiendas['CPI'] = dfTiendas['CPI'].fillna(moda_cpi)

dfDatos['Temperature'] = dfDatos['Temperature'].fillna(min)


#%% practica viii walmart PRUEBA
import pandas as pd
import random
 
dfDatos = pd.DataFrame()
 
def cargarDatos():
    dfDatos = pd.read_csv(r"C:\Users\Mañana\Documents\santi\walmart.csv")
    valoresPosiblesWeeklyRain =["Ninguna","Pocas","Medias","Muchas"]
    weekly_Rains= []
    for i in range(dfDatos.shape[0]):
        weekly_Rains.append(valoresPosiblesWeeklyRain[random.randint(0,3)])
    
    dfDatos['Weekly_Rains'] = weekly_Rains
    
    valoresPosiblesWeeklyDiscounts = ["Carnes","Pescados","Restos"]
    weekly_Discounts = []
    for i in range(dfDatos.shape[0]):
        weekly_Discounts.append(valoresPosiblesWeeklyDiscounts[random.randint(0,2)])
        
    dfDatos["Weekly_Discounts"] = weekly_Discounts
    
    dfDatos = dfDatos[dfDatos.Store == 1]
    return dfDatos
 
 
dfDatos = cargarDatos()
print(dfDatos.shape[0])
print("\n\nTipo de datos:")
print(type(dfDatos))
print("\n\nDataframe dfDatos----------:\n")
print(dfDatos)
print("\n\nVer si hay algun null----------:\n")
print(dfDatos.isnull())
print("\n\nLa suma de cuantos null hay----------:\n")
print(dfDatos.isnull().sum())
 
 
dfDatos = dfDatos.dropna(subset=['Store','Date','Weekly_Sales'])
dfDatos = dfDatos.reset_index(drop=True)
print("\n\n\nDataframe dfDatos tras dropna---\n")
print(dfDatos)
 
#imputaciones
dfDatos['Holiday_Flag'] = dfDatos['Holiday_Flag'].fillna(0)
media_temp = dfDatos['Temperature'].mean()
dfDatos['Temperature'] = dfDatos['Temperature'].fillna(media_temp)
mediana_fuel = dfDatos['Fuel_Price'].median()
dfDatos['Fuel_Price'] = dfDatos['Fuel_Price'].fillna(mediana_fuel)
 
moda_cpi = dfDatos['CPI'].mode()[0]
dfDatos['CPI'] = dfDatos['CPI'].fillna(moda_cpi)
 
q1_unemployment = dfDatos['Unemployment'].quantile(0.25)
dfDatos['Unemployment'] = dfDatos['Unemployment'].fillna(q1_unemployment)
 
print("\nNulos tras imputacion")
print(dfDatos.isnull().sum())
print(moda_cpi)
print(mediana_fuel)
print(media_temp)
 
from sklearn.model_selection import train_test_split
df_X = pd.DataFrame(dfDatos, columns=[
    'Store', 'Date','Holiday_Flag','Temperature','Fuel_Price','CPI',
    'Unemployment','Weekly_Rains','Weekly_Discounts'])
 
df_Y = pd.DataFrame(dfDatos, columns=['Weekly_Sales'])
df_X_train, df_X_test, df_Y_train, df_Y_test = train_test_split(
    df_X, df_Y, test_size=0.2, random_state = 100)
 
print("\nCantidad de filas y columnas de X:\n")
print(df_X.shape)
print(df_Y.shape)
 
print("\nCantidad de filas y columnas de X_train",df_X_train.shape)
print("\nCantidad de filas y columnas de X_test",df_X_test.shape)
 
print("\nCantidad de filas y columnas de Y_test",df_Y_train.shape)
print("\nCantidad de filas y columnas de Y_test",df_Y_test.shape)
 
print("\nDataframe de df_X:")
print(df_X.head())
print("\nDataframe de df_X_train:")
print(df_X_train.head())
print("\nDataframe de df_X_test:")
print(df_X_test.head())
 
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
df_datos = cargarDatos()
categorias_weekly_rains = [['Ninguna','Pocas','Medias','Muchas']]
#crear codificador
codificador_ordinal = OrdinalEncoder(categories = categorias_weekly_rains)
#ojo doble corchete
codificar_ordinal = codificador_ordinal.fit_transform(df_datos[['Weekly_Rains']])
#convertimos a df
df_nuevas_columnas_ordinal = pd.DataFrame(
    codificar_ordinal,
    columns = ['Weekly_Rains_Cod'],
    index = df_datos.index)
 
#añadir la columna codificada al df origen
df_datos = df_datos.join(df_nuevas_columnas_ordinal)
print("---df_datos Ordinal Encoder---")
print(df_datos.head())
 
 
from sklearn.preprocessing import OneHotEncoder
#cargamos df original
df_datos = cargarDatos()
#creamos el objeto OneHotEncoder (convierte texto en column binarias 0/1)
codificador_oneHot = OneHotEncoder(sparse_output = False)
#transformamos column categorica en matriz numerica, ojo doble [[]]
codificar_oneHot = codificador_oneHot.fit_transform(df_datos[['Weekly_Discounts']])
 
#crear los nombres de las nuevas columnas OneHot
#categories_[0] contiene la lista de valores ['carnes','pescados','restos']
arr_nombre_nuevas_columnas = 'Weekly_Discounts_' + codificador_oneHot.categories_[0]
 
#convertimos la codificacion a DF
df_nuevas_columnas_oneHot= pd.DataFrame(
    codificar_oneHot,
    columns= arr_nombre_nuevas_columnas,
    index= df_datos.index)
 
#hacemos el join al DF original
df_datos = df_datos.join(df_nuevas_columnas_oneHot)
print("---df_datos OneHotEncoder--")
print(df_datos.head())
 
 
 
 
# Normalizar con MinMaxScaler (escalado entre 0 y 1)
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
 
df_datos = cargarDatos()
#seleccionamos solo columnas numericas a normalizar
columnas_a_normalizar = ['Fuel_Price','CPI']
#creamos el escalador y lo ajustamos + transformamos
minmax_scaler = MinMaxScaler()
arr_normalizado = minmax_scaler.fit_transform(df_datos[columnas_a_normalizar])
 
#convertimos de nuevo a DF
df_normalizado = pd.DataFrame(
    arr_normalizado,
    columns= ['Fuel_Price_normaliz','CPI_normaliz'],
    index = df_datos.index)
 
print('minimo de Fuel_Price normalizado:\n',df_normalizado['Fuel_Price_normaliz'].min())
print('MAXIMO de CPI normalizado:\n',df_normalizado['CPI_normaliz'].max())
 
#añadimos las columans al df origen
df_datos = df_datos.join(df_normalizado)
df_datos[['Fuel_Price','Fuel_Price_normaliz']].hist(bins=30)
df_datos[['CPI','CPI_normaliz']].hist(bins=30)
plt.show()
 
 
from sklearn.preprocessing import StandardScaler
#media = 0 y desviacion tipica 1
scaler_std = StandardScaler()
 
#fit calcula media y desv tipica - transform aplica estandarizacion
arr_estandarizado = scaler_std.fit_transform(df_datos[['Fuel_Price','CPI']])
df_estandarizado = pd.DataFrame(
    arr_estandarizado,
    columns= ['Fuel_Price_std','CPI_std'],
    index=df_datos.index)
print("MEDIA Fuel_Price estandarizado\n", df_estandarizado['Fuel_Price_std'].mean())
print("Desviacion Tipica fuel price\n", df_estandarizado['Fuel_Price_std'].std())
#
 
df_datos[['Fuel_Price','CPI']].hist(bins=30)
plt.suptitle('ORIGINAL')
plt.show()
df_estandarizado[['Fuel_Price_std','CPI_std']].hist(bins=30)
plt.suptitle("ESTANDARIZADO")
plt.show()


























