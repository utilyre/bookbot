def count_words(string):
    words = string.split()
    return len(words)

def count_individual_chars(string):
    char_counts = {}
    for char in string:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def prettify_char_counts(num_chars):
    list = [(char, count) for char, count in num_chars.items()]
    list.sort(key=lambda tup : tup[1], reverse=True)
    return list
