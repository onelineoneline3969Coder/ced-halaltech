#!/usr/bin/env python3
# 🏳️ MODULE: ÉTHIQUE / AUTOMATION_SCRIPT
# Projet: CED HalalTech™ - Outil de Conformité Charte EuriaHub
# Charte: EuriaHub-CED (Beige)
# Conformité: Souveraineté (Infomaniak CH), Zéro GAFAM, LPD
# Auteur: Yamina Yakoubi | PrettyhowQc AI
# Date: 2026-09-17
# Description: Script d'injection automatique des en-têtes de fichiers selon la charte couleur.

import os
import re
from datetime import datetime
from pathlib import Path

# --- CONFIGURATION DE LA CHARTE EURIAHUB-CED ---
# Mots-clés pour identifier le pôle basé sur le chemin ou le nom du fichier
POLES = {
    "orange": {
        "keywords": ["education", "academy", "lms", "course", "training", "mentor", "institut_yamina", "formation", "learning"],
        "color": "🟧",
        "name": "INCUBATION / FORMATION",
        "entity": "Institut Yamina",
        "charte": "Orange",
        "desc": "LMS, cours certifiants, Labs de recherche, Programmes de mentorat"
    },
    "blue": {
        "keywords": ["infra", "server", "database", "db", "docker", "cloud", "network", "config", "deployment"],
        "color": "🟦",
        "name": "INFRASTRUCTURE / SOCLE_TECHNIQUE",
        "entity": "CED HalalTech™",
        "charte": "Bleu Marine",
        "desc": "Cloud Halal™ (Infomaniak), CED Core Banking, Socle technique"
    },
    "purple": {
        "keywords": ["ai", "ia", "ml", "blockchain", "smart_contract", "fiqh", "algo", "research", "lab", "super_iarp"],
        "color": "🟪",
        "name": "IA & R&D / INNOVATION",
        "entity": "CED HalalTech™",
        "charte": "Violet",
        "desc": "Super IARP Pro, Algorithmes de Fiqh, Blockchain Zakat"
    },
    "green": {
        "keywords": ["green", "eco", "energy", "carbon", "optimization", "environment"],
        "color": "🟢",
        "name": "ÉCOLOGIE / GREENTECH",
        "entity": "CED HalalTech™",
        "charte": "Vert Pistache",
        "desc": "Green Coding Engine, Optimisation Carbone, Énergies renouvelables"
    },
    "beige": {
        "keywords": ["ethics", "legal", "compliance", "audit", "security", "sharia", "rgpd", "lpd", "manifesto"],
        "color": "🏳️",
        "name": "ÉTHIQUE / CONFORMITÉ",
        "entity": "CED HalalTech™",
        "charte": "Beige",
        "desc": "Compliance Charia, Audit FINMA, Gouvernance, Sécurité des données"
    }
}

# Extensions de fichiers supportées et leurs styles de commentaires
SUPPORTED_EXTENSIONS = {
    ".js": {"style": "js", "ext": "javascript"},
    ".ts": {"style": "js", "ext": "typescript"},
    ".jsx": {"style": "js", "ext": "javascript"},
    ".tsx": {"style": "js", "ext": "typescript"},
    ".py": {"style": "py", "ext": "python"},
    ".sol": {"style": "sol", "ext": "solidity"},
    ".sql": {"style": "sql", "ext": "sql"},
    ".yaml": {"style": "yaml", "ext": "yaml"},
    ".yml": {"style": "yaml", "ext": "yaml"},
    ".sh": {"style": "sh", "ext": "bash"},
    ".json": {"style": "json", "ext": "json"}, # Traitement spécial pour JSON
    ".md": {"style": "md", "ext": "markdown"}
}

