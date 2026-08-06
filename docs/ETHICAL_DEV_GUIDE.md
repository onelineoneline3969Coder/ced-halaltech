# 📘 Guide de Développement Éthique (Ethical Dev Kit)
**CED HalalTech – Architecture Souveraine & Code Conscient**

> *"Le code est une forme d'adoration par l'action. Chaque ligne doit refléter la vérité, la justice et la protection de l'utilisateur."*

Ce guide définit les standards de développement pour l'écosystème CED HalalTech. Il assure que notre infrastructure technique reste alignée avec nos principes fondateurs : **Souveraineté Suisse**, **Conformité Charia (AAOIFI)** et **Respect de la Vie Privée (LPD/RGPD)**.

## 1. Le Principe du "Juste Milieu" dans le Code (*Al-Wasatiyyah*)
Notre philosophie technique rejette les extrêmes : ni complexité inutile (over-engineering), ni laxisme sécuritaire.

- **Sobriété Algorithmique :** Privilégier la lisibilité et l'efficacité énergétique. Un code simple est plus auditable et donc plus éthique.
- **Transparence Radicale :** Aucune "boîte noire". Chaque fonction critique (calcul financier, gestion de données) doit être documentée et compréhensible par un auditeur tiers.
- **Équilibre des Ressources :** Optimiser l'utilisation du serveur (Infomaniak) pour minimiser l'empreinte écologique, sans compromettre la sécurité.

## 2. Règles d'Or : Conformité Charia & Finance Éthique
Le code doit intégrer des garde-fous empêchant toute opération non conforme (*Haram*).

### A. Interdiction Stricte du Riba (Intérêt)
Aucune fonction ne doit calculer, accréditer ou simuler des intérêts composés ou des prêts usuraires.

- **❌ Interdit :** Fonctions nommées `calculateInterest`, `applyLateFeeInterest`, `compoundDebt`.
- **✅ Autorisé :** Fonctions basées sur le partage de profits/risques ou frais de service fixes.
  - *Exemple de nommage :* `calculateProfitShare`, `applyServiceFee`, `processCharityDonation`.

**Exemple de Code (Node.js) :**

```javascript
// ❌ MAUVAISE PRATIQUE (Non-Conforme)
function calculateMonthlyInterest(principal, rate, months) {
  return principal * Math.pow((1 + rate), months); // Riba interdit
}

// ✅ BONNE PRATIQUE (Conforme - Murabaha/Mudaraba)
function calculateProfitShare(investment, profitRate, duration) {
  // Calcul basé sur un bénéfice réel préétabli, pas un intérêt temporel
  const share = investment * profitRate; 
  return { netProfit: share, principle: investment };
}
### B. Transparence des Frais (Gharar)
L'incertitude excessive est interdite. Les frais doivent être clairs, fixes ou proportionnels, et jamais cachés dans des algorithmes complexes.
- **Règle :** Tout calcul de frais doit être déterministe et affiché à l'utilisateur *avant* validation de la transaction.

## 3. Règles d'Or : Souveraineté & Protection des Données (LPD/RGPD)
Nos données sont un dépôt (*Amanah*). Elles ne doivent jamais quitter la juridiction suisse.

### A. Localisation des Données (Data Residency)
- **Contrainte :** Toutes les connexions aux bases de données et au stockage objet doivent pointer exclusivement vers les endpoints **Infomaniak (Suisse)**.
- **Interdiction :** Aucun appel API vers des services cloud américains (AWS, Google Cloud, Azure) ou des SaaS tiers non conformes LPD pour le traitement de données personnelles.

### B. Privacy by Design (Confidentialité par Défaut)
- **Minimisation :** Ne collecter que les données strictement nécessaires.
- **Chiffrement :**
  - **Au repos :** AES-256 obligatoire pour tout champ sensible (nom, email, solde).
  - **En transit :** TLS 1.3 obligatoire.
- **Anonymisation :** Les logs de production ne doivent jamais contenir de PII (Personally Identifiable Information). Utiliser des IDs uniques hashés.

**Exemple de Configuration (Database) :**

```javascript
// ✅ Configuration Infomaniak (Suisse) uniquement
const dbConfig = {
  host: 'db-12345.infomaniak.ch', // Endpoint Suisse vérifié
  ssl: { rejectUnauthorized: true }, // TLS 1.3 obligatoire
  encryption: { algorithm: 'AES-256-GCM' } // Chiffrement au repos
};
// ❌ Interdit : host: 'aws-us-east-1...'
## 4. Standards de Sécurité & Qualité (FINMA / ISO 27001)
La sécurité n'est pas une option, c'est un devoir religieux et légal.

- **Authentification :** MFA (Multi-Factor Authentication) obligatoire pour tous les comptes administrateurs et privilégiés.
- **Gestion des Secrets :** Aucune clé API, mot de passe ou clé privée ne doit être "hardcodé" dans le code source. Utiliser exclusivement les variables d'environnement sécurisées ou un gestionnaire de secrets (Vault).
- **Revue de Code :** Chaque Pull Request doit être validée par au moins un autre développeur, avec une check-list spécifique "Éthique & Conformité".

## 5. Couleurs et Design Éthique (UI/UX)
Même l'interface visuelle doit refléter le Juste Milieu.
- **Clarté :** Éviter les "Dark Patterns" (designs trompeurs qui poussent à l'achat ou cachent des désabonnements).
- **Couleurs :** Utiliser une palette apaisante et professionnelle. Éviter le rouge agressif pour les erreurs (préférer l'orange ou le bleu foncé) et le vert excessif pour inciter à la dépense.
- **Accessibilité :** Le service doit être accessible à tous, quel que soit le handicap (contraste WCAG AA minimum).

## 6. Checklist avant Commit (Pull Request)
Avant de fusionner du code dans la branche principale, le développeur doit cocher :

- [ ] Le code contient-il des appels vers des services non-suisses ? **(NON)**
- [ ] Y a-t-il des calculs d'intérêts (Riba) ? **(NON)**
- [ ] Les données sensibles sont-elles chiffrées ou anonymisées dans les logs ? **(OUI)**
- [ ] Les frais sont-ils affichés clairement pour l'utilisateur ? **(OUI)**
- [ ] Le code est-il simple, lisible et documenté ? **(OUI)**

---

**Conclusion**
En suivant ce guide, chaque contributeur participe à la construction d'une alternative crédible, éthique et souveraine. Que chaque ligne de code écrite ici soit une source de bénédiction (*Barakah*) pour son auteur et pour la communauté.

*© 2026 CED HalalTech. Hébergé en Suisse par Infomaniak.*
