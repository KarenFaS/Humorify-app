from flask import Flask, request, jsonify, render_template
from datetime import datetime
import openai
import mysql.connector
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

# Configurar la clave de API de OpenAI
openai.api_key = 'sk-proj-AZZkHYvHDsgeERWDTUuPT3BlbkFJmWJFpsF8bagBO1oTsLvS'

# Configurar la base de datos MySQL
db_config = {
    'user': 'admin',
    'password': 'TheBridge2024',
    'host': 'proyecto-gpt.c1qae640iwed.eu-north-1.rds.amazonaws.com',
    'database': 'funny_gpt_db',
    'port': 3306
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def get_gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Dame una respuesta corta y con poco graciosa a la pregunta"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response.choices[0].message['content'].strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    location = data.get('location')
    
    if not question:
        return jsonify({'response': 'Por favor, proporciona una pregunta.'}), 400

    response = get_gpt_response(question)

    # Guardar la pregunta y respuesta en la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO messages (date_time, location, question, response) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (datetime.now(), location, question, response))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

