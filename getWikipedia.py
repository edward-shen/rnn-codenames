import requests
import json
import re#eeeeeeeeeeeeeeeeeeeeeee

# Fetches our data
wikiDataUrl = "https://en.wikipedia.org/w/api.php?action=parse&page=List_of_computer_technology_code_names&srlimit=1&format=json"
wikiDataR = requests.get(wikiDataUrl)

# Parse our data
wikiData = json.loads(wikiDataR.text)["parse"]["text"]["*"]

with open('./customData.txt') as f:
    lines = f.read().splitlines()

# Creates our regex filter for titles
getTitles = re.compile('<b>(.*)<\/b>')
checkNotClean = re.compile('<a(.*)>(.*)<\/a(.*)>')


# Removes any html tag that surrond the values
def clean(input):
    if checkNotClean.match(input):
        input = input.split(">", 1)[1]
        input = input.split("<", 1)[0]
        return input
    else:
        return input

# Parse our titles into a list
wikiData = getTitles.findall(wikiData)

# clean up our data
wikiData = list(map(clean, wikiData))
# The last two values are "^"
wikiData = wikiData[:-2] + lines
output = open("char-rnn-tensorflow-master/data/codenames/input.txt", "w")
print(wikiData)
for item in wikiData:
  output.write("%s\n" % item)
