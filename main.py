import sys
from stats import count_words, count_character_stats, create_stat_report

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analysing book found at {file_path}")
    contents = get_book_text(file_path)
    word_count = count_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    character_stats = count_character_stats(contents)
    stat_report = create_stat_report(character_stats)
    print("----------- Word Count ----------")
    for row in stat_report:
        char = row["char"]
        count = row["count"]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
