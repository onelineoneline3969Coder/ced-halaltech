# 🤝 Politique de Contribution (CED HalalTech™)

**Version :** 1.0  
**Date :** 21 Août 2026  
**Statut :** En vigueur

Bienvenue dans l'écosystème **CED HalalTech™**. Ce document encadre toute contribution externe au projet afin de garantir la cohérence éthique, la sécurité des données et le respect de la propriété intellectuelle.

---

## 1. Principes Fondamentaux

Toute contribution à ce projet implique l'acceptation sans réserve des trois piliers suivants :

1.  **Souveraineté Numérique** : Tout contributeur accepte que les données et le code restent hébergés exclusivement en **Suisse** (Infomaniak). Aucun transfert vers des juridictions non conformes (ex: CLOUD Act) n'est toléré.
2.  **Éthique & Conformité Charia** : Toute ligne de code doit être validée par les **"Gardiens Éthiques"** du projet. Elle ne doit contenir aucun élément facilitant le *Ribâ* (intérêt), le *Gharar* (incertitude illicite) ou le *Maysir* (jeu/spéculation).
3.  **Propriété Intellectuelle** : Le code source reste la propriété exclusive de **CED HalalTech™**. Toute contribution est cédée sous licence propriétaire (voir [LICENSE](../LICENSE)).

---

## 2. Modalités de Contribution

### A. Demande d'Autorisation Préalable
Contrairement aux projets open-source classiques, **l'accès en écriture n'est pas public**.
*   Toute contribution externe nécessite une demande signée via le formulaire **[Demande d'Autorisation d'Utilisation](AUTHORIZATION_FORM.md)**.
*   L'accès au dépôt (ACL) n'est accordé qu'après validation de ce formulaire et signature d'un NDA.

### B. Processus de Validation (Pull Request)
Toute proposition de modification (Pull Request) suit un cycle de validation en trois étapes :

1.  **Revue Technique** : Analyse automatique (CodeQL) et manuelle de la sécurité et de la performance.
2.  **Revue Éthique** : Vérification de la conformité Charia et RGPD par le comité d'audit.
3.  **Revue de Code** : Respect strict des standards de codage (voir section 4).

---

## 3. Rôles et Responsabilités

| Rôle | Responsabilités |
| :--- | :--- |
| **Contributeur** | Signer le NDA, respecter la confidentialité, coder selon les standards, signaler les failles. |
| **Mainteneur** | Valider les contributions, fusionner le code, garantir la cohérence architecturale. |
| **Auditeur Éthique** | Vérifier la conformité religieuse (Charia) et légale (FINMA/LPD) avant déploiement. |

---

## 4. Standards de Codage (Le "Juste Milieu")

Nous appliquons la règle de l'**Al-Wasatiyyah** (équilibre) dans le code : ni complexité inutile, ni laxisme.

*   **Clarté** : Code commenté, lisible, noms de variables explicites (pas d'ambiguïté).
*   **Sécurité** :
    *   Aucune donnée sensible (clés API, mots de passe) ne doit être committée (voir [.gitignore](../.gitignore)).
    *   Chiffrement systématique des données sensibles.
*   **Esthétique** : Respect strict des conventions de style (indentation, structure) pour une maintenance pérenne.
*   **Performance & Écologie** : Code optimisé pour minimiser la consommation énergétique (alignement avec la politique écologique d'Infomaniak).

---

## 5. Signalement des Failles (Bug Bounty Éthique)

La sécurité est une obligation religieuse (*Amânah*).

*   **Canal Unique** : Toute faille doit être signalée via le fichier [SECURITY.md](../SECURITY.md) ou à `security@ced-halaltech.ch`.
*   **Interdiction Formelle** : Toute exploitation, test intrusif non autorisé, ou divulgation publique avant résolution est passible de poursuites légales immédiates.
*   **Récompense** : Les contributeurs identifiant des failles critiques de bonne foi recevront un **Certificat de Contribution Éthique** et une reconnaissance publique (si souhaité).

---

## 6. Droits et Devoirs Juridiques

*   **Cession de Droits** : En soumettant une contribution, vous cédez vos droits patrimoniaux à CED HalalTech™. Vous conservez vos droits moraux (paternité).
*   **Usage Commercial** : Toute utilisation du code modifié à des fins commerciales sans accord écrit est interdite.
*   **Loi Applicable** : Tout litige relatif à une contribution est soumis au droit suisse et à la compétence des tribunaux de Genève.

---

> **"Allah vous ordonne de rendre les dépôts à leurs ayants droit." (Sourate 4:58)**
>
> En contribuant, vous devenez dépositaire de la confiance de la Oumma et des utilisateurs de CED HalalTech™.

**Signé :** Yamina Yakoubi, Architecte Fondatrice  
**Contact :** direction@ced-halaltech.ch
