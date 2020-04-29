import csv
with open('birnen.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\tcol 0: {row["col0"]}, col1: {row["x"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')
