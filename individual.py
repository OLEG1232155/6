#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    s = tuple(map(int, input("Кортеж: ").split()))
    # Проверить количество элементов кортежа.
    if not s:
        print("Неверный размер кортежа.", file=sys.stderr)
        exit(1)

    k = 0
    s1 = []

    for i in range(0, len(s)):
        if (i == 0) or (i == len(s) - 1):
            continue
        if s[i - 1] < s[i] > s[i + 1]:
            s1.append(i)
            s1.append(i + 1)
            s1.append(i + 2)
            k = 1
            break

    if k == 0:
        print("Нет среднего элемента больше своих соседей.")
    else:
        print("Индексы тройки соседних чисел: ", s1)
