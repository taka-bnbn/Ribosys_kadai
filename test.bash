#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目が違うぞボケ"
    res=1
}

res=0

### NORMAL INPUT ###
out=$(echo 1000000 | ./tedorikeisan)
expected="年収 1,000,000 円の場合，手取りは約 794,500 円です．
205,500 円は国の下へ去りました．"
[ "${out}" = "${expected}" ] || ng "$LINENO"

### STRANGE INPUT ###
out=$(echo 0.0 | ./tedorikeisan 2>&1)
[ "$?" -ne 0 ] || ng "$LINENO"
expected_error="入力エラー: 年収は正の数である必要があります。"
[ "${out}" = "${expected_error}" ] || ng "$LINENO"

out=$(echo -1000000 | ./tedorikeisan 2>&1)
[ "$?" -ne 0 ] || ng "$LINENO"
[ "${out}" = "${expected_error}" ] || ng "$LINENO"

out=$(echo "abc" | ./tedorikeisan 2>&1)
[ "$?" -ne 0 ] || ng "$LINENO"
[ "${out}" = "${expected_error}" ] || ng "$LINENO"

### EMPTY INPUT ###
out=$(echo "" | ./tedorikeisan 2>&1)
[ "$?" -ne 0 ] || ng "$LINENO"
[ "${out}" = "${expected_error}" ] || ng "$LINENO"

### CHECK RESULT ###
[ "$res" -eq 0 ] && echo OK
exit $res

