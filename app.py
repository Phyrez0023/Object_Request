from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/inscripcion-curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return f'Inscrito: {nombre} {apellido} en el curso {curso}'
    return render_template('inscripcion_curso.html')

@app.route('/registro-usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        contrasena = request.form['contrasena']
        return f'Usuario registrado: {nombre} {apellido}, Correo: {email}'
    return render_template('registro_usuarios.html')

@app.route('/registro-productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f'Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}'
    return render_template('registro_productos.html')

@app.route('/registro-libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form.get('medio')
        return f'Libro registrado: {titulo} por {autor}, Medio: {medio}'
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)
