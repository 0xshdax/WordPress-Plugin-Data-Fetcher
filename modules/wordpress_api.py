import requests

def fetch_plugin_data(page):
    api_endpoint = 'https://api.wordpress.org/plugins/info/1.2/'
    payload = {
        'action': 'query_plugins',
        'request[page]': str(page),
        'request[per_page]': '100'
    }

    response = requests.get(api_endpoint, params=payload)
    return response.json()
