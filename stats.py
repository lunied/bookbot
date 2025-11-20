def get_num_words(text):
    text = text.split()
    num_words = 0
    for word in text:
        num_words += 1
    print(f"Found {num_words} total words")

def get_num_characters(text):
    character_dictionary = {}
    for ch in text:
        ch = ch.lower()
        if ch not in character_dictionary:
            character_dictionary[ch] = 0
        character_dictionary[ch] += 1
    return character_dictionary

def sorted_list(ch_dict):
    ch_dict_list = []
    for key in ch_dict:
        if key.isalpha():
            dict = {}
            dict["name"] = key
            dict["num"] = ch_dict[key]
            ch_dict_list.append(dict)
    ch_dict_list.sort(reverse=True, key=sort_on)
    return ch_dict_list

def sort_on(characters):
    return characters["num"]