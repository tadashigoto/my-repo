import pandas as pd

# データの作成
data = [
    ["令和6年1月11日", "東京高輪病院", 220, ""],
    ["令和6年1月12日", "東京高輪病院", 5850, ""],
    ["令和6年1月18日", "慶應義塾大学病院", 3890, ""],
    ["令和6年1月31日", "慶應義塾大学病院", 3550, ""],
    ["令和6年2月6日", "慶應義塾大学病院", 153920, "入院診療"],
    ["令和6年2月7日", "慶應義塾大学病院", 2180, ""],
    ["令和6年2月13日", "西新宿調剤薬局", 1030, "薬局のため優先"],
    ["令和6年2月20日", "慶應義塾大学病院", 152610, "入院診療"],
    ["令和6年2月27日", "慶應義塾大学病院", 1180, ""],
    ["令和6年3月18日", "渡辺クリニック", 4880, ""],
    ["令和6年4月16日", "渡辺クリニック", 6720, ""],
    ["令和6年5月7日", "西新宿調剤薬局", 1240, "薬局のため優先"],
    ["令和6年5月9日", "ハラダ薬局西新宿店", 890, "薬局のため優先"],
    ["令和6年5月9日", "西新宿メンタルクリニック", 1830, ""],
    ["令和6年5月14日", "西新宿メンタルクリニック", 3330, ""],
    ["令和6年5月14日", "西新宿メンタルクリニック", 220, "診察券再発行代として"],
    ["令和6年5月17日", "西新宿調剤薬局", 990, "薬局のため優先"],
    ["令和6年5月17日", "春山記念病院", 430, ""],
    ["令和6年5月17日", "渡辺クリニック", 4820, ""],
    ["令和6年5月30日", "西新宿メンタルクリニック", 1430, ""],
    ["令和6年6月4日", "西新宿メンタルクリニック", 1950, ""],
    ["令和6年6月7日", "田口歯科医院", 3830, ""],
    ["令和6年6月13日", "渡辺クリニック", 4670, ""],
    ["令和6年6月20日", "メディカルスキャニング新宿", 7880, ""],
    ["令和6年6月25日", "初音整形外科クリニック", 380, ""],
    ["令和6年6月29日", "不動薬局", 1190, "薬局のため優先"],
    ["令和6年6月29日", "初音整形外科クリニック", 560, ""],
]

# DataFrameの作成
df = pd.DataFrame(data, columns=["日付", "病院名 / 薬局名", "金額", "備考"])

# Excelファイルとして保存
df.to_excel("medical_expenses.xlsx", index=False)

# Excelファイルのダウンロードリンク作成
print("medical_expenses.xlsx ファイルが作成されました。")
