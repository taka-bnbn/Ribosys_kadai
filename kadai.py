import sys

def calculate_take_home_salary(gross_income):
    """
    年収から手取りを計算する関数
    - 所得税、住民税、社会保険料を考慮
    """
    # 社会保険料（約15%）を計算
    social_insurance = gross_income * 0.15

    # 課税所得 = 年収 - 社会保険料 - 基礎控除（48万円）
    taxable_income = gross_income - social_insurance - 480000
    if taxable_income < 0:
        taxable_income = 0

    # 所得税（簡略計算: 超過累進税率）
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

    # 手取り額 = 年収 - 社会保険料 - 所得税 - 住民税
    take_home = gross_income - social_insurance - income_tax - resident_tax

    return round(take_home, 2)


def main():
    # コマンドライン引数から年収を取得
    if len(sys.argv) != 2:
        print("使い方: python kadai.py [年収]")
        sys.exit(1)

    try:
        annual_income = int(sys.argv[1])
    except ValueError:
        print("年収には数値を入力してください．")
        sys.exit(1)

    take_home_salary = calculate_take_home_salary(annual_income)
    
    byebyemoney = annual_income - take_home_salary

    print(f"年収 {annual_income:,.0f} 円の場合，手取りは約 {take_home_salary:,.0f} 円です．{byebyemoney:,.0f}は国の下へ去りました．")


if __name__ == "__main__":
    main()

