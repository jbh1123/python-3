from ValidationException import ValidationException
import csv

def validate_file(input_file):
    with open(input_file) as csv_file:
        rows = list(csv.reader(csv_file, delimiter=','))
        for row in rows[1:]:
            if float(row[1]) % 1.0 != 0.0:
                raise ValidationException(f"Invalid mileage: {row[1]}")


def ex1():
    try:
        validate_file("files/input.txt")
    except ValidationException as ve:
        print(ve)