#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目が違うぞボケ"
    res=1
}

res=0

### NORMAL INPUT ###
out=$(echo ""| ./tedorikeisan)
input(\n)
out=$(echo 1000000 | \n ) # 最初の1行（プロンプト）を削除
expected="年収を入力してください(円) : 年収 1,000,000 円の場合，手取りは約 794,500 円です．
205,500 円は国の下へ去りました．"
[ "${out}" = "${expected}" ] || ng "$LINENO"

### STRANGE INPUT ###
out=$(echo ""| ./tedorikeisan)
input(\n)
out=$(echo 0.0| \n )
[ "$?" -ne 0 ] || ng "$LINENO"
expected_error="入力エラー: 年収は正の数である必要があります。"
[ "${out}" = "${expected_error}" ] || ng "$LINENO"

### CHECK RESULT ###
[ "$res" -eq 0 ] && echo OK
exit $res
