'''
В данном упражнении вы должны написать программу для подсчета среднего значения всех введенных пользователем чисел.
Индикатором окончания ввода будет служить ноль. При этом программа должна выдавать соответствующее сообщение об ошибке,
если первым же введенным пользователем значением будет ноль.
'''

lst = list()
a = int(input())
if a == 0:
	print("Ошибка!")
while a != 0:
	lst.append(a)
	a = int(input())
print(sum(lst)/len(lst))
