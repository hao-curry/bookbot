from stats import num_of_words, get_counted_chars


def get_book_text(path: str) -> str:
    with open(path) as file:
        return file.read()


def main() -> None:
    frankenstein = get_book_text("books/frankenstein.txt")
    num = num_of_words(frankenstein)
    char_count = get_counted_chars(frankenstein)
    print(f"Found {num} total words")
    print(char_count)


if __name__ == '__main__':
    main()
