from flask import Flask, request, render_template



app = Flask(__name__)



@app.route('/')
def home():
    return "Pagina de inicio"


#Ruta parametros por URL
@app.route('/consulta')
def ruta_consulta():
    producto = request.args.get("product")
    talla = request.args.get("size")
    if producto and talla is None:
        return f"Se esta consultando el producto {producto}"
    if talla and producto is None:
        return f"Por favor ingrese el producto"
    if talla is None and producto is None:
        return f"Bienvenido a la pagina de ropa"

    
    
    return f"Se esta consultando el producto {producto} y la talla {talla}"

#Ruta para capturar datos por el cuerpo de solicitud para el body
@app.route("/registro", methods=["GET"]) 
def ruta_registro():
    return render_template("formulario.html")

@app.route("/registro", methods=["POST"])
def procesar_registro():
    nombre = request.form.get("Nombre")
    correo = request.form.get("correo")
    return f"El estudiante a registrar es {nombre} y su correo es {correo}"
    






if __name__ == "__main__":
    app.run(debug=True)