key="6db422d7-afc7-4a68-9919-7d62bf2272c0"
url='https://api-azure.botsonic.ai/v1/botsonic/generate'



import requests

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    'Content-Type': 'application/json',
    'User-Agent': 'python-requests/2.28.1',
    'accept': 'application/json',
    'token': key,
}

json_data = {
    'question': 'How to develop these skills?',
    'input_text':'this is done',
    'chat_history': [],
}

response = requests.post(url, headers=headers, json=json_data)
print(response.json())