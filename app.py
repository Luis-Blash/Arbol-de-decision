import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier

datos = pandas.read_csv('/app/Enfermedades.csv')

i = 0
enfermedades = {}
for e in  datos["Respuesta"]:
    enfermedades.setdefault(e,i)
    i += 1

datos["Respuesta"] = datos["Respuesta"].map(enfermedades)

caracteristicas = []
for a in range(len(datos.columns)-1):
    caracteristicas.append(datos.columns[a])
print(datos)

# Dependiente
x = datos[caracteristicas]
# Independiente
y = datos["Respuesta"]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x,y)
datos = tree.export_graphviz(dtree, out_file=None, feature_names=caracteristicas)
graph = pydotplus.graph_from_dot_data(datos)
graph.write_png('/app/im.png')


def milista():
    e = ["Tos","Mucosidad","Dolor de Garganta","Diarrea","Inflamacion",
    "Dolor muscular","Dolor cabeza","Fatiga","Nauseas","Fiebre"]
    d = []
    for i in range(10):
        print(f"Tienes {e[i]}")
        if( i != 9):
            print("1)Si \n0)No")
        d.append(int(input()))
    return d

# Respuesta
respuesta = dtree.predict([milista()])
for k,v in enfermedades.items():
    if(v == respuesta[0]):
        print(f"{k}")