def get_pole_info(file_path):
    """Détermine le pôle en fonction du chemin du fichier."""
    path_lower = file_path.lower()
    
    # Vérification par ordre de priorité (spécifique d'abord)
    for pole_key, pole_data in POLES.items():
        for keyword in pole_data["keywords"]:
            if keyword in path_lower:
                return pole_data
    
    # Défaut : Infrastructure (Bleu) si aucun mot-clé ne correspond
    return POLES["blue"]

def generate_header(pole, date_str):
    """Génère le bloc d'en-tête selon le langage (simplifié pour JS/Py pour l'exemple)."""
    author = "Yamina Yakoubi | PrettyhowQc AI"
    project = "CED HalalTech™"
    
    # Template de base (à adapter selon le style de commentaire du langage)
    # Ici on génère un format universel commenté, le script final devra l'adapter précisément
    header_template = f"""
 * {pole['color']} MODULE: {pole['name']}
 * Projet: {project} - {pole['entity']}
 * Charte: EuriaHub-CED ({pole['charte']})
 * Conformité: Souveraineté (Infomaniak CH), Zéro GAFAM, LPD
 * Auteur: {author}
 * Date: {date_str}
 * Description: {pole['desc']}
"""
    return header_template

def process_file(file_path, date_str):
    """Lit le fichier, vérifie l'en-tête, et l'injecte si manquant."""
    ext = Path(file_path).suffix.lower()
    
    if ext not in SUPPORTED_EXTENSIONS:
        return

    style = SUPPORTED_EXTENSIONS[ext]["style"]
    pole = get_pole_info(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier si un en-tête existe déjà (recherche simple des 200 premiers caractères)
    # On cherche la présence de l'emoji du pôle ou "MODULE:"
    if "MODULE:" in content[:300] or pole['color'] in content[:100]:
        print(f"⏭️  Déjà conforme : {file_path}")
        return

    # Génération de l'en-tête formaté selon le langage
    header_block = ""
    if style in ["js", "ts", "jsx", "tsx"]:
        header_block = f"/**{generate_header(pole, date_str)} */\n\n"
    elif style == "py":
        lines = generate_header(pole, date_str).split('\n')
        header_block = "".join([f"# {line}\n" for line in lines]) + "\n"
    elif style == "sol":
        lines = generate_header(pole, date_str).split('\n')
        header_block = "".join([f"// {line}\n" for line in lines]) + "\n"
    elif style == "sql":
        lines = generate_header(pole, date_str).split('\n')
        header_block = "".join([f"-- {line}\n" for line in lines]) + "\n"
    elif style == "yaml":
        lines = generate_header(pole, date_str).split('\n')
        header_block = "".join([f"# {line}\n" for line in lines]) + "\n"
    elif style == "sh":
        lines = generate_header(pole, date_str).split('\n')
        header_block = "#!/bin/bash\n" + "".join([f"# {line}\n" for line in lines]) + "\n"
    
    # Écriture du nouveau contenu
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(header_block + content)
        print(f"✅ Mis à jour ({pole['color']}): {file_path}")
    except Exception as e:
        print(f"❌ Erreur sur {file_path}: {e}")

def main():
    # Répertoire cible (par défaut le dossier courant ou celui passé en argument)
    target_dir = os.getcwd()
    if len(os.sys.argv) > 1:
        target_dir = os.sys.argv[1]
        
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    print(f"🚀 Démarrage de l'harmonisation EuriaHub-CED sur : {target_dir}")
    print(f"📅 Date appliquée : {date_str}")
    print("-" * 50)

    count = 0
    for root, _, files in os.walk(target_dir):
        # Ignorer les dossiers git, node_modules, etc.
        if '.git' in root or 'node_modules' in root or 'venv' in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            if Path(file).suffix.lower() in SUPPORTED_EXTENSIONS:
                process_file(file_path, date_str)
                count += 1

    print("-" * 50)
    print(f"🎉 Terminé. {count} fichiers analysés/traités.")
    print("Bi Hawlli Allah, votre code est maintenant harmonisé.")

if __name__ == "__main__":
    main()
