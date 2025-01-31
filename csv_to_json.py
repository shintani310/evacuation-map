import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, "r", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        print(f"CSVのヘッダー: {reader.fieldnames}")  # ヘッダーを表示
        for row in reader:
            print(f"行データ: {row}")  # 各行のデータを表示

            # 緯度と経度が空の場合の処理
            if not row["緯度"] or not row["経度"]:
                print(f"警告: 緯度または経度が空です。スキップします: {row}")
                continue  # 空の行をスキップ

            try:
                data.append({
                    "name": row["名前"].strip(),
                    "address": row["住所"].strip(),
                    "lat": float(row["緯度"]),
                    "lng": float(row["経度"])
                })
            except ValueError as e:
                print(f"エラー: 緯度または経度が不正な値です。スキップします: {row}")
                continue

    with open(json_file, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

# 入力CSVファイルと出力JSONファイルのパスを指定
csv_file = "/Users/shintanitakaaki/Desktop/Python/shelters_with_coordinates.csv"
json_file = "/Users/shintanitakaaki/Desktop/Python/shelters.json"

# 関数を呼び出して変換を実行
csv_to_json(csv_file, json_file)
print(f"JSONファイルが作成されました: {json_file}")