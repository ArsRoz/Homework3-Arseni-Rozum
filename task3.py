# 3.Даны два списка чисел.
# Посчитайте, сколько различных чисел
# содержится одновременно как в первом списке,
# так и во втором.

list_1 = [1, 2, 3, 4, 5, 6, 12]
list_2 = [1, 6, 8, 9, 2]
res = [x for x in list_1 + list_2 if x not in list_1 or x not in list_2]
print('В списках 1 и 2 ', len(res), 'различных чисел')
