def get_num_words(file_content):
    return len(file_content.split())

def get_char_frequency(file_content):
    char_freq = {}
    file_content = file_content.lower()
    for char in file_content:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def sort_on(items):
    return items["num"]

def get_sorted_char_list(char_dict):
    char_list = [] 
    for char in char_dict:
        counts = char_dict[char]
        char_list.append({"char": char, "num": counts})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
