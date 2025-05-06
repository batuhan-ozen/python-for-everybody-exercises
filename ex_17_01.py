import urllib.request, urllib.parse, json

def get_plus_code(location):
    base_url = "http://py4e-data.dr-chuck.net/opengeo?"
    params = {"q": location.strip("\"")}
    url = base_url + urllib.parse.urlencode(params)
    
    print(f"Retrieving {url}")
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
    
    print(f"Retrieved {len(data)} characters")
    
    try:
        js = json.loads(data)
        print("JSON Response:", json.dumps(js, indent=2))  # Print the JSON response
    except json.JSONDecodeError:
        print("Failed to parse JSON")
        return None
    
    if "plus_code" in js:
        return js["plus_code"]
    elif "results" in js and len(js["results"]) > 0 and "plus_code" in js["results"][0]:
        return js["results"][0]["plus_code"]
    else:
        print("No plus_code found in response")
        return None

if __name__ == "__main__":
    location = input("Enter location: ")
    plus_code = get_plus_code(location)
    if plus_code:
        print(f"Plus code {plus_code}")
