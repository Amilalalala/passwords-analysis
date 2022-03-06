#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use a breakpoint in the code line below to debug your script.

broj_velikih_slova = 0
ukupan_broj_velikih_slova = 0
broj_malih_slova = 0
ukupan_broj_malih_slova = 0
broj_cifri = 0
ukupan_broj_cifri = 0
broj_znakova = 0
ukupan_broj_znakova = 0
ukupno_karaktera = 0
broj_lozinki = 0

# with open('rockyou.txt', encoding='utf8') as f:
with open('baze_lozinki/croatian_lower.txt', encoding="ISO-8859-1") as f:
    for line in f:
        lozinka = line
        broj_lozinki = broj_lozinki + 1
        # brojaci
        broj_velikih_slova = 0
        broj_malih_slova = 0
        broj_cifri = 0
        broj_znakova = 0

        # iterate over the string
        for element in lozinka:
            pom = ord(element)
            if 65 <= int(pom) <= 90:
                broj_velikih_slova = broj_velikih_slova + 1
            elif 97 <= int(pom) <= 122:
                broj_malih_slova = broj_malih_slova + 1
            elif 48 <= int(pom) <= 57:
                broj_cifri = broj_cifri + 1
            elif 33 <= int(pom) <= 47 or 58 <= int(pom) <= 64 or 91 <= int(pom) <= 96 or 123 <= int(pom) <= 126:
                broj_znakova = broj_znakova + 1
            else:
                continue

        ukupan_broj_velikih_slova = ukupan_broj_velikih_slova + broj_velikih_slova
        ukupan_broj_malih_slova = ukupan_broj_malih_slova + broj_malih_slova
        ukupan_broj_znakova = ukupan_broj_znakova + broj_znakova
        ukupan_broj_cifri = ukupan_broj_cifri + broj_cifri

        ukupno_karaktera = ukupan_broj_velikih_slova + ukupan_broj_malih_slova + ukupan_broj_cifri + ukupan_broj_znakova


print('Ukupan broj lozinki je ', broj_lozinki)
# print('Ukupno unesenih karaktera je ', ukupno_karaktera)
# print('Ukupno malih slova ', ukupan_broj_malih_slova)
# print('Ukupno znakova ', ukupan_broj_znakova)
# print('Ukupno cifri ', ukupan_broj_cifri)

print('Prosjecan broj karaktera u jednoj lozinki je: ', ukupno_karaktera / broj_lozinki)
print('Prosjecan broj velikih slova u jednoj lozinki je: ', ukupan_broj_velikih_slova/broj_lozinki)
print('Prosjecan broj malih slova u jednoj lozinki je: ', ukupan_broj_malih_slova/broj_lozinki)
print('Prosjecan broj cifri u jednoj lozinki je: ', ukupan_broj_cifri/broj_lozinki)
print('Prosjecan broj znakova u jednoj lozinki je: ', ukupan_broj_znakova/broj_lozinki)
