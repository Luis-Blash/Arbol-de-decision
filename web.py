from crypt import METHOD_CRYPT, methods
from flask import Flask,render_template,request,redirect,url_for
import app as predicion

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html",fallo = "-",preguntas = predicion.caracteristicas)

@app.route("/datos",methods=['POST'])
def datos():
	a = request.form["Temperatura"].isnumeric()
	if(a):
		# recibimos los datos del formulario
		datos = []
		for i in predicion.caracteristicas:
			datos.append(request.form[i])
		
		# Usando el arreglo creado podemos ver que tipo de respuesta es.
		respuesta = predicion.dtree.predict([datos])
		for k,v in predicion.enfermedades.items():
			if(v == respuesta[0]):
				return render_template("prediccion.html",enfermedad = k)
	else:
		return render_template("index.html",fallo = "Temperatura tiene que se numero", preguntas = predicion.caracteristicas)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')