from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    content = get_book_text("./books/frankenstein.txt")
    print(get_num_words(content))
if __name__ == "__main__":
    main()
