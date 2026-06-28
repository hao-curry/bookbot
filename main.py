def get_book_text(path: str) -> str:
    with open(path) as file:
        return file.read()


def main() -> None:
    print(get_book_text("books/frankenstein.txt"))


if __name__ == '__main__':
    main()
