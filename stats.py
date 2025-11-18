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
    print(character_dictionary)