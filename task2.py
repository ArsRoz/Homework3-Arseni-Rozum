# 2.Дан список стран и городов каждой страны.
# Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

dict_1 = {}
for _ in range(int(input())):
    country, *town = input().split()
    for town in towns:
        dict_1[town] = country
print(*(dict_1[input()] for _ in range(int(input()))), sep="\n")
