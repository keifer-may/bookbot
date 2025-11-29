import sys
from stats import get_num_words, count_chars

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)


    path = sys.argv[1]
    book_text = get_book_text(path)
    book_word_count = get_num_words(book_text)
    char_count = count_chars(book_text)

    ##print(f'Found {book_word_count} total words')
    ##print(char_count)
    
    report_text = f'''============ BOOKBOT ============\n
Analyzing book found at {path}...\n
----------- Word Count ----------\n
Found {book_word_count} total words\n
--------- Character Count -------\n'''
    
    for char in char_count.keys():
        report_text += f'{char}: {char_count[char]}\n'

    report_text += '============= END ==============='

    print(report_text)
        


main()



