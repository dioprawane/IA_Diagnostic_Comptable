# Diagnostic Comptable IA

Ce projet est une application web de diagnostic comptable utilisant l'API OpenAI pour détecter les anomalies dans les écritures comptables et analyser les états financiers. L'application est développée avec Flask et permet d'entrer les données soit par saisie directe, soit en téléchargeant des fichiers de différents formats (CSV, Excel, JSON).

## Fonctionnalités

- Analyse des écritures comptables pour détecter les anomalies.
- Analyse des états financiers pour fournir une analyse détaillée.
- Support de l'entrée des données via texte ou téléchargement de fichier (CSV, Excel, JSON).
- Expertise comptable sur des questions précises.

## Prérequis

- Python 3.7 ou supérieur
- Un compte OpenAI avec une clé API

## Installation

1. Clonez le repository :

    ```bash
    git clone https://github.com/dioprawane/ia_diagnostic_comptable.git
    cd Diagnostic_Comptable_IA
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement :

    Créez un fichier `.env` à la racine du projet et ajoutez votre clé API OpenAI :

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Utilisation

1. Lancez l'application Flask :

    ```bash
    python app.py
    ```

2. Ouvrez votre navigateur et allez à l'adresse suivante :

    ```
    http://127.0.0.1:5000
    ```

3. Utilisez l'interface web pour entrer vos données comptables ou téléchargez un fichier à analyser.

## Structure du Projet

- `app.py` : Le fichier principal de l'application Flask.
- `requirements.txt` : Liste des dépendances Python nécessaires.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Références
- https://platform.openai.com/docs/guides/fine-tuning/create-a-fine-tuned-model
- https://cookbook.openai.com/examples/how_to_finetune_chat_models#check-job-status
- https://cookbook.openai.com/


## Auteurs

- **DIOP Serigne Rawane** - *Développeur principal* - [dioprawane](https://github.com/dioprawane)
- **BORREANI Théo** - *Développeur principal* - [sanseviera](https://github.com/sanseviera)

---

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou à me contacter directement.

