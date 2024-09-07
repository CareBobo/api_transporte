from flask import Flask, jsonify, request
import pymysql.cursors

transporte = Flask(__name__)

# Configuración de la base de datos


def connection_mysql():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='mototx',
        cursorclass=pymysql.cursors.DictCursor)
    return connection


# Crear un usuario

@transporte.route('/usuarios', methods=['POST'])
def create_usuarios():

    data = request.get_json()
    connection = connection_mysql()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO usuarios (nombre, telefono) VALUES (%s, %s)"
            cursor.execute(sql, (data['nombre'], data['telefono']))
            result = cursor.fetchall()
        connection.commit()

    return jsonify({
        'Mensaje': 'Usuario registrado con exito'
    }), 201


# Obtener todos los datos

@transporte.route('/usuarios', methods=['GET'])
def get_usuarios():
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT id, nombre, telefono FROM usuarios'
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify({
            'Date': result
        }), 200


# Obtener un usuario por su ID

@transporte.route('/usuarios/<int:usuarios_id>', methods=['GET'])
def get_usuarios_by_id(usuarios_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM usuarios WHERE id = %s'
        cursor.execute(sql, (usuarios_id,))
        result = cursor.fetchone()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'Mensaje': 'Usuario no encontrado'}), 404


# Actualizar un usuario por ID

@transporte.route('/usuarios/<int:usuarios_id>', methods=['PUT'])
def update_usuarios(usuarios_id):
    data = request.json
    nombre = data.get('nombre')
    correo = data.get('telefono')

    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "UPDATE usuarios SET nombre = %s, telefono = %s WHERE id = %s"
        cursor.execute(sql, (nombre, correo, usuarios_id))
        connection.commit()

    return jsonify({'Mensaje': 'Usuario actualizado'}), 200


# Eliminar  usuario por ID

@transporte.route('/usuarios/<int:usuarios_id>', methods=['DELETE'])
def delete_usuarios(usuarios_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (usuarios_id))
        connection.commit()

    return jsonify({'Mensaje': 'Usuario eliminado'}), 200


# Crear un producto

@transporte.route('/vehiculo', methods=['POST'])
def create_vehiculo():

    data = request.get_json()
    nombre = data.get('nombre')
    placa = data.get('placa')

    connection = connection_mysql()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO vehiculo (nombre, placa) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, placa))
        connection.commit()

    return jsonify({
        'Mensaje': 'vehiculo creado'
    }), 201


#todos los vehiculo

@transporte.route('/vehiculo', methods=['GET'])
def get_vehiculo():
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT id, nombre, placa FROM vehiculo'
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify({
            'vehiculos': result
        }), 200


#vehiculo por su ID

@transporte.route('/vehiculo/<int:vehiculo_id>', methods=['GET'])
def get_vehiculo_id(vehiculo_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM vehiculo WHERE id = %s'
        cursor.execute(sql, (vehiculo_id,))
        result = cursor.fetchone()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'Mensaje': 'vehiculo no existe'}), 404


# Actualizar vehiculo por ID

@transporte.route('/vehiculo/<int:vehiculo_id>', methods=['PUT'])
def update_vehiculo(vehiculo_id):
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('placa')

    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "UPDATE vehiculo SET nombre = %s, placa = %s WHERE id = %s"
        cursor.execute(sql, (nombre, precio, vehiculo_id))
        connection.commit()

    return jsonify({'Mensaje': 'vehiculo actualizado'}), 200


# Eliminar vehiculo por ID

@transporte.route('/vehiculo/<int:vehiculo_id>', methods=['DELETE'])
def delete_vehiculo(vehiculo_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "DELETE FROM vehiculo WHERE id = %s"
        cursor.execute(sql, (vehiculo_id,))
        connection.commit()

    return jsonify({'Mensaje': 'vehiculo eliminado'}), 200


if __name__ == '__main__':
    transporte.run(debug=True)


