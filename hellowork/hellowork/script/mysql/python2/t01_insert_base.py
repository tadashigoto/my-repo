import csv
import pymysql
import re

# MySQL接続情報
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0371',
    'database': 'hellowork',
    'port': 3306
}

# SQLスキーマから型情報を取得
def parse_sql_schema(file_path):
    column_types = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r"`(\w+)`\s+(\w+)", line)
            if match:
                column_name = match.group(1)
                column_type = match.group(2).lower()
                column_types[column_name] = column_type
    return column_types

# 型変換
def convert_value(value, data_type):
    if 'int' in data_type:
        return int(value) if value and value.isdigit() else None
    else:
        return value.strip() if value else None

# データ挿入
def insert_data_to_mysql(csv_file, db_config):
    try:
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            port=db_config['port']
        )
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        return

    INSERT_SQL = """
    INSERT INTO BaseTable (
        kjno,                 -- 12: 求人番号
        uktkymd_seireki,      -- 14: 受付年月日（西暦）
        uktkymd_wareki,       -- 15: 受付年月日（和暦）
        kjyukoymd,            -- 16: 求人有効年月日（西暦）
        shokaikigenymd,       -- 17: 紹介期限日（和暦）
        kjkbn1_c,             -- 18: 求人区分１（コード）
        kjkbn1_n,             -- 19: 求人区分１
        kjkbn2_c,             -- 20: 求人区分２（コード）
        kjkbn2_n,             -- 21: 求人区分２
        kjkbn_title,          -- 22: 求人区分（求人票タイトル）
        kokaikibo,            -- 23: 公開希望
        sgsyakbn_c,           -- 24: 障害者区分（コード）
        sgsyakbn_n,           -- 25: 障害者区分
        srkzksien_agtjigyo_c, -- 26: 就労継続支援Ａ型事業の利用者募集（コード）
        srkzksien_agtjigyo_n, -- 27: 就労継続支援Ａ型事業の利用者募集
        trialkoyoheiyo_kibo_c,-- 28: トライアル雇用併用の希望（コード）
        trialkoyoheiyo_kibo_n,-- 29: トライアル雇用併用の希望
        onlinejishuobo_uktkkahi_c, -- 30: オンライン自主応募の受付可否（コード）
        onlinejishuobo_uktkkahi_n, -- 31: オンライン自主応募の受付可否
        sngbrui_c,            -- 48: 産業分類（コード）
        sngbrui_dai_c,        -- 49: 産業分類（大分類コード）
        sngbrui_n,            -- 50: 産業分類（名称）
        skbtrn1,              -- 418: 識別欄１
        skbtrn2,              -- 419: 識別欄２
        skbtrn3,              -- 420: 識別欄３
        skbtrn4,              -- 421: 識別欄４
        skbtrn5,              -- 422: 識別欄５
        skbtrn6,              -- 423: 識別欄６
        skbtrn7,              -- 424: 識別欄７
        skbtrn8,              -- 425: 識別欄８
        skbtrn9,              -- 426: 識別欄９
        skbtrn10,             -- 427: 識別欄１０
        juriatsno,            -- 428: 受理安定所番号
        juriatsmei            -- 429: 受理安定所名
    ) VALUES (
        %s,  -- 12: 求人番号
        %s,  -- 14: 受付年月日（西暦）
        %s,  -- 15: 受付年月日（和暦）
        %s,  -- 16: 求人有効年月日（西暦）
        %s,  -- 17: 紹介期限日（和暦）
        %d,  -- 18: 求人区分１（コード）
        %s,  -- 19: 求人区分１
        %d,  -- 20: 求人区分２（コード）
        %s,  -- 21: 求人区分２
        %s,  -- 22: 求人区分（求人票タイトル）
        %d,  -- 23: 公開希望
        %d,  -- 24: 障害者区分（コード）
        %s,  -- 25: 障害者区分
        %s,  -- 26: 就労継続支援Ａ型事業の利用者募集（コード）
        %s,  -- 27: 就労継続支援Ａ型事業の利用者募集
        %d,  -- 28: トライアル雇用併用の希望（コード）
        %s,  -- 29: トライアル雇用併用の希望
        %d,  -- 30: オンライン自主応募の受付可否（コード）
        %s,  -- 31: オンライン自主応募の受付可否
        %d,  -- 48: 産業分類（コード）
        %s,  -- 49: 産業分類（大分類コード）
        %s,  -- 50: 産業分類（名称）
        %s,  -- 418: 識別欄１
        %s,  -- 419: 識別欄２
        %s,  -- 420: 識別欄３
        %s,  -- 421: 識別欄４
        %s,  -- 422: 識別欄５
        %s,  -- 423: 識別欄６
        %s,  -- 424: 識別欄７
        %s,  -- 425: 識別欄８
        %s,  -- 426: 識別欄９
        %s,  -- 427: 識別欄１０
        %d,  -- 428: 受理安定所番号
        %s   -- 429: 受理安定所名
    )
    """
    try:
        with open(csv_file, 'r', encoding='shift-jis') as file:
            reader = csv.reader(file)
            next(reader)
            with connection.cursor() as cursor:
                for row in reader:
                    try:
                        values = [
                            convert_value(row[12 - 12], column_types['kjno']),  # 12: 求人番号
                            convert_value(row[14 - 12], column_types['uktkymd_seireki']),  # 14: 受付年月日（西暦）
                            convert_value(row[15 - 12], column_types['uktkymd_wareki']),  # 15: 受付年月日（和暦）
                            convert_value(row[16 - 12], column_types['kjyukoymd']),  # 16: 求人有効年月日（西暦）
                            convert_value(row[17 - 12], column_types['shokaikigenymd']),  # 17: 紹介期限日（和暦）
                            convert_value(row[18 - 12], column_types['kjkbn1_c']),  # 18: 求人区分１（コード）
                            convert_value(row[19 - 12], column_types['kjkbn1_n']),  # 19: 求人区分１
                            convert_value(row[20 - 12], column_types['kjkbn2_c']),  # 20: 求人区分２（コード）
                            convert_value(row[21 - 12], column_types['kjkbn2_n']),  # 21: 求人区分２
                            convert_value(row[22 - 12], column_types['kjkbn_title']),  # 22: 求人区分（求人票タイトル）
                            convert_value(row[23 - 12], column_types['kokaikibo']),  # 23: 公開希望
                            convert_value(row[24 - 12], column_types['sgsyakbn_c']),  # 24: 障害者区分（コード）
                            convert_value(row[25 - 12], column_types['sgsyakbn_n']),  # 25: 障害者区分
                            convert_value(row[26 - 12], column_types['srkzksien_agtjigyo_c']),  # 26: 就労継続支援Ａ型事業の利用者募集（コード）
                            convert_value(row[27 - 12], column_types['srkzksien_agtjigyo_n']),  # 27: 就労継続支援Ａ型事業の利用者募集
                            convert_value(row[28 - 12], column_types['trialkoyoheiyo_kibo_c']),  # 28: トライアル雇用併用の希望（コード）
                            convert_value(row[29 - 12], column_types['trialkoyoheiyo_kibo_n']),  # 29: トライアル雇用併用の希望
                            convert_value(row[30 - 12], column_types['onlinejishuobo_uktkkahi_c']),  # 30: オンライン自主応募の受付可否（コード）
                            convert_value(row[31 - 12], column_types['onlinejishuobo_uktkkahi_n']),  # 31: オンライン自主応募の受付可否
                            convert_value(row[48 - 12], column_types['sngbrui_c']),  # 48: 産業分類（コード）
                            convert_value(row[49 - 12], column_types['sngbrui_dai_c']),  # 49: 産業分類（大分類コード）
                            convert_value(row[50 - 12], column_types['sngbrui_n']),  # 50: 産業分類（名称）
                            convert_value(row[418 - 12], column_types['skbtrn1']),  # 418: 識別欄１
                            convert_value(row[419 - 12], column_types['skbtrn2']),  # 419: 識別欄２
                            convert_value(row[420 - 12], column_types['skbtrn3']),  # 420: 識別欄３
                            convert_value(row[421 - 12], column_types['skbtrn4']),  # 421: 識別欄４
                            convert_value(row[422 - 12], column_types['skbtrn5']),  # 422: 識別欄５
                            convert_value(row[423 - 12], column_types['skbtrn6']),  # 423: 識別欄６
                            convert_value(row[424 - 12], column_types['skbtrn7']),  # 424: 識別欄７
                            convert_value(row[425 - 12], column_types['skbtrn8']),  # 425: 識別欄８
                            convert_value(row[426 - 12], column_types['skbtrn9']),  # 426: 識別欄９
                            convert_value(row[427 - 12], column_types['skbtrn10']),  # 427: 識別欄１０
                            convert_value(row[428 - 12], column_types['juriatsno']),  # 428: 受理安定所番号
                            convert_value(row[429 - 12], column_types['juriatsmei'])  # 429: 受理安定所名
                        ]
                        cursor.execute(INSERT_SQL, values)
                    except Exception as e:
                        print(f"Error inserting row {row}: {e}")
                        continue

            connection.commit()
    except Exception as e:
        print(f"Error reading CSV file or inserting data: {e}")
    finally:
        connection.close()
# 関数の呼び出し
csv_file = 'top10.csv'
insert_data_to_mysql(csv_file, db_config)