def main():
    book_path  = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_characters = count_char(text)
    list_dict_count_characters = [{"char":k, "num":v} for k, v in count_characters.items()]
    list_dict_count_characters.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("\n")
    # Filter only alphabet
    for character in list_dict_count_characters:
        if character["char"].isalpha():
            print(f"The '{character['char']}' character was found {character['num']} times")
    print("--- End report ---")
    
def sort_on(dict):
    return dict["num"]

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

