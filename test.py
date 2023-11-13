import requests
TOKEN = "5781046852:AAFOpKJJQR28gPMQE9lJQ9lXqVYx-t14D-k"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=-1"
while(1):
        message = requests.get(url).json()
        Text = message['result'][0]['message']['text']
        print(Text)
