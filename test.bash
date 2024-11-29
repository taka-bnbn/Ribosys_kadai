#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Takaya Mizumaki
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目が違うぞボケ"
    res=1
}

res=0

### NORMAL INPUT ###
out=$(./tedorikeisan 1000000)
expected="年収 1,000,000 円の場合，手取りは約 794,500 円です．
205,500 円は国の下へ去りました．"
[ "${out}" = "${expected}" ] || ng "$LINENO"

### STRANGE INPUT ###
out=$(./tedorikeisan 2>&1)
[ "$?" -ne 0 ] || ng "$LINENO"
expected_error="使い方: ./kadai [年収]"
[ "${out}" = "${expected_error}" ] || ng "$LINENO"

### CHECK RESULT ###
[ "$res" -eq 0 ] && echo OK
exit $res

