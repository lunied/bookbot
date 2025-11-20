from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list

def get_path_from_pathfile():
    with open("./pathfile.txt") as path:
        return path.read()


def get_book_text(book):
    with open(book) as b:
        return b.read()

def main():
    book_path = get_path_from_pathfile()
    book_text = get_book_text(book_path)
    print(sorted_list(get_num_characters(book_text)))

main()