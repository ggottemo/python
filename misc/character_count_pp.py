import pprint
def characterCount(message):
    count = {}

    for character in message:
        count.setdefault(character,0)
        count[character] = count[character]+1

    return count

message = "This is a test message"

pprint.pprint(characterCount(message))
