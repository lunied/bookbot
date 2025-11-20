import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list
from stats import print_report

def get_book_text(book):
    with open(book) as b:
        return b.read()
    
def sys_argcheck(args):
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main_py = sys.argv[0]
    book_path = sys.argv[1]
    return [main_py, book_path]

def main():
    [main_py, book_path] = sys_argcheck(sys.argv)
    book_text = get_book_text(book_path)
    print_report(book_path, book_text)

main()