def get_num_words(text):
    return len(text.split())

def count_characters(text):
    lookup = dict()
    for char in text:
        val = char.lower()
        if val not in lookup:
            lookup[val] =0
        lookup[val]+=1
    return lookup


def sort_on(val):
    return val["num"]

def get_character_dict(character_dict):
    sorted = []
    for key in character_dict:
        val = character_dict[key]
        if key.isalpha():
            sorted.append({ "char":key, "num": val})
    sorted.sort(reverse=True, key=sort_on)
    return sorted