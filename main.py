def get_word_count(file_contents):
    count = 0
    for line in file_contents.split('\n'):
        count += len(line.split())
    return count

def get_character_count(file_contents):
    counts = {}
    for line in file_contents.split('\n'):
        for word in line.split():
            for char in word.lower():
                if char in counts.keys():
                    counts[char] += 1
                else:
                    counts[char] = 1
    return counts

def gen_report(book_name, word_count, character_count):
    print(f'--- Begin report of {book_name} ---')
    print(f'{word_count} words found in the document')
    print('')
    sorted_character_count = sorted(character_count, key=character_count.get, reverse=True)
    for k in sorted_character_count:
        if k.isalpha():
            print(f'The \'{k}\' character was found {character_count[k]} times')
    print('--- End report ---')


def main():
    file_path='books/frankenstein.txt'
    with open(file_path) as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        character_count = get_character_count(file_contents)
    gen_report(file_path, word_count, character_count)

if __name__ == '__main__':
    main()