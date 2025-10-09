import dao_Carrera as dao   
from flask import jsonify 
from flask import Flask
import carrera
import mysql.connector
app = Flask(__name__)

def connect_db ():
    user = "root" 
    passwd = "12345678"
    cnx = dao.connect_db(user, passwd)
    return cnx
conexion = connect_db()
cursor = conexion.cursor(dictionary=True)  # Retorna resultados como diccionarios
    
@app.route('/')
def hola_mundo():
    return '<p>Hola  en Flask!</p>'

@app.route('/ver/carreras/', methods=['GET'])
def api_ver_carreras():
    return jsonify(dao.ver_carreras(cursor))


'''@app.route('/agregar/carreras/', methods=['POST'])
def api_ver_carreras(carrera):
    return jsonify(dao.ver_carreras(cursor))'''

