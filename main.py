from stats import count_words, count_each_char

def main():
    frankenstein = get_book_text("books/frankenstein.txt")

    num_words = count_words(frankenstein)
    print(f"{num_words} words found in the document")

    num_chars = count_each_char(frankenstein)
    print(num_chars)

def get_book_text(filename):
    with open(filename) as f:
        contents = f.read()
        return contents

main()
