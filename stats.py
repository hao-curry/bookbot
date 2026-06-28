def num_of_words(text: str) -> int:
    return len(text.split())


def get_counted_chars(text: str) -> dict[str, int]:
    char_count: dict[str, int] = {}
    for letter in text.lower():
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count
