# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

def CreateMassive (massive):
    value=int(input("> "))
    for i in range(1,value+1):
        massive.append(int(input(f"Введите {i} элемент массива: ")))
    return massive

print("Введите количество элементов в первом массиве")
FirstMassive = []
n=CreateMassive(FirstMassive)

print("Введите количество элементов во втором массиве")
SecondMassive = []
m=CreateMassive(SecondMassive)

TotalMassive=[]

for i in range(len(FirstMassive)):
    for j in range(len(SecondMassive)):
        if SecondMassive[j] == FirstMassive[i]:
            TotalMassive.append(SecondMassive[j])

unique_numbers = list(set(TotalMassive))
print(sorted(unique_numbers))








