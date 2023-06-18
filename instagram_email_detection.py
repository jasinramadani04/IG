import requests
import re

def find_email(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        biography = data["graphql"]["user"]["biography"]
        email_match = re.search(r'[\w\.-]+@[\w\.-]+', biography)
        if email_match:
            email = email_match.group(0)
            print(f"Email adresa e llogarisë: {email}")
        else:
            print("Nuk është gjetur adresë email për këtë llogari.")
    else:
        print("Llogaria nuk u gjet. Provoni një emër përdoruesi të vlefshëm.")

# Përdorimi i funksionit për të gjetur adresën e email-it të llogarisë
username = "erjon_merdita"
find_email(username)
