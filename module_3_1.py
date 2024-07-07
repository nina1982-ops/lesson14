calls = 0                         #  Создать переменную calls = 0 вне функций
def count_calls():                # объявили функцию count_calls, подсчитывающую вызовы остальных функций
    global calls                  # переменная глобальная
    calls += 1
    return calls                  # завершает выполнение функции, и передает значение обратно в вызывающий код
def string_info(string):          # объявили функцию string_info с параметром string
    string = (len(string), string.upper(), string.lower())   # создали переменную - кортеж из: длины этой строки
                                                             # (принимает аргумент), строку (принимает аргумент)
                                                             # в верхнем регистре,строку (принимает аргумент) в нижнем
                                                             # регистре.
    count_calls()                  # вызов функции count_calls
    return string                  # завершает выполнение функции, и передает значение обратно в вызывающий код
def is_contains (string, list_to_search):   # объявили функцию is_contains с параметрами string, list_to_search
    count_calls()                           # вызов функции count_calls
    for i in list_to_search:
        if i.lower() == string.lower():     # условие: если строка находится в этом списке возвращает True и
                                            # False - если отсутствует
            return True
    return False
print(string_info('Capybara'))              # Вызвать соответствующие функции string_info и is_contains произвольное
                                            # кол-во раз с произвольными данными.
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)                                












