from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tareas = ["Hacer compras", "Estudiar para el examen", "Practicar Python"]

@app.route('/')
def lista_tareas():
    return render_template('tareas.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    nueva_tarea = request.form.get('nueva_tarea')
    if nueva_tarea:
        tareas.append(nueva_tarea)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)