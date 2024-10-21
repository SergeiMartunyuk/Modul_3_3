# 1 Функция с параметрами по умолчанию

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()

# 2 Распаковка параметров

print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [159, False, (1, 3)]
values_dict = {'a':354, 'b':98.7, 'c':'Hi!'}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)