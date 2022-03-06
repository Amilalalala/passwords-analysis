#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use a breakpoint in the code line below to debug your script.
lozinka = str(input('Unesite potencijalnu šifru: '))
print(lozinka)

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
    else:
        broj_znakova = broj_znakova + 1


# ispis rezultata, pokusati smanjiti
print('Vaša lozinka se sastoji od ', broj_velikih_slova, ' velikih slova, ', broj_malih_slova, ' malih slova, ', broj_cifri, ' cifri i ', broj_znakova, ' ostalih znakova.')

if broj_velikih_slova < 1:
    print('Savjetujemo korištenje barem jednog velikog slova.')
if broj_malih_slova < 1:
    print('Savjetujemo korištenje barem jednog malog slova.')
if broj_cifri < 1:
    print('Savjetujemo korištenje barem jedne cifre.')
if broj_znakova < 1:
    print('Savjetujemo korištenje barem jednog specijalnog znaka.')
