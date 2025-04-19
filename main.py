from stats import num_words, num_chars, sorted_count_list
import sys


def get_book_text(filepath):
  with open(filepath) as book:
    file_contents = book.read()
  return file_contents

def main():
  if len(sys.argv) == 2:
    pathoffile = sys.argv[1]
    text = get_book_text(pathoffile)
    words = num_words(text)
    chars = num_chars(text)
    sorted_list = sorted_count_list(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {pathoffile}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print(f"--------- Character Count -------")
    count = 0
    for items in sorted_list:
      if sorted_list[count]["character"].isalpha():
        print(f"{sorted_list[count]['character']}: {sorted_list[count]['count']}")
      count +=1
    print(f"============= END ===============")
  else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


main()
