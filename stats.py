def get_word_count(book_text):
    # filtered_text = ""
    # for text in book_text.split():
    #     # print(f"text: {text}")
    #     for char in text:
    #         # print(f"char: {char}")
    #         if (char.isalnum() or char == "-"):
    #             filtered_text += char
    #         elif (char == "’" or char == "."):
    #             filtered_text += ""
    #         else:
    #             filtered_text += " "
    #     filtered_text += " "
    #     # print(f"Filtered text: {filtered_text}")

    # # print(f"Filtered word count {len(filtered_text.split())}")
    # # print(f"Filtered text: {filtered_text.split()}")
    # print(f"Book text string[]: {book_text.split()}")
    return len(book_text.split())


def get_char_count(book_text):
    char_counter = {}

    for char in book_text:
        # print(f"Current char and its type: {char} is {type(char)}")
        if char.lower() not in char_counter:
            char_counter[char.lower()] = 1
        else:
            char_counter[char.lower()] += 1  

    return char_counter

def sort_on(dict):
    return dict["num"]

def sort_word_count(char_dict):
    char_count_list = []

    for key, value in char_dict.items():
        if key.isalpha():
            char_count_list.append({"char":key, "num":value})

    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list



