from stats import get_num_words, get_num_chars, sort_dict
import sys
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    content = get_book_text(sys.argv[1])
    #print(get_num_words(content))
    char_dict = get_num_chars(content)
    sorted_list = sort_dict(char_dict)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {get_num_words(content)} total words
--------- Character Count -------
          """)
    for char, num in sorted_list:
        print(f"{char}: {num}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
