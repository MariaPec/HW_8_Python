# 2. Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). 
# Через рекурсию необходимо делать

# Input: 2 -> 3 4
# Output: 4 3

from calendar import c
from random import randint

N = int(input("введите N: "))

a = randint(1, 10)

def Sub(x, start, N):
    if x == start + N:
        return ""
    if x < start + N:
        return f"{x} {Sub(x+1, start, N)}"

def SubBack(x, start, N):
    if x == start - N:
        return ""
    if x + N > start:
        return f"{x - 1} {SubBack(x-1, start, N)}"

print(Sub(a, a, N))
print()
print(SubBack(a + N, a + N, N))

