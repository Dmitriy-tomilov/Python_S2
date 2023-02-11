# Задача 2. Ближайший элемент

# Найдите в list_1 ближайший по величине к числу k элемент. 
# Сохраните этот элемент в переменную res. 
# Выводить переменную res на экран не требуется.

list_1 = [1, 2, 3, 3, 4, 6]
k = int (input("Введите число: "))

min = abs(k - list_1[0])
res = list_1[0]
for i in range (len(list_1)):
    if min > abs(k - list_1[i]):
        min = abs(k - list_1[i])
        res = list_1[i]
print(res)