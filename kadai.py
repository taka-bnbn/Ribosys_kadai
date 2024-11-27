import sys

def calculate_take_home_salary(gross_income):
    """
    年収から手取りを計算
    - 社会保険料、所得税、住民税を考慮
    """
    # 社会保険料（約15%）
    social_insurance = gross_income * 0.15

    # 課税所得を計算
    taxable_income = gross_income - social_insurance - 480000
    taxable_income = max(taxable_income, 0)  # 負の値をゼロに補正

    # 所得税（累進課税）
    if taxable_income <= 1950000:
        income_tax = taxable_income * 0.05
    elif taxable_income <= 3300000:
        income_tax = taxable_income * 0.10 - 97500
    elif taxable_income <= 6950000:
        income_tax = taxable_income * 0.20 - 427500
    elif taxable_income <= 9000000:
        income_tax = taxable_income * 0.23 - 636000
    elif taxable_income <= 18000000:
        income_tax = taxable_income * 0.33 - 1536000
    elif taxable_income <= 40000000:
        income_tax = taxable_income * 0.40 - 2796000
    else:
        income_tax = taxable_income * 0.45 - 4796000

    # 住民税（約10%）
    resident_tax = taxable_income * 0.10

    # 手取り額
    take_home = gross_income - social_insurance - income_tax - resident_tax

    return round(take_home, 2)


def main():
    # コマンドライン引数から年収を取得
    if len(sys.argv) != 2:
        print("使い方: python kadai.py [年収]")
        sys.exit(1)

    try:
        annual_income = int(sys.argv[1])
        if annual_income < 0:
            raise ValueError("年収は正の数である必要があります。")
    except ValueError as e:
        print(f"入力エラー: {e}")
        sys.exit(1)

    take_home_salary = calculate_take_home_salary(annual_income)
    byebyemoney = annual_income - take_home_salary

    print(f"年収 {annual_income:,.0f} 円の場合，手取りは約 {take_home_salary:,.0f} 円です．")
    print(f"{byebyemoney:,.0f} 円は国の下へ去りました．")


if __name__ == "__main__":
    main()

