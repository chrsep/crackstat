import json
from time import sleep
from urllib.request import Request, urlopen

page = 0
all_games = []

while 1==1:
    crackwatch_page = Request('https://api.crackwatch.com/api/games?page='+str(page), headers={'User-Agent': 'Mozilla/5.0'})
    loaded_page = urlopen(crackwatch_page).read()
    parsed_data = json.loads(loaded_page)
    if len(parsed_data) == 0:
        break
    all_games += parsed_data
    page = page + 1


filename = 'allgames.json'
myfile = open(filename, 'a')
myfile.write(json.dumps(all_games, indent=4, sort_keys=True))
myfile.close()

with open(filename) as file:
    contents = file.read()
    count_games = contents.count('title')
print(count_games)