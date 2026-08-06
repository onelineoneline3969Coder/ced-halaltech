
# 🚀 Déploiement & Architecture – CED HalalTech™

**Version :** 1.0 (Production Infomaniak)  
**Date :** Janvier 2026  
**Principe :** Souveraineté, Sécurité, Juste Milieu (*Al-Wasatiyyah*)

---

## 🏗️ 1. Architecture Cible (Infomaniak Geneva 🇨🇭)

L'ensemble de l'écosystème est hébergé sur l'infrastructure souveraine d'Infomaniak à Genève, garantissant conformité LPD/RGPD et indépendance vis-à-vis du CLOUD Act.

```text
┌─────────────────────────────────────────────────────────────────┐
│                    INFOMANIAK GENEVA 🇨🇭                        │
│                     185.125.27.160                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────┼─────────────────────┐
        ↓                     ↓                     ↓
┌────────────────────┐   ┌──────────────┐   ┌────────────────┐
│  Node.js Hosting   │   │  PostgreSQL  │   │  Object Storage│
│  (Cœur Euria Hub)  │   │  (Données)   │   │  (Fichiers)    │
│                    │   │              │   │                │
│ • React/Vite       │   │ • Users      │   │ • Assets       │
│ • Express API      │   │ • Courses    │   │ • Backups      │
│ • Super IARP Pro   │   │ • Analytics  │   │                │
│ • FastAPI (Python) │   │ • Logs       │   │                │
└────────────────────┘   └──────────────┘   └────────────────┘
🛠️ 2. Prérequis & Configuration
2.1 Variables d'Environnement (Production)
À configurer dans le Manager Infomaniak > Node.js Hosting > Variables d'environnement.

bash
Copier
# --- Application ---
NODE_ENV=production
PORT=5000
DOMAIN=ced-halaltech.ch

# --- Base de Données (PostgreSQL Infomaniak) ---
DATABASE_URL=postgresql://user:password@pgsql.infomaniak.com:5432/ced_halaltech_prod
PGHOST=pgsql.infomaniak.com
PGPORT=5432
PGUSER=ced_admin
PGPASSWORD=<mot_de_passe_fort>
PGDATABASE=ced_halaltech_prod

# --- Sécurité & Session ---
SESSION_SECRET=<générer_64_caractères_aléatoires>
JWT_SECRET=<même_secret_que_nodejs>

# --- IA (Priorité Infomaniak AI) ---
INFOMANIAK_AI_API_KEY=<cle_infomaniak_ai>
INFOMANIAK_AI_PRODUCT_ID=<product_id>
# Fallback OpenAI (optionnel)
OPENAI_API_KEY=sk-...

# --- Paiement (Stripe) ---
STRIPE_SECRET_KEY=sk_live_...
VITE_STRIPE_PUBLIC_KEY=pk_live_...

# --- Stockage Objet (Optionnel) ---
DEFAULT_OBJECT_STORAGE_BUCKET_ID=<bucket_id>
PUBLIC_OBJECT_SEARCH_PATHS=public
PRIVATE_OBJECT_DIR=.private
🔒 Note de Sécurité : Générez une SESSION_SECRET forte avant de déployer :

bash
Copier
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
⚙️ 3. Procédure de Déploiement (Script Automatisé)
Ce script assure un déploiement reproductible, sécurisé et conforme au "Juste Milieu" (ni trop complexe, ni trop léger).

3.1 Script de Déploiement (deploy.sh)
Créez un fichier deploy.sh à la racine du projet avec le contenu suivant :

bash
Copier
#!/bin/bash
# ==============================================
# CED HALALTECH - SCRIPT DEPLOIEMENT INFOMANIAK
# ==============================================
set -e

echo "🚀 Déploiement CED HalalTech - Infomaniak Geneva"
echo "Bismillah ar-Rahman ar-Rahim"

# Configuration
SERVER="ced-halaltech.ch"
USER="infomaniak_user"
REMOTE_PATH="/web/ced-halaltech"

# 1. Build de Production
echo "🔨 Étape 1 : Build de production..."
npm ci --production=false
npm run build

if [ ! -d "dist" ]; then
    echo "❌ Échec du build : dossier dist/ introuvable."
    exit 1
fi
echo "✅ Build terminé."

# 2. Création Archive Sécurisée
echo "📦 Étape 2 : Création de l'archive..."
ARCHIVE="ced-halaltech-$(date +%Y%m%d-%H%M%S).tar.gz"
tar -czvf "$ARCHIVE" \
    dist/ \
    server/ \
    shared/ \
    package.json \
    package-lock.json \
    ecosystem.config.cjs \
    --exclude='node_modules' \
    --exclude='.git' \
    --exclude='*.log'

echo "✅ Archive créée : $ARCHIVE"

# 3. Transfert (Instructions)
echo "📤 Étape 3 : Transfert vers Infomaniak..."
echo "   Exécutez : scp $ARCHIVE $USER@$SERVER:$REMOTE_PATH/"
echo "   Puis sur le serveur :"
echo "   cd $REMOTE_PATH && tar -xzvf $ARCHIVE"
echo "   npm ci --production"
echo "   pm2 reload ecosystem.config.cjs --env production"

# 4. Vérification
echo "🔍 Étape 4 : Vérification post-déploiement..."
echo "   Testez : curl -I https://ced-halaltech.ch/api/health"
echo "   Testez : curl -I https://euriahub.ced-halaltech.ch"

echo "✅ Déploiement préparé avec succès. Barakallahu fikoum."
3.2 Commandes d'Exécution
Rendre le script exécutable :
bash
Copier
chmod +x deploy.sh
Lancer le build local :
bash
Copier
./deploy.sh
Transférer l'archive générée via SCP/SFTP (commande affichée par le script).
Sur le serveur Infomaniak : Extraire l'archive, installer les dépendances (npm ci --production) et redémarrer PM2.
🐍 4. Intégration Service FastAPI (Python)
Le service Python (synchronisation Access & Filtre EURIA) tourne en parallèle du Node.js.

4.1 Déploiement FastAPI
Environnement : Python 3.10+ dans un venv isolé sur le même serveur Infomaniak ou conteneur Docker.
Port : 8000 (interne), exposé via Nginx en /api/python/.
4.2 Configuration .env FastAPI
bash
Copier
DATABASE_URL=postgresql://user:password@pgsql.infomaniak.com:5432/ced_halaltech_prod
ACCESS_DSN=Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=/chemin/vers/base.accdb;
JWT_SECRET=<identique_au_nodejs>
EURIA_MIN_HALAL_SCORE=80.0
EURIA_STRICT_MODE=true
4.3 Intégration Node.js ↔ FastAPI
Le backend Node.js appelle FastAPI pour les tâches spécifiques (validation Charia, sync Access) via des requêtes HTTP internes sécurisées par JWT.

🛡️ 5. Sécurité & Conformité (Checklist)
Avant la mise en production, validez chaque point :

 Chiffrement : TLS 1.3 activé (Let's Encrypt Infomaniak).
 Données : Base PostgreSQL hébergée exclusivement à Genève.
 Accès : MFA activé sur le compte Infomaniak Manager.
 Secrets : Aucune clé API ou mot de passe dans le code source (tout dans les variables d'environnement).
 Backups : Script de backup quotidien configuré (BDD + Fichiers).
 Monitoring : UptimeRobot configuré sur https://ced-halaltech.ch/api/health.
📞 6. Support & Contacts
Infomaniak Support : +41 22 820 35 44 (24/7)
CED HalalTech Tech : contact@ced-halaltech.ch
Responsable Déploiement : Yakoubi Yamina
"Qu'Allah accepte ce travail et le rende bénéfique pour la Oumma."

