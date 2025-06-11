from stats import get_word_count, get_char_count, sort_word_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    print(sys)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return

    print(sys.argv)
    file_contents = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file_contents)} total words")
    print("--------- Character Count -------")
    sort_word_count_list = sort_word_count(get_char_count(file_contents))

    for char_dict in sort_word_count_list:
        print(f"{char_dict['char']}: {char_dict['num']}")
    
main()

