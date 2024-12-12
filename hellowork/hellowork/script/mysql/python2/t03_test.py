import csv

csv_file = 'top10.csv'

with open(csv_file, 'r', encoding='shift-jis') as file:
    reader = csv.reader(file, delimiter=',')  # デフォルトはカンマ
    headers = next(reader)
    print(f"Headers: {headers} {len(headers)} columns")
