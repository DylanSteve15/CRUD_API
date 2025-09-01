#Primera version V.1.0 agregamos crear y actualizar .
#Segunda version v.1.1 se agrega Eliminar 
#Tercera Version v.1.2 se crea el curl.sh
# cuarta version v.1.3 se crea el puerto_host 5000

from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos temporal en memoria (lista de diccionarios)
estudiantes = []

# Ruta raíz de bienvenida
@app.route('/')
def home():
    return "API de CRUD de Estudiantes está funcional."

# Obtener todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def get_estudiantes():
    return jsonify(estudiantes), 200

# Obtener un estudiante por ID
@app.route('/estudiantes/<int:estudiante_id>', methods=['GET'])
def get_estudiante(estudiante_id):
    estudiante = next((e for e in estudiantes if e['id'] == estudiante_id), None)
    if estudiante is None:
        return jsonify({'error': 'Estudiante no encontrado'}), 404
    return jsonify(estudiante), 200

# Crear un nuevo estudiante
@app.route('/estudiantes', methods=['POST'])
def create_estudiante():
    if not request.json or 'nombre_estudiante' not in request.json:
        return jsonify({'error': 'Solicitud incorrecta'}), 400
    
    new_id = max(e['id'] for e in estudiantes) + 1 if estudiantes else 1
    estudiante = {
        'id': new_id,
        'nombre_estudiante': request.json['nombre_estudiante'],
        'horario_clase': request.json.get('horario_clase', ''),
        'nombre_clase': request.json.get('nombre_clase', ''),
        'docente_clase': request.json.get('docente_clase', '')
    }
    estudiantes.append(estudiante)
    return jsonify(estudiante), 201

# Actualizar un estudiante existente
@app.route('/estudiantes/<int:estudiante_id>', methods=['PUT'])
def update_estudiante(estudiante_id):
    estudiante = next((e for e in estudiantes if e['id'] == estudiante_id), None)
    if estudiante is None:
        return jsonify({'error': 'Estudiante no encontrado'}), 404
    if not request.json:
        return jsonify({'error': 'Solicitud incorrecta'}), 400
    
    estudiante['nombre_estudiante'] = request.json.get('nombre_estudiante', estudiante['nombre_estudiante'])
    estudiante['horario_clase'] = request.json.get('horario_clase', estudiante['horario_clase'])
    estudiante['nombre_clase'] = request.json.get('nombre_clase', estudiante['nombre_clase'])
    estudiante['docente_clase'] = request.json.get('docente_clase', estudiante['docente_clase'])
    
    return jsonify(estudiante), 200

# Eliminar un estudiante
@app.route('/estudiantes/<int:estudiante_id>', methods=['DELETE'])
def delete_estudiante(estudiante_id):
    estudiante = next((e for e in estudiantes if e['id'] == estudiante_id), None)
    if estudiante is None:
        return jsonify({'error': 'Estudiante no encontrado'}), 404
    estudiantes.remove(estudiante)
    return jsonify({'result': 'Estudiante eliminado'}), 200

if __name__ == '__main__':
    # Importante para Codespaces: host=0.0.0.0 y port=5000
    app.run(debug=True, host='0.0.0.0', port=5000)
