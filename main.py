def max_in_two(a,b):
    if a == b: return 'Числа равны'
    elif a > b: return 'Первое число больше'
    else: return 'Второе число больше'
def emptyfunc():
    pass
def chet(n):
    for i in range(0, n+1, 2):
        yield i
def test_max_in_two():
    assert max_in_two(2,3) == 'Второе число больше', 'Ошибка: 2<3'
    assert max_in_two(2, -3) == 'Первое число больше', 'Ошибка: 2>-3'
    assert max_in_two(2, 2) == 'Числа равны', 'Ошибка: 2=2'
    print('Тесты пройдены!')
a = -10
b = -10
print(max_in_two(a,b))
chisla = chet(10)
for i in chisla:
    print(i)
test_max_in_two()
