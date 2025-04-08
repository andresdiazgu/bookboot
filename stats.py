def num_words(text):
    words = text.split()
    count = 0
    for x in words:
        count += 1
    return count

def letters_count(text):
    dictionary = {}
    for x in text:
        x = x.lower()
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary

def sort_chars(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)

    def sort_on(dict):
        return dict["count"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
   
