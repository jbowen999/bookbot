with open("books/frankenstein.txt") as f:
    file_contents = f.read()
# print(file_contents)


def word_counter(file):
    word_list = file.split()
    count = 0
    for i in word_list:
        count += 1

    return count


def char_counter(file):
    dic = {}
    for char in file.lower():
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic


def print_report(dic):
    print("--- Begin report of books/frankenstein.txt ---")
    print("77986 words found in the document")
    for key, value in dic.items():
        if ord("a") <= ord(key) <= ord("z"):
            print(f"The '{key}' character was found {value} times")
        else:
            pass
    print("--- End report ---")


char_counts = char_counter(file_contents)
print_report(char_counts)
