import sys
from stats import get_num_words,count_characters,get_character_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here
        file_contents = f.read()
        num_words= get_num_words(file_contents)
        
        chars = count_characters(file_contents)
        sorted_chars = get_character_dict(chars)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words words")
        print("--------- Character Count -------")
        for tuple in sorted_chars:
            char = tuple["char"]
            num = tuple["num"]
            print(f"{char}: {num}")
        print("============= END ===============")

        
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    get_book_text(book_path)
    
    
main()