from stats import count_words

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = count_words(frankenstein)
    print(f"{num_words} words found in the document")

def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
        return contents

main()
