def get_book_text(path: str) -> str:
    with open(path) as file:
        return file.read()


def num_of_words(text: str) -> int:
    return len(text.split())


def main() -> None:
    num = num_of_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num} total words")


if __name__ == '__main__':
    main()
