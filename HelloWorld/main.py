# Functions should be lowercase with words separated by underscores as necessary to improve readbility
## Variable names follow the same convention as fucntion names

def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', '1897', '4.01'

    print(f' {book} is a novel by  {author}, published in {release_year}. It has a rating of {goodreads_rating} on goodreads.')

if __name__ == '__main__':
    main()
# Dracula
# Bram Stoker
# 1897
# 4.01