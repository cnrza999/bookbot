def main():
    book_path  = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_characters = count_char(text)
    print(f"{num_words} words found in the document")
    print(f"{count_characters}")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_char(text):
    lower_char = text.lower()
    characters = {}
    for char in lower_char:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

if __name__ == "__main__":
    main()

