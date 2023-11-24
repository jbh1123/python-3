import csv

def find_total_visits():
    total = 0
    for file in ("files/week-1.csv", "files/week-2.csv", "files/week-3.csv"):
        with open(file) as csv_file:
            rows = list(csv.reader(csv_file, delimiter=','))
            for row in rows[1:]:
                total += len(list(filter(lambda s: s.strip() == '1', row)))
    return total


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")