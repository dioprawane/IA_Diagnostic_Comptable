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

## Fine-Tuning d'un Modèle Financier avec l'API OpenAI

Cette partie se concentre sur le fine-tuning d'un modèle à l'aide de l'API OpenAI pour mieux
comprendre et répondre aux questions liées à l’équilibre financier. Voici un aperçu détaillé des
fonctionnalités et caractéristiques du modèle fine-tuné. Ce model a pu être réalisé grâce à la
documentation d’open ai sur le fine-tuning et à travers le contenu de ce lien également « https://
cookbook.openai.com/examples/how_to_finetune_chat_models#check-job-status »

### Fonctionnalités et Capacités

1. Préparation de l'ensemble de données
    * Données d'entraînement : Un ensemble de données diversifié couvrant divers aspects
des bilans financiers et issu principalement du cours de M Anigo sur l’équilibre financier, a
été préparé pour l'entraînement. Cela inclut des définitions, des explications de concepts
et des descriptions détaillées des composants du bilan.
    * Données de validation : Un ensemble de données de validation est utilisé pour évaluer les
performances du modèle pendant le processus de fine-tuning, garantissant que le modèle
se généralise bien aux nouvelles données non vues.
    * Données de test : Des données de test séparées sont utilisées pour tester les
performances et la précision du modèle final.

2. Couverture étendue des concepts financiers

Le modèle fine-tuné est conçu pour comprendre et fournir des explications détaillées sur un
large éventail de sujets liés aux bilans financiers qui se trouvent sur « la liste des
questions.md » , tels que :
    * Définition et composants d'un bilan financier
    * Approche patrimoniale du bilan
    * Structure et détails des actifs et passifs du bilan
    * Systèmes de présentation des bilans
    * Annexes et leurs composants
    * Bilans fonctionnels et financiers
    * Tableaux de flux de trésorerie et leur interprétation

4. Processus de Fine-Tuning
    * Formatage des données : Les données sont formatées en fichiers JSONL pour un
téléchargement et un traitement sans faille par l'API OpenAI.
   * Intégration API : En utilisant l'API OpenAI, les fichiers de formation et de validation sont
téléchargés, et un travail de fine-tuning est créé.
   * Suivi du travail : Le statut du travail de fine-tuning est continuellement surveillé pour
assurer son achèvement réussi

5. Inférence et Validation
    * Reconnaissance des questions : Le modèle peut reconnaître et répondre à un ensemble
de questions prédéfinies et valides liées aux bilans financiers.
    * Messages système : Le processus d'inférence inclut des messages système spécifiques
pour définir le contexte, garantissant que le modèle répond en tant qu'expert financier.
    * Test en temps réel : Les réponses du modèle sont testées en temps réel avec des
questions valides et invalides pour démontrer ses capacités et ses limitations.

6. Réponses détaillées

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

