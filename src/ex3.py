import csv

def count_words(input_file):
    set_of_words = set()

    with open(input_file) as csv_file:
        rows = csv.reader(csv_file, delimiter=' ')
        for row in rows:
            set_of_words.update(row)

    set_of_words.remove('')
    small_words = set(filter(lambda w: len(w) < 3, set_of_words))
    large_words = set(set_of_words.difference(small_words))

    with open("files/large-words.txt", mode='w') as csv_file:
        large_writer = csv.writer(csv_file, delimiter='\n')
        large_writer.writerows([large_words])

    with open("files/small-words.txt", mode='w') as csv_file:
        small_writer = csv.writer(csv_file, delimiter='\n')
        small_writer.writerows([small_words])
    
    return len(set_of_words)

def ex3():
    total_words = count_words("files/words.txt")
    print(f"Total words: {total_words}.")