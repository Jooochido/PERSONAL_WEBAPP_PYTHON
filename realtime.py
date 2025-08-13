from flask import Flask, render_template
from flask_socketio import SocketIO

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la clave secreta para sesiones
app.config['SECRET_KEY'] = 'mi_clave_secreta_segura'

# Inicializar SocketIO con la aplicación Flask
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('realtime.html')

@socketio.on('mensaje')
def manejar_mensaje(data):
    # Obtener el nombre y el nuevo mensaje del diccionario data
    nombre = data['nombre']
    nuevo_mensaje = data['mensaje']
    # Emitir un evento actualizar_mensajes a todos los clientes conectados
    socketio.emit('actualizar_mensajes', {'nombre': nombre, 'mensaje': nuevo_mensaje})

# Ejecutar la aplicación Flask con el servidor SocketIO en modo de depuración
if __name__ == '__main__':
    socketio.run(app, debug=True)