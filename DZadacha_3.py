# Задача 3 Скрабл.

word = input("Введите слово:")
Points_en = {1: "AEIOULNSTR", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
Points_ru = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ" }

word = word.upper()
res = 0

for i in word:
    if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
        for j in Points_en:
            if i in Points_en[j]:
                print(j)
                res = res+j
    else:
        for j in Points_ru:
            if i in Points_ru:
                res = res + j
print(res)