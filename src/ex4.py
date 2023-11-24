import boto3, csv
from botocore.exceptions import ClientError

def calculate():
    with open("files/calculator-log.txt", 'w', newline='') as csv_file:
        log_writer = csv.writer(csv_file)

        while (True):
            num1 = input("Enter the first number: ")
            if num1 == 'q': break
            num2 = input("Enter the second number: ")
            if num2 == 'q': break
            result = f"{num1} + {num2} = {int(num1)+int(num2)}"
            print(result)
            log_writer.writerow([result])
    
    # now that the file is created, it would be uploaded to the S3 bucket here

def ex4():
    calculate()