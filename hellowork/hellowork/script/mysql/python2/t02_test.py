import csv

csv_file = 'top10.csv'
error_log = 'error_log.txt'

with open(csv_file, 'r', encoding='shift-jis') as file:
    reader = csv.reader(file)
    headers = next(reader)
    expected_columns = len(headers)

    with open(error_log, 'w', encoding='utf-8') as log:
        for line_number, row in enumerate(reader, start=2):  # ヘッダーが1行目なので2行目から
            if len(row) != expected_columns:
                log.write(f"Line {line_number}: Column count mismatch. Expected {expected_columns}, got {len(row)}\n")
