def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()

        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts

def sort_on(d):
    return d["num"]

def sort_char(char_counts):
    chars = []
    for char, num in char_counts.items():
        chars.append({"char": char, "num": num})
    chars.sort(reverse=True, key=sort_on)
    return chars
