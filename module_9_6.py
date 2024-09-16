def all_variants(text):
    len_ = len(text)  # длина строки
    # for single in range(len_):
    #     yield text[single]
    for num in range(1, len_ + 1):  # Выбирается кол-во элементов для вывода
        for symbol in range(len_ - num + 1):  # Выбирается символ или начало вывода символов
            yield text[symbol:symbol + num]  # Вывод диапазона


a = all_variants("abc")
for i in a:
    print(i)
