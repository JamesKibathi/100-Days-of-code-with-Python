import requests
response = requests.get('https://api.github.com/users/JamesKibathi/repos')

json_response = response.json()

print(json_response[0])

for project in json_response:
    print(f"Project Name: {project['name']}\n URL: {project['full_name']}\n")

# print(response.json())