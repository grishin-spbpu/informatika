# TODO Найдите количество книг, которое можно разместить на дискете
#записываю исходные данные
volume_of_diskette = 1.44 * 2**20 #объём дискеты в байтах
volume_of_one_symbol = 4

count_of_pages = 100
count_of_lines_per_page = 50
count_of_symbols_per_line = 25
#количество байтов, требующихся для хранения одной книги
volume_of_one_book = count_of_symbols_per_line * count_of_lines_per_page * count_of_pages *volume_of_one_symbol

#количество книг, помещающихся на дискете. Использую целочисленное деление, так как нужно найти целое число и функцией
#int() убираю дробную часть (она появилась, потому что значение volume_of_diskette - дробное число). Благодаря этому на
#выходе получаю значение "3", а не "3.0"
count_of_books_fit_on_diskette = int(volume_of_diskette // volume_of_one_book)
#вывод результата
print("Количество книг, помещающихся на дискету:", count_of_books_fit_on_diskette)
