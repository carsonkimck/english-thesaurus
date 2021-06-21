import json
from difflib import get_close_matches


content = json.load(open("data.json"))

def getVal(key):

    if key.capitalize() in content: 
            return content[key.capitalize()]

    if key.upper() in content:
            return content[key.upper()]

    key = key.lower()

    if key in content:
        return content[key]

    elif len(get_close_matches(key, content.keys())) > 0:
        similar_match = get_close_matches(key, content.keys())[0]
        print("Did you mean %s instead?" % similar_match)
        confirm = input("Enter Y for yes, N for no: ")
        if confirm.lower() == 'y':
            return content[similar_match]
        elif confirm.lower() == 'n':
            return "This word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "This word does not exist. Please double check it."


try:
    while True:
        key = input("Enter word: ")
        output = getVal(key)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

except KeyboardInterrupt:
        print("goodbye!")