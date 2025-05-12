
import sys
from stats import count_words, count_chars, sort_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(filepath):
    file_contents = get_book_text(filepath)

    num_words = count_words(file_contents)
    print(f"Found {num_words} total words")

    char_counts = count_chars(file_contents)
    sorted_chars = sort_char(char_counts)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        main(filepath)


