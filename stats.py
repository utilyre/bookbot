def count_words(string):
    words = string.split()
    return len(words)

def count_each_char(string):
    num_chars = {}
    for char in string:
        char = char.lower()
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_num_chars(num_chars):
    list = [(char, count) for char, count in num_chars.items()]
    list.sort(key=lambda tup : tup[1], reverse=True)
    return list
