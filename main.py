from stats import count_words, count_individual_chars, prettify_char_counts

def main():
    filename = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print("Analyzing book found at {filename}...")
    content = read_file(filename)
    num_words = count_words(content)
    char_counts = prettify_char_counts(count_individual_chars(content))

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for char, count in char_counts:
        print(f"{char}: {count}")

def read_file(filename):
    with open(filename) as f:
        contents = f.read()
        return contents

main()
