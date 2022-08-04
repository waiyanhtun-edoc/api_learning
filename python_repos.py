import requests

#Make call api

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

respons_dict = r.json()

print(respons_dict.keys())

print(f"Total repostries: {respons_dict['total_count']}")

repo_dicts = respons_dict['items']
print(f"Reporitied Return : {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKey : {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key)