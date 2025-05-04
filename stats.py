def get_num_words(book) -> int:
    return len(book.split())

def count_characters(book):
    char_count = {}
    lower = book.lower()

    for char in lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def get_sorted_char_list(char_dict):
    result = [{"char": key, "num": value} for key, value in char_dict.items()]
    result.sort(key=lambda x: x["num"], reverse=True)
    return result
