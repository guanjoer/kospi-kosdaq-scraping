import csv
import json
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y_%m_%d")

def csv_to_json(csv_f, json_f):
    with open(csv_f, mode='r', encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f)
        data = [row for row in csv_reader]

    with open(json_f, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)  # ensure_ascii=False로 한글 출력

    print(f"CSV to JSON conversion completed! {json_f}")

csv_to_json(f'public_companies_{formatted_date}.csv', f'data_{formatted_date}.json')
