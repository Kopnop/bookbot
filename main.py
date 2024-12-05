def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")
    char_dict = count_chars(text)
    #print()
    print_chars(char_dict)
    print("--- End report ---")

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["value"]

def print_chars(chars):
    my_list = []
    for x in chars:
        if x.isalpha():
            my_list.append({"char": x, "value":chars[x]})
    my_list.sort(reverse=True, key=sort_on)
    #print(my_list)
    for x in my_list:
        print(f"The '{x["char"]}' character was found {x["value"]} times")
    pass

def count_chars(text):
    count_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in count_dict:
            count_dict[char] += 1 
        else:
            count_dict[char] = 1
    return count_dict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
