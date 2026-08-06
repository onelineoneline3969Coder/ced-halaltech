# Politique de Sécurité (Security Policy)

## 🛡️ Engagement de Souveraineté et d'Éthique (Amanah)
Chez CED HalalTech, la sécurité est un devoir éthique (*Amanah*) avant d'être une contrainte technique. Notre infrastructure, hébergée exclusivement en Suisse chez **Infomaniak**, garantit que vos données restent sous juridiction suisse (LPD/RGPD), à l'abri de toute ingérence extraterritoriale (CLOUD Act).

Notre approche du **Juste Milieu** (*Al-Wasatiyyah*) s'applique à la sécurité : ni laxisme, ni complexité inutile, mais une protection rigoureuse, transparente et proportionnée aux risques.

## 🔒 Standards Techniques & Chiffrement
Conformément aux exigences de la FINMA et aux standards internationaux (ISO 27001), nous appliquons les mesures suivantes :

- **Chiffrement des données au repos :** AES-256 sur l'ensemble des bases de données et stockages objet.
- **Chiffrement des données en transit :** TLS 1.3 obligatoire pour toutes les communications API et web.
- **Gestion des clés :** Les clés de chiffrement sont générées, stockées et gérées exclusivement en Suisse, séparées des données.
- **Authentification :** MFA (Multi-Factor Authentication) obligatoire pour tout accès administrateur et recommandé pour les utilisateurs finaux.

## 📅 Versions Supportées
Nous maintenons activement les versions suivantes avec des mises à jour de sécurité critiques :

| Version | Supportée | Date de fin de support |
| ------- | :-------: | :--------------------- |
| 1.0.x   |     ✅    | 31 Décembre 2027       |
| < 1.0   |     ❌    | Déjà obsolète          |

## 🚨 Signaler une Vulnérabilité
La protection des données de nos utilisateurs est primordiale. Si vous découvrez une vulnérabilité, nous vous prions de la signaler de manière responsable.

**Méthode de signalement sécurisée :**
- **Email chiffré (PGP) :** security@ced-halaltech.ch (Clé publique disponible sur demande)
- **Délai de réponse initial :** 48 heures ouvrées
- **Langues acceptées :** Français, Anglais, Arabe

*Note : Conformément à l'éthique islamique, nous nous engageons à ne pas poursuivre en justice les chercheurs en sécurité agissant de bonne foi et dans le respect de la confidentialité.*

## 🔄 Procédure de Réponse aux Incidents
En cas de signalement valide, notre équipe de réponse (CSIRT) active le protocole suivant :

1.  **Confirmation (J+0 à J+2) :** Accusé de réception et validation préliminaire de la vulnérabilité.
2.  **Analyse & Correctif (J+3 à J+14) :** Investigation approfondie, développement et test interne du correctif sur l'infrastructure Infomaniak.
3.  **Déploiement (J+15 max) :** Mise en production sécurisée du correctif.
4.  **Transparence (J+20) :** Publication d'un avis de sécurité anonymisé dans le Changelog, détaillant la nature du risque et la correction apportée, sans exposer les utilisateurs.

## 📋 Processus d'Audit et de Conformité
Conformément aux standards **AAOIFI** et aux exigences de la **FINMA** :
- **Audits Externes :** Audit de sécurité complet prévu pour le **Q3 2026** par un cabinet tiers indépendant (Suisse).
- **Tests d'Intrusion :** Réalisés trimestriellement sur l'infrastructure cloud.
- **Revue de Code :** Analyse statique et dynamique automatisée intégrée dans la pipeline CI/CD.

## 🤝 Responsabilité Partagée
La sécurité est un effort conjoint. Nous nous engageons à :
- Fournir des correctifs rapides pour les vulnérabilités critiques.
- Maintenir une documentation à jour sur les meilleures pratiques.
- Traiter chaque rapport avec sérieux, respect et confidentialité.

© 2026 CED HalalTech. Hébergé en Suisse (Infomaniak). Conforme Charia & FINMA.
