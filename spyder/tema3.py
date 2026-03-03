# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 11:06:18 2026

@author: Mañana
"""
import pandas as pd

#%% Ejercicios repaso-ampliacion 1
ruta = r"C:\Users\Mañana\Documents\santi\cotizacion.csv"

# a) Crear la funcion cotizaciones
def cotizaciones(ruta):
    # b) leer el fichero indicando separador (;) , los miles (.) y decimal (,)
    df_inicial = pd.read_csv(ruta, sep=';', thousands='.', decimal=',')
    
    # c) Eliminar la columna 'Nombre'
    df_inicial.drop(columns=['Nombre'], inplace=True)
    '''
    inplace=True
    Qué hace: Modifica el DataFrame original directamente.
    Sin inplace (por defecto): Pandas genera una copia con los cambios y el original queda intacto (requiere reasignar: df = df.operacion()).
    Con inplace=True: No se crea copia, los cambios se aplican sobre la variable actual (no devuelve nada).
    '''
    
    # d) Crear DataFrame usando clave:valor y asignarle columnas 'Minimo','Maximo','Media'
    
    df_final = pd.DataFrame({
        'Minimo': df_inicial.min(),
        'Maximo': df_inicial.max(),
        'Media': df_inicial.mean()
    })

    return df_final
    
    
ruta = r"C:\Users\Mañana\Documents\santi\cotizacion.csv"

# e) Retornar el dataframe creado e imprimirlo desde fuera de la función
try:
    resultado = cotizaciones(ruta)
    print("DataFrame generado con éxito:")
    print(resultado)
except FileNotFoundError:
    print("Error: No se encontró el archivo en la ruta especificada.")


#%% priemra parte titanic

ruta = r"C:\Users\Mañana\Documents\santi\titanic.csv"

def titanic(ruta):
    # a) Genera un dataframe con los datos de titanic.csv
    df = pd.read_csv(ruta, sep=',')
    
    # b) Imprima dimensiones, tamaño, indice y las 10 ultimas lineas del dataframe
    print(f"Dimensiones (filas, columnas): {df.shape}")
    print(f"Tamaño total (nº de elementos): {df.size}")
    print(f"Índice del dataframe: {df.index}")
    print("\n--- Las 10 últimas líneas ---")
    print(df.tail(10))
    
    # c) Datos del pasajero con identificador 148 con loc[] (ojo indexacion desde cero)
    pasajero_148 = df.loc[148]
    print("\n--- Datos del pasajero con identificador 148 ---")
    print(pasajero_148)
    
    # d) Mostrar por pantalla las filas pares usando iloc[range(...)]
    filas_pares = df.iloc[range(0, len(df), 2)]
    print("\n--- Filas pares del DataFrame ---")
    print(filas_pares)
    
    # e) Nombres de personas de primera clase 'Pclass==1' ordenadas alfabeticamente
    nombres_clase_1 = df[df['Pclass'] == 1]['Name'].sort_values()
    print("\n--- Nombres de pasajeros de primera clase (ordenados) ---")
    print(nombres_clase_1)


try:
    resultado = titanic(ruta)
    print("DataFrame generado con éxito:")
except FileNotFoundError:
    print("Error: No se encontró el archivo en la ruta especificada.")


#%% segunda parte titanic

'''
3 Continuando con el archivo csv de titanic, investiga cómo usar los métodos:
a) Imprimir porcentaje de supervivientes con .value_counts(normalize=True)*100
b) Porcentaje de supervivientes de cada clase, usando .groupby('Pclass')['Survived']
c) Eliminar los pasajeros con edad desconocida con dropna()
d) Edad media (mean) de las mujeres que viajaban de cada clase, ['Sex']=='female'....
e) Añadir columna booleana 'Young' para ver si pasajero era menor de edad
f) Mostrar todas las columnas del dataframe usando pd.set_option(...)'''
    
#%% Emisiones

'''
4 Los ficheros emisiones-201X.csv contienen datos sobre las emisiones contaminantes ('MAGNITUD') en la ciudad de Madrid.
a) Generar el DataFrame 'emisiones' con los datos de los 4 ficheros conjuntos usando .concat
b) Filtrar las columnas para quedarse con Estacion, Magnitud, Año y Mes de los dias D01, D02, etc
c) Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los dias aparezcan en una única columna usando .melt(id_vars=[...]))
d) (import datetime) Crear columna FECHA con la concatenación del año, mes, día. (usar método emisiones.DIA.str.strip() y emisiones.ANO.astype(str)))
e) Eliminar filas con fechas no validas usando numpy.isnat(...)
    '''
    
import pandas as pd
import numpy as np
import datetime

print("Parte 1")

ruta = r'C:\Users\Mañana\Downloads'


ficheros = [
    ruta + r'\emisiones2016.csv',
    ruta + r'\emisiones2017.csv',
    ruta + r'\emisiones2018.csv',
    ruta + r'\emisiones2019.csv'
]

# a) Generar el DataFrame 'emisiones' con los datos de los 4 ficheros conjuntos usando .concat
emisiones = pd.concat([pd.read_csv(f, sep=';') for f in ficheros])

# b) Filtrar las columnas para quedarse con Estacion, Magnitud, Año y Mes de los dias D01, D02, etc
columnas_dias = [col for col in emisiones.columns if col.startswith('D') and len(col) == 3]
emisiones = emisiones[['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + columnas_dias]

# c) c) Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los dias aparezcan en una única columna usando .melt(id_vars=[...]))
emisiones = emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], 
                           var_name='DIA', 
                           value_name='VALOR')

# d) (import datetime) Crear columna FECHA con la concatenación del año, mes, día. (usar método emisiones.DIA.str.strip() y emisiones.ANO.astype(str)))
# Usamos strip() para quitar la 'D' y astype(str) para el año
emisiones['DIA'] = emisiones['DIA'].str.strip('D')
emisiones['FECHA'] = pd.to_datetime(
    emisiones['ANO'].astype(str) + '/' + 
    emisiones['MES'].astype(str) + '/' + 
    emisiones['DIA'], 
    format='%Y/%m/%d', 
    errors='coerce'
)

# e) Eliminar filas con fechas no validas usando numpy.isnat(...)
emisiones = emisiones[~np.isnat(emisiones['FECHA'])]

print(emisiones.head())
     
    
# Emisiones Continuacion

'''
5 Continuar con el ejercicio anterior para los siguientes apartados:
f) ordenar las columnas en este orden Estacion, Magnitud, Fecha
g) Función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
h) Mostrar un resumen descriptivo (min, MAX, media) para cada contaminante usando .groupby(...).VALOR.describe()
i) Mostrar resumen descriptivo para cada contaminante por distritos ampliando el código del apartado anterior
j) Función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
k) Función que devuelva emisiones medias mensuales de un contaminante y un año dados para todas las estaciones
l) Función que reciba estación y devuelva DataFrame con medias mensuales de los tipos de contaminantes
    '''
print("Parte 2")
    
print("EMISIONES=======================")
print(emisiones)
# f) Ordenar las columnas en el orden: Estacion, Magnitud, Fecha
emisiones = emisiones[['ESTACION', 'MAGNITUD', 'FECHA', 'VALOR']]
emisiones = emisiones.sort_values(by=['ESTACION', 'MAGNITUD', 'FECHA'])

# g) Función que devuelve emisiones filtradas por estación, contaminante y rango de fechas
def filtrar_emisiones(estacion, contaminante, fecha_inicio, fecha_fin):
    # Convertimos las fechas de entrada a datetime por seguridad
    inicio = pd.to_datetime(fecha_inicio)
    fin = pd.to_datetime(fecha_fin)
    
    # Filtramos el DataFrame
    filtro = (emisiones['ESTACION'] == estacion) & \
             (emisiones['MAGNITUD'] == contaminante) & \
             (emisiones['FECHA'] >= inicio) & \
             (emisiones['FECHA'] <= fin)
    
    # Devolvemos una Serie con el VALOR y la FECHA como índice
    resultado = emisiones[filtro].set_index('FECHA')['VALOR']
    return resultado

# h) Resumen descriptivo (min, MAX, media) para cada contaminante
resumen_contaminantes = emisiones.groupby('MAGNITUD').VALOR.describe()[['min', 'max', 'mean']]
print("Resumen por contaminante:\n", resumen_contaminantes)

# i) Resumen descriptivo por contaminante y estación (distrito)
resumen_distritos = emisiones.groupby(['MAGNITUD', 'ESTACION']).VALOR.describe()
print("\nResumen por contaminante y estación:\n", resumen_distritos)

# j) Función que devuelve resumen descriptivo de un contaminante y estación dados
def resumen_especifico(estacion, contaminante):
    filtro = (emisiones['ESTACION'] == estacion) & (emisiones['MAGNITUD'] == contaminante)
    return emisiones[filtro].VALOR.describe()[['min', 'max', 'mean']]

# k) Función: emisiones medias mensuales de un contaminante y año para todas las estaciones
def media_mensual_año(contaminante, año):
    # Extraemos el mes de la fecha para agrupar
    filtro_año_mag = emisiones[(emisiones['MAGNITUD'] == contaminante) & 
                               (emisiones['FECHA'].dt.year == año)]
    
    # Agrupamos por el mes de la FECHA
    resultado = filtro_año_mag.groupby(filtro_año_mag['FECHA'].dt.month).VALOR.mean()
    resultado.index.name = 'MES'
    return resultado

# l) Función: medias mensuales de todos los contaminantes para una estación dada
def medias_por_estacion(estacion):
    filtro_estacion = emisiones[emisiones['ESTACION'] == estacion].copy()
    
    # Añadimos columna de mes para agrupar fácilmente
    filtro_estacion['MES'] = filtro_estacion['FECHA'].dt.month
    
    # Creamos una tabla dinámica (pivot table) para ver contaminantes vs meses
    tabla_medias = filtro_estacion.groupby(['MAGNITUD', 'MES']).VALOR.mean().unstack()
    return tabla_medias

# --- EJEMPLOS DE USO ---
print("\nEjemplo Función G (Serie temporal):")
print(filtrar_emisiones(4, 1, '2016-01-01', '2016-01-05'))

print("\nEjemplo Función K (Media mensual CO - Mag 1 en 2016):")
print(media_mensual_año(1, 2016))
    
    
#%% ud3 Teoria ejemplo regresion lineal multiple pag 4
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
# Aplica regresión lineal sobre el dataset Diabetes de sklearn, seleccionando una
# única característica como variable independiente. Divide los datos en entrenamiento
# y test, entrena el modelo, evalúa el error mediante Mean Squared Error (MSE) y
# compara gráficamente los resultados en ambos conjuntos.
#carga de los datos
diabetes = datasets.load_diabetes()
#seleccion de la variable dependiente y de las independientes
y=diabetes.target
X=diabetes.data[:,np.newaxis,2]
print(diabetes.data.shape)
print(diabetes.data[:,2].shape)
#division en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=10)
#generación del método y entrenamiento
linear_regression = linear_model. LinearRegression()
linear_regression.fit(X_train,y_train)
#calculo de valores predichos
y_train_predicted = linear_regression.predict (X_train)
y_test_predicted = linear_regression.predict(X_test)
#calculo de las diferencias entre predicho y real
train_MSD = mean_squared_error(y_train,y_train_predicted)
test_MSD = mean_squared_error(y_test,y_test_predicted)
#graficacion de las curvas predichas y de las reales
fig, axs = plt.subplots(1,2, figsize=(15,4))
axs[0].scatter(X_train, y_train, color='orange')
axs[0].plot(X_train, y_train_predicted, color= 'black')
axs[0].set_title('training set, MSD:{:.0f}'.format(train_MSD))
axs[1].scatter(X_test, y_test, color='gray')
axs[1].plot(X_test, y_test_predicted, color='black')
axs[1].set_title('testing set, MSD:{:.0f}'.format(test_MSD))
plt.show()
'''
diabetes.data[:, np.newaxis, 2]:
    2 selecciona una característica concreta.
    np.newaxis convierte el vector en matriz columna (2D), obligatorio para sklearn.
train_test_split separa datos para evaluar generalización del modelo.
mean_squared_error mide el error cuadrático medio entre valores reales y predichos.
plt.subplots(1,2) permite comparar entrenamiento vs test en una sola figura.
'''


#%%
'''
26 Desarrolla un modelo de regresión lineal múltiple para predecir el precio de las casas en California de acuerdo con el 
número de habitaciones que tiene la vivienda, el tiempo que ha estado ocupada y la distancia a los centros de trabajo de
 California. Estas son varias características que se tomarán en cuenta para diseñar nuestro modelo. 
 Para ello, utiliza el conjunto de datos fetch_california_housing() de los datasets de scikit-learn.

En este ejercicio vas a construir un modelo de regresión lineal para predecir el precio medio de viviendas en 
California utilizando el dataset California Housing disponible en sklearn. 

Sigue los siguientes pasos:

a)	 Importa las librerías necesarias:
•	pandas
•	fetch_california_housing desde sklearn.datasets
•	train_test_split desde sklearn.model_selection
•	LinearRegression desde sklearn.linear_model
•	mean_squared_error y r2_score desde sklearn.metrics
•	StandardScaler desde sklearn.preprocessing

b)	Carga el dataset California Housing.
 
c)	Crea un DataFrame de pandas con las variables predictoras y añade una nueva columna llamada PRICE que contenga 
    la variable objetivo (usando el atributo .target de los datos cargados)
 
d)	Crea un array 'caracteristicas' con las variables independientes: 
    MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude.
 
e)	Separa el conjunto de datos en Variables predictoras (X) con las caracteristicas del dataframe y Variable objetivo (y) 
    con la columna de PRICE
 
f)	Divide los datos en conjunto de entrenamiento y prueba: 80% entrenamiento, 20% prueba y usa random_state=42
'''
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
 
#b)	Carga el dataset California Housing.
california = fetch_california_housing()

#c)	Crea un DataFrame de pandas con las variables predictoras y añade una nueva columna llamada PRICE que contenga 
#la variable objetivo (usando el atributo .target de los datos cargados)
df = pd.DataFrame(california.data, columns=california.feature_names)
df['PRICE'] = california.target

#d)	Crea un array 'caracteristicas' con las variables independientes: 
#MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude.
caracteristicas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

#e)	Separa el conjunto de datos en Variables predictoras (X) con las caracteristicas del dataframe y 
# Variable objetivo (y) con la columna de PRICE
X = df[caracteristicas]
y = df['PRICE']
 
#f)	Divide los datos en conjunto de entrenamiento y prueba: 80% 
#entrenamiento, 20% prueba y usa random_state=42''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

'''
Probar
'''
# 1. Crear la instancia del modelo
modelo = LinearRegression()
# 2. Entrenar (el modelo aprende la relación entre X_train e y_train)
modelo.fit(X_train, y_train)
# 3. Predecir (el modelo hace el examen usando solo las preguntas X_test)
predicciones = modelo.predict(X_test)

# Comparamos las predicciones con los precios reales (y_test)
mse = mean_squared_error(y_test, predicciones)
r2 = r2_score(y_test, predicciones)

print(f"Error Cuadrático Medio (MSE): {mse:.4f}")
print(f"Coeficiente de determinación (R2): {r2:.4f}")

#grafico
import matplotlib.pyplot as plt
plt.scatter(y_test, predicciones, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Precio Real')
plt.ylabel('Precio Predicho')
plt.title('Comparación: Real vs Predicción')
plt.show()

'''
g)	Aplica una normalización (escalado) de los datos utilizando StandardScaler: 
    Ajusta el escalador con los datos de entrenamiento. Transforma tanto los datos de entrenamiento como los de prueba.

h)	Crea la variable modelo, instancia de LinearRegression() y usa su método fit() pasándole como parametros 
    el X_train escalado y el y_train.

i)	Crea la variable ‘prediccionConjuntoPrueba’ y realiza predicciones sobre el conjunto de prueba con 
    el método .predict() usando de parametro el X_test escalado

j)	Calcula Error Cuadrático Medio (MSE) en una variable usando mean_squared_error(), con parametros y_test 
    y la prediccion del conjunto de prueba. Muéstralo por pantalla

k)	Calcula el Coeficiente de Determinación (R²) en una variable usando r2_score(), con parametros y_test y 
    la prediccion del conjunto de prueba. Muéstralo por pantalla.
    
l)	Muestra por pantalla todos los valores (MedInc, HouseAge, AveRooms,etc) a los que se pueden acceder mediante 
    el método modelo.coef_
'''

# g) Normalización con StandardScaler
scaler = StandardScaler()
#Ajustamos con el entrenamiento (aprende la media y desviación) y transformamos ambos
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# h) Crear instancia de LinearRegression y entrenar (fit)
modelo = LinearRegression()
modelo.fit(X_train_scaled, y_train)

# i) Realizar predicciones sobre el conjunto de prueba escalado
prediccionConjuntoPrueba = modelo.predict(X_test_scaled)

# j) Calcular y mostrar el Error Cuadrático Medio (MSE)
mse = mean_squared_error(y_test, prediccionConjuntoPrueba)
print(f"Error Cuadrático Medio (MSE): {mse:.4f}")

# k) Calcular y mostrar el Coeficiente de Determinación (R²)
r2 = r2_score(y_test, prediccionConjuntoPrueba)
print(f"Coeficiente de Determinación (R²): {r2:.4f}")

# l) Mostrar los coeficientes del modelo para cada característica
print("\nCoeficientes del modelo (importancia de cada variable):")
for nombre, coef in zip(caracteristicas, modelo.coef_):
    print(f"{nombre}: {coef:.4f}")

#%% EJERCICIO 27
'''
27 Desarrolla un modelo de clasificación mediante Regresión Logística para predecir la especie de flor Iris utilizando únicamente el largo y el ancho del sépalo.
En este ejercicio vas a construir un modelo de clasificación supervisada usando el dataset load_iris() de scikit-learn. El objetivo es entrenar un modelo de Regresión Logística, evaluarlo con métricas de clasificación y visualizar su frontera de decisión.
 
a) Importa las siguientes librerías:
• numpy como np
• pandas como pd
• load_iris desde sklearn.datasets
• train_test_split desde sklearn.model_selection
• LogisticRegression desde sklearn.linear_model
• StandardScaler desde sklearn.preprocessing
• accuracy_score, classification_report y confusion_matrix desde sklearn.metrics
• matplotlib.pyplot como plt
 
b) Carga el dataset Iris en una variable llamada datosIris utilizando:
datosIris = load_iris()
 
c) Crea un DataFrame llamado dfIris con:
• Las variables predictoras usando datosIris.data
• Los nombres de columnas usando datosIris.feature_names
Añade una nueva columna llamada target usando: dfIris['target'] = datosIris.target
 
d) Crea un array llamado caracteristicas con las siguientes variables independientes:  'sepal length (cm)' y  'sepal width (cm)'
 
e) Separa el conjunto de datos en: variable X con dfIris[caracteristicas] y variable y con dfIris['target']
 
f) Divide los datos en conjunto de entrenamiento y prueba utilizando: train_test_split(X, y, test_size=0.2, random_state=42)
    '''
# a) Importar librerías
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
 
# b) Cargar dataset
datosIris = load_iris()
 
# c) Crear DataFrame
dfIris = pd.DataFrame(datosIris.data, columns=datosIris.feature_names)
dfIris['target'] = datosIris.target
 
# d) Seleccionar características
caracteristicas = ['sepal length (cm)', 'sepal width (cm)']
 
# e) Separar X e y
X = dfIris[caracteristicas]
y = dfIris['target']
 
# f) Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

'''
g) Aplica una normalización utilizando StandardScaler:
    • Crea una instancia llamada scaler
    • Ajusta y transforma los datos de entrenamiento con: escalaAjusteEntrenamiento = scaler.fit_transform(X_train)
    • Transforma los datos de prueba con: escalaAjustePrueba = scaler.transform(X_test)

h) Crea la variable ‘modelo’ como una instancia de LogisticRegression() y entrena modelo usando 
    modelo.fit(escalaAjusteEntrenamiento, y_train)

i) Realiza las predicciones sobre el conjunto de prueba utilizando: predicionesPrueba = modelo.predict(escalaAjustePrueba)

j) Evalúa la precisión del modelo calculando la variable accuracy usando: accuracy_score(y_test, predicionesPrueba) y 
    mostrándola por pantalla.

k) Genera y muestra el informe de clasificación usando: classification_report(y_test, predicionesPrueba) y la 
    matriz de confusión almacenándola en una variable llamada matrizConfusion usando: confusion_matrix(y_test, predicionesPrueba)

l) Visualización de la frontera de decisión (solo si el número de características es 2):
    • Crea una malla de puntos usando este código:
        x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
        y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
    • Predice las clases sobre la malla con este código
        Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
m)  Usa plt.contourf() para dibujar la superficie, plt.scatter() para representar los puntos de entrenamiento y añade
    etiquetas a los ejes y un título con plt.xlabel() y plt.title()
    '''
# g) Normalización
scaler = StandardScaler()
escalaAjusteEntrenamiento = scaler.fit_transform(X_train)
escalaAjustePrueba = scaler.transform(X_test)
 
# h) Crear y entrenar modelo
modelo = LogisticRegression()
modelo.fit(escalaAjusteEntrenamiento, y_train)
 
# i) Predicciones
predicionesPrueba = modelo.predict(escalaAjustePrueba)
 
# j) Accuracy
accuracy = accuracy_score(y_test, predicionesPrueba)
print(f"Accuracy: {accuracy:.4f}")
 
# k) Reporte y matriz de confusión
print("\nClassification Report:\n")
print(classification_report(y_test, predicionesPrueba))
 
matrizConfusion = confusion_matrix(y_test, predicionesPrueba)
print("Matriz de Confusión:\n")
print(matrizConfusion)
 
# l) Visualización frontera de decisión
 
# Escalamos TODOS los datos para visualizar
X_scaled = scaler.transform(X)
 
x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
 
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)
 
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
 
# m) Dibujar superficie y puntos
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(
    escalaAjusteEntrenamiento[:, 0],
    escalaAjusteEntrenamiento[:, 1],
    c=y_train,
    edgecolor='k'
)
 
plt.xlabel('Sepal length (scaled)')
plt.ylabel('Sepal width (scaled)')
plt.title('Frontera de decisión - Regresión Logística (Iris)')
plt.show()
 
#%% EJERCICIO 28
'''
28 Evalúa un modelo de Regresión Logística mediante validación cruzada para clasificar las especies Iris utilizando el largo y 
el ancho del sépalo.
En este ejercicio vas a construir un modelo de clasificación supervisada utilizando el dataset load_iris() de scikit-learn. 
A diferencia del ejercicio anterior, no realizarás una única división en entrenamiento y prueba, sino que evaluarás el modelo 
mediante validación cruzada con 5 pliegues para obtener una estimación más robusta de su rendimiento. 
Posteriormente, entrenarás el modelo con todos los datos para visualizar la frontera de decisión.

a) Importa las siguientes librerías:
• numpy como np
• pandas como pd
• matplotlib.pyplot como plt
• load_iris desde sklearn.datasets
• cross_val_score desde sklearn.model_selection
• LogisticRegression desde sklearn.linear_model
• StandardScaler desde sklearn.preprocessing

b) Carga el dataset Iris en una variable llamada datosIris utilizando datosIris = load_iris()
    
c) Crea un DataFrame llamado dfIris con las variables predictoras usando datosIris.data y los nombres de columnas usando 
    datosIris.feature_names.  Después añade una nueva columna llamada target usando dfIris['target'] = datosIris.target
    
d) Crea un array llamado caracteristicas con las siguientes variables independientes: 'sepal length (cm)' y 'sepal width (cm)'
    
e) Separa el conjunto de datos en variable X con dfIris[caracteristicas] y variable y con dfIris['target']
    
f) Aplica una normalización utilizando StandardScaler. Crea una instancia llamada scaler, ajusta y transforma todos los datos 
    utilizando: X_scaled = scaler.fit_transform(X)
g) Crea la variable modelo como una instancia de LogisticRegression().
'''
# a) Importar librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
 
# b) Cargar dataset
datosIris = load_iris()
 
# c) Crear DataFrame
dfIris = pd.DataFrame(datosIris.data, columns=datosIris.feature_names)
dfIris['target'] = datosIris.target
 
# d) Seleccionar características
caracteristicas = ['sepal length (cm)', 'sepal width (cm)']
 
# e) Separar X e y
X = dfIris[caracteristicas]
y = dfIris['target']
 
# f) Normalización (todos los datos)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
 
# g) Crear modelo
modelo = LogisticRegression()

'''
h) Realiza una validación cruzada con 5 pliegues utilizando 
    cv_accuracy = cross_val_score(modelo, X_scaled, y, cv=5, scoring='accuracy')
    Muestra por pantalla: El vector de precisiones obtenido en cada pliegue y la precisión media calculada mediante 
    np.mean(cv_accuracy)
    
i) Entrena el modelo con todos los datos escalados utilizando modelo.fit(X_scaled, y)
    
j) Visualización de la frontera de decisión:
    • Calcula los valores mínimos y máximos de cada característica usando X_scaled[:, 0] y X_scaled[:, 1]
    • Crea una malla de puntos usando np.meshgrid()
    • Predice las clases sobre la malla utilizando:
        Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
k) Representa gráficamente:
    • La superficie de decisión usando plt.contourf()
    • Los puntos reales del dataset usando plt.scatter()
    • Añade etiquetas a los ejes con plt.xlabel() y plt.ylabel()
    • Añade un título con plt.title()
    • Muestra la figura con plt.show()
'''
 
# h) Validación cruzada (5 pliegues)
cv_accuracy = cross_val_score(
    modelo,
    X_scaled,
    y,
    cv=5,
    scoring='accuracy'
)
 
print("Precisión en cada pliegue:", cv_accuracy)
print("Precisión media:", np.mean(cv_accuracy))
 
# i) Entrenar modelo con todos los datos
modelo.fit(X_scaled, y)
 
# j) Crear malla para frontera de decisión
x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
 
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)
 
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# k) Representación gráfica
plt.contourf(xx, yy, Z, alpha=0.3)
 
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=y,
    edgecolor='k'
)
 
plt.xlabel('Sepal length (scaled)')
plt.ylabel('Sepal width (scaled)')
plt.title('Frontera de decisión - Regresión Logística (Iris)')
plt.show()
 
 
#%% EJERCICIO 29
'''
29 Clasificación de tumores de cáncer de mama utilizando Regresión Logística con todas las características
En este ejercicio vas a construir un modelo de clasificación binaria para predecir si un tumor de mama es benigno o 
maligno utilizando todas las características disponibles en el dataset de cáncer de mama de scikit-learn. 

Dividirás los datos en conjuntos de entrenamiento y prueba, estandarizarás las características para mejorar el rendimiento 
del modelo, y evaluarás la calidad del clasificador mediante múltiples métricas incluyendo accuracy, precision, sensibilidad, 
F1-score y la matriz de confusión.

a) Importa las bibliotecas necesarias: pandas como pd, load_breast_cancer desde sklearn.datasets, train_test_split desde 
    sklearn.model_selection, LogisticRegression desde sklearn.linear_model, StandardScaler desde sklearn.preprocessing, 
    y las métricas confusion_matrix, accuracy_score, precision_score, recall_score y f1_score desde sklearn.metrics.
    
b) Carga el conjunto de datos de cáncer de mama en una variable llamada datosCancer utilizando load_breast_cancer(). 
    Este dataset contiene mediciones de características de núcleos celulares presentes en imágenes de biopsias de mama.
c) Crea un DataFrame llamado dfCancer con todas las características utilizando datosCancer.data como datos y 
    datosCancer.feature_names como nombres de columnas. Añade una nueva columna llamada 'target' al DataFrame asignándole 
    los valores de datosCancer.target, donde 0 representa tumores malignos y 1 representa tumores benignos.
    
d) Análisis del dataset
    •	Muestra por pantalla los nombres de todas las características del dataset usando datosCancer.feature_names. 
        ¿Cuántas características tiene el dataset?
    •	Muestra los nombres de las clases objetivo con datosCancer.target_names. 
        ¿Qué valor numérico corresponde a cada clase según lo que viste en el enunciado?
    •	Muestra las primeras 5 filas del dataset en formato array con datosCancer.data[:5] para hacerte una idea de los valores 
        numéricos que contiene.
    •	Una vez creado el DataFrame dfCancer (apartado c), muestra sus primeras filas con .head() y consulta su estructura 
        con .info() o .describe(). ¿Qué tipo de datos contiene? ¿Hay valores nulos?
    •	Muestra cuántos tumores malignos (0) y cuántos benignos (1) hay en el dataset usando .value_counts() sobre la columna target. 
        ¿Está el dataset balanceado?
 
e) Selecciona las variables predictoras creando la variable X que contenga todas las características del dataset usando dfCancer[datosCancer.feature_names]. Crea la variable y que contenga la columna objetivo con dfCancer['target'], representando la clasificación benigno/maligno del tumor.
'''
# a) Importar librerías
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
)
 
# b) Cargar dataset
datosCancer = load_breast_cancer()
 
# c) Crear DataFrame con todas las características y la columna target
dfCancer = pd.DataFrame(datosCancer.data, columns=datosCancer.feature_names)
dfCancer['target'] = datosCancer.target  
 
# d) Análisis del dataset
 
# d1) Nombres de las características y cantidad
print("d1) Características del dataset:\n", datosCancer.feature_names)
print("d1) Número de características:", len(datosCancer.feature_names))
 
# d2) Nombres de las clases objetivo y valores numéricos
print("\nd2) Clases objetivo:", datosCancer.target_names)
print("d2) Valores numéricos: 0 = maligno, 1 = benigno")
 
# d3) Primeras 5 filas en formato array
print("\nd3) Primeras 5 filas (array):\n", datosCancer.data[:5])
 
# d4) Primeras filas del DataFrame y estructura
print("\nd4) Primeras filas del DataFrame:\n", dfCancer.head())
print("\nd4) Información del DataFrame:\n")
print(dfCancer.info())
print("\nd4) Estadísticas descriptivas:\n", dfCancer.describe())
 
# d5) Conteo de tumores por clase
print("\nd5) Conteo de tumores por clase:\n", dfCancer['target'].value_counts())
 
# e) Selección de variables predictoras
X = dfCancer[datosCancer.feature_names].values
y = dfCancer['target'].values
 
print("\ne) Tamaño de X:", X.shape)
print("e) Tamaño de y:", y.shape)

'''
f) Divide el conjunto de datos en entrenamiento y prueba utilizando train_test_split() con X, y como entrada y los parámetros 
    test_size=0.2 y random_state=42.
    
g) Estandariza los datos creando una instancia de StandardScaler() llamada scaler. Ajusta el escalador con los datos de 
    entrenamiento y transfórmalos guardando el resultado en X_train_scaled usando scaler.fit_transform(X_train). 
    Transforma el conjunto de prueba guardando el resultado en X_test_scaled usando scaler.transform(X_test). 
    La estandarización es crucial en regresión logística para que todas las características contribuyan equitativamente al modelo.
    
h) Crea el modelo de Regresión Logística en una variable llamada modelo utilizando LogisticRegression(). 
    Entrena el modelo con los datos de entrenamiento estandarizados usando modelo.fit(X_train_scaled, y_train).
    
i) Realiza predicciones sobre el conjunto de prueba utilizando modelo.predict(X_test_scaled) y guarda el resultado en la 
    variable y_pred.
    
j) Evalúa la calidad del modelo calculando múltiples métricas de clasificación. Calcula el accuracy usando 
    accuracy_score(y_test, y_pred), la precision usando precision_score(y_test, y_pred), la sensibilidad (recall) 
    usando recall_score(y_test, y_pred), y el F1-score usando f1_score(y_test, y_pred). 
    Calcula también la matriz de confusión usando confusion_matrix(y_test, y_pred) y guárdala en confusionMatrix.
    
k) Muestra por pantalla todas las métricas calculadas: accuracy, precision, sensibilidad y F1-score con sus respectivas etiquetas. 
    Finalmente, muestra la matriz de confusión con un encabezado descriptivo que indique claramente qué métrica se 
    está presentando.
'''

# f) Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
# g) Estandarización de los datos
scaler = StandardScaler()
 
# Ajustamos y transformamos los datos de entrenamiento
X_train_scaled = scaler.fit_transform(X_train)
 
# Transformamos los datos de prueba
X_test_scaled = scaler.transform(X_test)
 
# h) Crear y entrenar el modelo de Regresión Logística
modelo = LogisticRegression()
modelo.fit(X_train_scaled, y_train)
 
# i) Predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test_scaled)
 
# j) Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)  # sensibilidad
f1 = f1_score(y_test, y_pred)
confusionMatrix = confusion_matrix(y_test, y_pred)
 
# k) Mostrar métricas y matriz de confusión
print(f"k) Accuracy: {accuracy:.4f}")
print(f"k) Precision: {precision:.4f}")
print(f"k) Sensibilidad (Recall): {recall:.4f}")
print(f"k) F1-score: {f1:.4f}")
 
print("\nk) Matriz de Confusión:\n", confusionMatrix)

#%% EJERCICIO 30

'''
30 En este ejercicio vas a construir un modelo de clasificación supervisada utilizando el dataset de cáncer de mama de scikit-learn. 
A diferencia de realizar una única división en entrenamiento y prueba, evaluarás el modelo mediante validación 
cruzada con 5 pliegues para obtener una estimación más robusta de su rendimiento utilizando únicamente dos características 
del dataset.

a) Importa las bibliotecas necesarias: numpy como np, pandas como pd, load_breast_cancer desde sklearn.datasets, 
    cross_val_score desde sklearn.model_selection, SVC desde sklearn.svm y StandardScaler desde sklearn.preprocessing.
b) Carga el dataset de cáncer de mama en una variable llamada datosCancer utilizando load_breast_cancer(). 
    
    A continuación, crea un DataFrame llamado dfCancer con las variables predictoras usando datosCancer.data y 
    los nombres de columnas usando datosCancer.feature_names. Después añade una nueva columna llamada 'target' con los 
    valores de datosCancer.target.
c) Crea un array llamado caracteristicas que contenga las siguientes dos variables independientes: 
    'mean radius' y 'mean texture'. Estas serán las únicas características que utilizarás para entrenar el modelo.
'''
# a) Importar librerías
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
 
# b) Cargar dataset y crear DataFrame
datosCancer = load_breast_cancer()
 
dfCancer = pd.DataFrame(
    datosCancer.data,
    columns=datosCancer.feature_names
)
 
dfCancer['target'] = datosCancer.target  
# 0 = maligno, 1 = benigno
 
# c) Seleccionar únicamente dos características
caracteristicas = ['mean radius', 'mean texture']
 
# d) Separar variables predictoras (X) y variable objetivo (y)
X = dfCancer[caracteristicas]
y = dfCancer['target']
 
print("d) Tamaño de X:", X.shape)
print("d) Tamaño de y:", y.shape)
 
# e) Normalización de los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
 
# f) Crear modelo SVC (kernel por defecto = rbf)
modelo = SVC()
 
# g) Validación cruzada con 5 pliegues
accuracyModelo = cross_val_score(
    modelo,
    X_scaled,
    y,
    cv=5,
    scoring='accuracy'
)
 
# h) Mostrar precisión en cada pliegue
print("\nh) Precisión en cada pliegue:")
 
for i, precision in enumerate(accuracyModelo, start=1):
    print(f"   Pliegue {i}: {precision:.4f}")
 
print(f"\n   Precisión media: {np.mean(accuracyModelo):.4f}")
 
#%%

'''
32 Clasificación de valoraciones de reseñas utilizando K-Nearest Neighbors (KNN)
En este ejercicio vas a construir un modelo de clasificación supervisada para predecir la puntuación en estrellas (Star Rating) 
de reseñas basándote en características textuales como el número de palabras y el valor de sentimiento. 
Utilizarás el algoritmo K-Nearest Neighbors (KNN), dividirás los datos en conjuntos de entrenamiento y prueba, normalizarás 
las características y evaluarás el rendimiento del modelo mediante diferentes métricas de clasificación.

a) Importa las bibliotecas necesarias: pandas como pd, train_test_split desde sklearn.model_selection, StandardScaler 
    desde sklearn.preprocessing, KNeighborsClassifier desde sklearn.neighbors, y las métricas accuracy_score, 
    classification_report y confusion_matrix desde sklearn.metrics.
b) Carga el archivo CSV llamado 'reviews_sentiment.csv' en un DataFrame llamado df utilizando pd.read_csv() con los 
    parámetros delimiter=';' y encoding='utf-8'. Este dataset contiene información sobre reseñas de productos incluyendo 
    el número de palabras, el valor de sentimiento y la puntuación en estrellas.
    
c) Selecciona las columnas que servirán como características predictoras creando la variable features que contenga las 
    columnas 'wordcount' y 'sentimentValue' del DataFrame. Luego crea la variable target que contenga la columna 'Star Rating', 
    que representa la puntuación que se quiere predecir.
d) Divide el conjunto de datos en conjuntos de entrenamiento y prueba utilizando train_test_split() con features y target 
    como entrada, y los parámetros test_size=0.2 y random_state=42.
'''

# a) Importar bibliotecas necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
 
 
# b) Cargar el CSV
ruta = r"C:\Users\Mañana\OneDrive - Consejería de Educación\Documentos\santi\"
df = pd.read_csv(r'C:\Users\Mañana\OneDrive - Consejería de Educación\Documentos\santi\', delimiter=';', encoding='utf-8')
 
 
# c) Seleccionar características y variable objetivo
features = df[['wordcount', 'sentimentValue']]
target = df['Star Rating']
 
 
# d) Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

'''
e) Normaliza los datos creando una instancia de StandardScaler() llamada scaler. 
    Ajusta el escalador con los datos de entrenamiento y transfórmalos guardando el resultado en escalarAjustarEntrenamiento 
    mediante scaler.fit_transform(X_train). A continuación, transforma el conjunto de prueba guardando el resultado en 
    escalarAjustarPrueba usando el método .transform(X_test).
    
f) Crea el modelo K-Nearest Neighbors en una variable llamada modeloKnn utilizando KNeighborsClassifier() con el parámetro 
    n_neighbors=5, que indica que el modelo considerará los 5 vecinos más cercanos para realizar la clasificación. 
    Puedes ajustar este número según sea necesario para mejorar el rendimiento.
    
g) Entrena el modelo utilizando modeloKnn.fit() con los datos de entrenamiento escalados escalarAjustarEntrenamiento y las 
    etiquetas y_train.
    
h) Realiza las predicciones sobre el conjunto de prueba utilizando modeloKnn.predict(escalarAjustarPrueba) 
    y guarda el resultado en la variable prediccionesConjuntoPrueba.
    
i) Evalúa el rendimiento del modelo calculando la precisión (accuracy) mediante accuracy_score(y_test, prediccionesConjuntoPrueba) 
    y guárdala en precisionAccuracy. Calcula la matriz de confusión usando confusion_matrix(y_test, prediccionesConjuntoPrueba) 
    y guárdala en matrizConfusion. Genera el informe de clasificación completo utilizando 
    classification_report(y_test, prediccionesConjuntoPrueba) y guárdalo en classification_rep.
    
j) Muestra por pantalla la precisión del modelo, la matriz de confusión con un encabezado descriptivo, 
    y el informe de clasificación completo que incluye métricas como precision, recall y f1-score para cada clase de puntuación.
'''

# e) Normalizar los datos
scaler = StandardScaler()

# Ajustamos y transformamos el conjunto de entrenamiento
escalarAjustarEntrenamiento = scaler.fit_transform(X_train)

# Transformamos el conjunto de prueba (usando el ajuste del entrenamiento)
escalarAjustarPrueba = scaler.transform(X_test)


# f) Crear el modelo K-Nearest Neighbors
# Definimos n_neighbors=5 como indica el ejercicio
modeloKnn = KNeighborsClassifier(n_neighbors=5)


# g) Entrenar el modelo
modeloKnn.fit(escalarAjustarEntrenamiento, y_train)


# h) Realizar predicciones
prediccionesConjuntoPrueba = modeloKnn.predict(escalarAjustarPrueba)


# i) Evaluar el rendimiento
precisionAccuracy = accuracy_score(y_test, prediccionesConjuntoPrueba)
matrizConfusion = confusion_matrix(y_test, prediccionesConjuntoPrueba)
classification_rep = classification_report(y_test, prediccionesConjuntoPrueba)


# j) Mostrar resultados por pantalla
print(f"--- Evaluación del Modelo KNN ---")
print(f"Precisión (Accuracy): {precisionAccuracy:.4f}")

print("\nMatriz de Confusión:")
print(matrizConfusion)

print("\nInforme de Clasificación:")
print(classification_rep)


