def get_num_words(content):
    return (f"Found {len(content.split())} total words")

def get_num_chars(content):
    char_letter = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    char_dict = {char: 0 for char in char_letter}
    for c in content.lower():
        if c in char_dict:
            char_dict[c] += 1
    return char_dict
def sort_on(items):
    return items[num]
def sort_dict(dictionary):
    sorted_list = list(dictionary.items())
    sorted_list.sort(reverse=True, key=lambda x:x[1])
    return sorted_list
