import requests

def get_joke(category="Any"):
    """
    Fetch a joke using JokeAPI.
    """

    url = f"https://v2.jokeapi.dev/joke/{category}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Couldn't fetch a joke."

    data = response.json()

    if data["type"] == "single":
        return data["joke"]

    return f"{data['setup']}\n\n{data['delivery']}"