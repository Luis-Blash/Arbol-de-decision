import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import os

# usamos pandas para poder leer el archivo csv, y obtener los datos
datos = pandas.read_csv(f"{os.getcwd()}/Enfermedades.csv")

# Todas las respuestas necesitan ser de tipo numero
# indicamos que cada enfermedad tenga un indice
# Puede haber respuestas repetidas, pero con diferentes, por eso es el indice
i = 0
enfermedades = {}
for e in  datos["Respuesta"]:
    enfermedades.setdefault(e,i)
    i += 1

# Ahora lo devolvemos a la Columan para que cambie todas las enfermedades por sus indices
datos["Respuesta"] = datos["Respuesta"].map(enfermedades)

# Tomamos todas la columnas sin la ultima para poder indicar nuestros datos independientes y dependientes
caracteristicas = []
for a in range(len(datos.columns)-1):
    caracteristicas.append(datos.columns[a])

# Independiente sera nuestras columnas
x = datos[caracteristicas]
# Dependiente seran todas aquellas respuestas
y = datos["Respuesta"]

# Creacion del arbol pasando X y Y,para poderlo crear
dtree = DecisionTreeClassifier()
dtree = dtree.fit(x,y)
datos = tree.export_graphviz(dtree, out_file=None, feature_names=caracteristicas)

# Creamos la imagen para poder verlo visualmente
graph = pydotplus.graph_from_dot_data(datos)
graph.write_png(f"{os.getcwd()}/arbol.png")

"""
# Respuesta predecise el sintoma y lo que recibe es un arreglo con los datos 
# 1,1,1,0,1,0,1,1,1,1,0,0,38,Resfriado comun

respuesta = dtree.predict([[1,1,1,0,1,0,1,1,1,1,0,0,38,0]])

# Como nos devuelve un numero, usaremos el diccionario de enfermedades del principio
# Para poder ver que enfermedad es

for k,v in enfermedades.items():
    if(v == respuesta[0]):
        print(f"{k}")
"""
