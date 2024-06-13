from flask import Flask, request, render_template, redirect, jsonify
import openai
import os
from dotenv import load_dotenv
import pandas as pd
from werkzeug.utils import secure_filename
from flask_cors import CORS

load_dotenv()  # Charger les variables d'environnement à partir du fichier .env

app = Flask(__name__)
CORS(app)  # Permettre les requêtes CORS de tous les domaines

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.Client()
print("Client", client)
print("Clef", openai.api_key)

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'json'}

fine_tuned_model_id = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_file(file):
    if file.filename.endswith('.csv'):
        return pd.read_csv(file).to_string(index=False)
    elif file.filename.endswith('.xlsx'):
        return pd.read_excel(file).to_string(index=False)
    elif file.filename.endswith('.json'):
        return pd.read_json(file).to_string(index=False)
    else:
        return None

def analyze_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Vous êtes un expert en détection d'anomalies comptables."},
            {"role": "user", "content": f"Analysez les écritures comptables suivantes et détectez les anomalies comme des champs de montant incorrects, des descriptions non valides, ou des comptes incorrects.\n\n{text}\n\nFournissez un résumé clair des anomalies détectées."}
        ]
    )
    #return response['choices'][0]['message']['content'].strip()
    return response.choices[0].message.content.strip()

def analyze_financial_statement(statement):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Vous êtes un expert en analyse financière."},
            {"role": "user", "content": f"Analysez l'état financier suivant et fournissez une analyse :\n\n{statement}"}
        ],
    )
    #return response['choices'][0]['message']['content'].strip()
    return response.choices[0].message.content.strip()

def financial_balance_analysis(question):
    model = fine_tuned_model_id if fine_tuned_model_id else "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Vous êtes un expert en équilibre financier."},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()

@app.route('/')
def index():
    #return render_template('index.html')
    #return redirect("http://127.0.0.1:5500/miage_front_ia/index.html")
    return "Flask Server is running"

@app.route('/diagnose', methods=['POST'])
def diagnose():
    content = request.form.get('content')
    file = request.files.get('file')
    analysis_type = request.form['analysis_type']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_content = read_file(file)
        if analysis_type == 'entries':
            result = analyze_text(file_content)
        elif analysis_type == 'statement':
            result = analyze_financial_statement(file_content)
        elif analysis_type == 'balance':
            result = financial_balance_analysis(file_content)
        else:
            result = "Type d'analyse non reconnu."
    elif content:
        if analysis_type == 'entries':
            result = analyze_text(content)
        elif analysis_type == 'statement':
            result = analyze_financial_statement(content)
        elif analysis_type == 'balance':
            result = financial_balance_analysis(content)
        else:
            result = "Type d'analyse non reconnu."
    else:
        result = "Aucun contenu ou fichier valide fourni pour l'analyse."
    
    #return render_template('result.html', content=content or filename, result=result)
    return jsonify({'content': content or filename, 'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
