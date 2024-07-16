# from flask import Flask, request, jsonify
# import mysql.connector
# from mysql.connector import Error

# app = Flask(__name__)

# def create_connection():
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='dashboard_db',
#             user='root',
#             password='123456'
#         )
#     except Error as e:
#         print(f"The error '{e}' occurred")

#     return connection

# @app.route('/')
# def index():
#     return "Welcome to the Data Visualization Dashboard API"



from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import json
from config import db_config

app = Flask(__name__)

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=db_config['localhost'],
            database=db_config['dashboard_db'],
            user=db_config['root'],
            password=db_config['123456']
        )
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

@app.route('/')
def index():
    return "Welcome to the Data Visualization Dashboard API"

@app.route('/data', methods=['GET'])
def get_all_data():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(rows)

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(row)

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json
    connection = create_connection()
    cursor = connection.cursor()
    sql = """INSERT INTO data (end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, source, title, likelihood)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (data['end_year'], data['intensity'], data['sector'], data['topic'], data['insight'], data['url'], data['region'], data['start_year'], data['impact'], data['added'], data['published'], data['country'], data['relevance'], data['pestle'], data['source'], data['title'], data['likelihood'])
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Data added successfully"}), 201

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.json
    connection = create_connection()
    cursor = connection.cursor()
    sql = """UPDATE data SET end_year = %s, intensity = %s, sector = %s, topic = %s, insight = %s, url = %s, region = %s, start_year = %s, impact = %s, added = %s, published = %s, country = %s, relevance = %s, pestle = %s, source = %s, title = %s, likelihood = %s WHERE id = %s"""
    values = (data['end_year'], data['intensity'], data['sector'], data['topic'], data['insight'], data['url'], data['region'], data['start_year'], data['impact'], data['added'], data['published'], data['country'], data['relevance'], data['pestle'], data['source'], data['title'], data['likelihood'], id)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Data updated successfully"})

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Data deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
