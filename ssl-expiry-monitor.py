import ssl
import socket
import datetime
import requests

# --- Config ---
DOMAINS = [
    "google.com", 
    "github.com", 
    "ton-domaine.fr"
]
ALERT_DAYS = 30
WEBHOOK_URL = "TON_LIEN_WEBHOOK_ICI" 

def get_ssl_expiry(domain):
    # Recupere les infos du certificat
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
    conn.settimeout(5.0)
    
    try:
        conn.connect((domain, 443))
        ssl_info = conn.getpeercert()
        
        if not ssl_info or 'notAfter' not in ssl_info:
            return None
            
        expire_date = datetime.datetime.strptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
        days_left = (expire_date - datetime.datetime.utcnow()).days
        return days_left
        
    except Exception as e:
        print(f"[ERROR] Connexion echouee pour {domain}: {e}")
        return None
    finally:
        conn.close()

def notify_webhook(msg):
    # Envoi de l'alerte vers Teams/Slack
    if WEBHOOK_URL != "TON_LIEN_WEBHOOK_ICI":
        try:
            requests.post(WEBHOOK_URL, json={"text": msg}, timeout=5)
        except Exception as e:
            print(f"[ERROR] Webhook HS : {e}")
    print(f"[ALERT] {msg}")

if __name__ == "__main__":
    print("[INFO] Lancement du check SSL...")
    
    for domain in DOMAINS:
        days = get_ssl_expiry(domain)
        
        if days is not None:
            if days < ALERT_DAYS:
                notify_webhook(f"Certificat SSL pour {domain} expire dans {days} jours.")
            else:
                print(f"[OK] {domain} : {days} jours restants.")