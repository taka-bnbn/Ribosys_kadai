<p align="center">
  <img width="400" img src="https://github.com/user-attachments/assets/8d9332b3-e3c9-48a5-b9f1-cf349d146c9e" alt="Animation" />
</p>


[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![test](https://github.com/taka-bnbn/Ribosys_kadai/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/taka-bnbn/Ribosys_kadai/actions/workflows/test.yml)

### 自分の年収がいくら国に徴収されているか気になりませんか？

## 概要

- このプログラムは,日本の一般的な所得税,住民税,社会保険料の計算方法を簡略化して反映したものです,<br>
- なお,実際の手取り額は詳細な条件（扶養人数,住んでいる地域,保険の種類など）によって異なるため,あくまで目安としてご利用ください.<br>

## 設定項目

- 社会保険料: 健康保険,年金保険,雇用保険などを含みます. 年収の約15%程度と見積もっています.<br>
- 所得税:     超過累進課税方式を適用し,控除額を反映しました.<br>
- 住民税:     課税所得の約10%を基準に計算しています.<br>
- 基礎控除:   2020年以降,基礎控除額は48万円です.<br># Ribosys_kadai

## インストール&実行方法

- パーミッション変更
```bash
chmod +x kadai
```
- リポジトリをクローン
```bash
git clone https://github.com/taka-bnbn/Ribosys_kadai.git
```
- Robosys_kadaiに移動
```bash
cd Robosys_kadai
```
- (例)自分の年収が700万円の時
```bash
./kadai.py 700
```

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.11

## ライセンス

- 3条項BSDライセンスの下，再頒布及び使用が許可されます．
- このコマンドの社会保険料，所得税，住民税，基礎控除の計算方法は以下のサイトを基にコードを書いています．
```bash
https://www.musashi-corporation.com/wealthhack/annual-income-net-income
```

## テスト環境
- Ubuntu 20.04 LTS


## Copyright

@ 2024 Takaya Mizumaki
水牧鷹哉
