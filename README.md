# SSL Expiry Monitor with Webhook Alerts

Ce script Python permet aux administrateurs de surveiller l'expiration des certificats SSL d'un parc de noms de domaine et d'envoyer automatiquement une alerte vers Slack, Teams ou Discord lorsqu'un certificat est sur le point d'expirer.

## Fonctionnalités
- Vérification directe auprès du serveur cible.
- Calcul précis des jours restants avant expiration.
- Intégration Webhook pour le monitoring d'équipe (SecOps/NetOps).

## Installation
```bash
git clone [https://github.com/FilouCosmos/ssl-expiry-monitor.git](https://github.com/FilouCosmos/ssl-expiry-monitor.git)
cd ssl-expiry-monitor
pip install -r requirements.txt