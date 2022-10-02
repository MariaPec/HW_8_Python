# 1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

n = int(input("Введите количество оценок "))

from random import randint 
marks = []
for i in range(n):
    marks.append(randint(1,5))
print(marks)   

max = marks[0]
min = marks[0]

for i in range(len(marks)):
    if marks[i] > max:
        max = marks[i]
       
    if marks[i] < min:
        min = marks[i]

marks1 = []

for j in range(len(marks)):
    if marks[j] == max:
        marks1.append(min)
    else:
        marks1.append(marks[j])

print(marks1)   
