import requests

base_url = 'http://localhost:8000'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

def get_players():

    url = "https://jsonplaceholder.typicode.com/posts/1"
    #print('Getting all players...')
    resp = requests.get(url, headers=HEADERS)
    #print(resp)
    data = resp.json()
    #print(data)


for i in range(100):
    get_players()