import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import os

datos = pandas.read_csv(f"{os.getcwd()}/Enfermedades.csv")

i = 0
enfermedades = {}
for e in  datos["Respuesta"]:
    enfermedades.setdefault(e,i)
    i += 1

datos["Respuesta"] = datos["Respuesta"].map(enfermedades)

caracteristicas = []
for a in range(len(datos.columns)-1):
    caracteristicas.append(datos.columns[a])

#print(datos)
#print(len(enfermedades))

# Dependiente
x = datos[caracteristicas]
# Independiente
y = datos["Respuesta"]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x,y)
datos = tree.export_graphviz(dtree, out_file=None, feature_names=caracteristicas)
graph = pydotplus.graph_from_dot_data(datos)
graph.write_png(f"{os.getcwd()}/arbol.png")

"""
def milista(caracteristicas):
    aux = 0
    d = []
    for i in caracteristicas:
        print(f"Tienes {i}")
        if( aux != len(caracteristicas)-1):
            print("1)Si \n0)No")
        d.append(int(input()))
        aux += 1
    return d

# Respuesta
respuesta = dtree.predict([milista(caracteristicas)])
for k,v in enfermedades.items():
    if(v == respuesta[0]):
        print(f"{k}")
"""
