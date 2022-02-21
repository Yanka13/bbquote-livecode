import requests

def get_quote():
    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
    result = requests.get(url)
    response = result.json()[0]
    return f"{response['author']} says : {response['quote']}"


#print(get_quote())
