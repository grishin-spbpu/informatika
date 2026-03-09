numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
#индекс элемента со значением none
index_none = 4

#сумма элементов списка, полученного путем сложения списка элементов numbers, стоящих в исходном списке до элемента со
#значением None, со списком элементов, стоящих после элемента со значением None
sum_of_elements_numbers = sum(numbers[:index_none] + numbers[index_none+1:])
#количество элементов списка numbers
count_of_elements_numbers = len(numbers)
#среднее арифметическое, найденное в соответсвии с условием задачи
arithmetic_mean = sum_of_elements_numbers / count_of_elements_numbers

#замена элемента со значением None в списке numbers найденным средним арифметическим
numbers[index_none] = arithmetic_mean
#вывод результата
print("Измененный список:", numbers)
