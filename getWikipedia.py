import json
import re#eeeeeeeeeeeeeeeeeeeeeee

import requests

# Fetches our data
wikipediaBase = "https://en.wikipedia.org/w/api.php?"
wikipediaParams = "action=parse&srlimit=1&format=json&page="
wikipediaPageName = "List_of_computer_technology_code_names"
wikiDataUrl = wikipediaBase + wikipediaParams + wikipediaPageName
wikiDataR = requests.get(wikiDataUrl)

# Parse our data
wikiData = json.loads(wikiDataR.text)["parse"]["text"]["*"]

# Read custom imput
with open('./customData.txt') as f:
    customData = f.read().splitlines()

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
wikiData = wikiData[:-2] # The last two values are "^"

# Merge custom with scraped data
unified = wikiData + customData


print(unified)
print("Number of entries: " + str(len(unified)) + " (Scaped: " + str(len(wikiData)) + ", Custom: " + str(len(customData)) + ")")

output = open("char-rnn-tensorflow-master/data/codenames/input.txt", "w")
for item in unified:
    output.write("%s\n" % item)
