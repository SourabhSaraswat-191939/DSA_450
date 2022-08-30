import requests
# GITHUB_TOKEN= 

github_username = "Abkt2001"
URL = "https://api.github.com/orgs/OT-TRAINING/repos"

# for any username
# URL = "https://api.github.com/users/"+github_username+"/repos"

# with query like page size etc
# URL = f"https://api.github.com/orgs/OT-TRAINING/repos?order=desc&page=1&per_page=3"

response = requests.get(url = URL)

# to print the complete response 
# print(response.json())

# like if you want to print name of first repo in response.
print(response.json()[0]["name"])

