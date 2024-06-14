from flask import Flask, request, render_template, redirect, jsonify
import openai
import os
from dotenv import load_dotenv
import pandas as pd
from werkzeug.utils import secure_filename
from flask_cors import CORS
import difflib
#from fine_tuning import valid_questions

load_dotenv()  # Charger les variables d'environnement à partir du fichier .env

app = Flask(__name__)
CORS(app)  # Permettre les requêtes CORS de tous les domaines

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.Client()
print("Client", client)
print("Clef", openai.api_key)

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'json'}

fine_tuned_model_id = "ft:gpt-3.5-turbo-0125:universit-cote-d-azur:financial-balance:9a4MVECl"  # ID du modèle fine-tuné

valid_questions = [
    "Définition du bilan financier :",
    "Approche patrimoniale du bilan :",
    "Structure du bilan :",
    "Détails du bilan - Actif :",
    "Détails du bilan - Passif :",
    "Le BILAN présenté selon différents systèmes :",
    "L’ANNEXE :",
    "Le bilan fonctionnel :",
    "Le bilan fonctionnel et les cycles économiques de l’entreprise :",
    "Le bilan fonctionnel - éléments circulants :",
    "L’équilibre financier :",
    "Qu'est-ce que le besoin en fond de roulement (BFR) ?",
    "Comment est décomposé le besoin en fond de roulement (BFR) ?",
    "Comment se calcule le besoin en fond de roulement (BFR) ?",
    "Quels sont les facteurs impactant le niveau du besoin en fond de roulement d’exploitation (BFRE) ?",
    "Que se passe-t-il lorsque le BFRE progresse plus rapidement que le FRNG ?",
    "Qu'est-ce qu'un BFRE négatif ?",
    "Quels sont les ratios essentiels pour analyser le BFRE ?",
    "Qu'est-ce que le délai de rotation des stocks ?",
    "Qu'est-ce que le délai de crédit clients ?",
    "Qu'est-ce que le délai de crédit fournisseurs ?",
    "Qu'est-ce que le BFR hors exploitation (BFRHE) ?",
    "Pourquoi l'entreprise doit-elle gérer son BFR ?",
    "Qu'est-ce que la trésorerie nette ?",
    "Comment se calcule la trésorerie nette ?",
    "Quels sont les niveaux de la trésorerie nette ?",
    "Qu'est-ce qu'une trésorerie positive ?",
    "Qu'est-ce qu'une trésorerie négative ?",
    "Qu'est-ce qu'une trésorerie nulle ?",
    "Quels sont les ratios essentiels pour analyser la trésorerie nette (TN) ?",
    "Qu'est-ce que le ratio de couverture des capitaux investis ?",
    "Qu'est-ce que le ratio d’autonomie financière ?",
    "Qu'est-ce que le ratio de financement courant du BFR ?",
    "Qu'est-ce que le fond de roulement net global (FRNG) ?",
    "Comment se calcule le fond de roulement net global (FRNG) ?",
    "Que permet de mesurer le calcul du FRNG en utilisant les données de haut de bilan ?",
    "Que permet de mesurer le calcul du FRNG en utilisant les données de bas de bilan ?",
    "Quels sont les facteurs déterminants du niveau du fond de roulement net global (FRNG) ?",
    "Pourquoi une entreprise industrielle a-t-elle besoin d'un FRNG plus élevé ?",
    "Le FRNG est-il toujours positif dans les entreprises ?",
    "Une baisse du FRNG traduit-elle toujours une situation critique ?",
    "Comment améliorer le fond de roulement net global ?",
    "Qu'est-ce que le bilan financier ?",
    "Quels sont les objectifs du bilan financier ?",
    "Comment est structurée le bilan financier ?",
    "Quels sont les retraitements nécessaires pour le bilan financier ?",
    "Quels postes du bilan comptable doivent être éliminés ?",
    "Comment se présente le bilan financier après les retraitements ?",
    "Pouvez-vous donner un exemple de retraitement dans le bilan financier ?",
    "Quels sont les tableaux de flux ?",
    "Qu'est-ce que le tableau de financement ?",
    "Quels sont les objectifs du tableau de financement ?",
    "Comment est établi le tableau de financement ?",
    "Quelle est la structure du tableau de financement du PCG ?",
    "Qu'est-ce que le tableau des emplois et des ressources ?",
    "Quelles sont les ressources durables ?",
    "Quels sont les emplois stables ?",
    "Comment analyser le tableau des emplois et des ressources ?",
    "Comment se présente le tableau des variations du fonds de roulement net global ?",
    "Qu'est-ce que les besoins et les dégagements ?",
    "Comment calculer les soldes dans le tableau des variations du fonds de roulement net global ?",
    "Qu'est-ce que le tableau des flux de trésorerie ?",
    "Quels sont les objectifs du tableau des flux de trésorerie ?",
    "Quels sont les éléments constitutifs de la trésorerie ?",
    "Quelle est la structure du tableau des flux de trésorerie ?",
    "Comment se calcule la variation de trésorerie ?",
    "Quels sont les modèles du tableau des flux de trésorerie ?",
    "Comment analyser les flux de trésorerie ?"
]

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

def is_valid_question(question):
    threshold = 0.7  # Ajustez ce seuil selon le besoin
    # Convertir la question et les questions valides en minuscules
    question_lower = question.lower()
    valid_questions_lower = [q.lower() for q in valid_questions]
    closest_matches = difflib.get_close_matches(question_lower, valid_questions_lower, n=1, cutoff=threshold)
    return len(closest_matches) > 0

def financial_balance_analysis(question):
    if not is_valid_question(question):
        return "La question n'est pas valide."
    
    try:
        #model = fine_tuned_model_id if fine_tuned_model_id else "gpt-3.5-turbo"
        model = fine_tuned_model_id
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Tu es un expert en équilibre financier."},
                {"role": "user", "content": question}
            ],
            #max_tokens=150
        )
        #return response['choices'][0]['message']['content'].strip()
        return response.choices[0].message.content.strip()
    except openai.error.InvalidRequestError as e:
        print(f"Error: {e}")
        return "Le modèle fine-tuné spécifié n'existe pas ou vous n'y avez pas accès."


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
