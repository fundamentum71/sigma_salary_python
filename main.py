holidays = {
    # 29: 5,
    4: 5,
    5: 5,
    18: 5,
    19: 5,
}

holidaysInput = {}
nextHoliday = 0

while nextHoliday < 4:
    day = input("Введите введите число, когда выходили: ")
    hours = input("Введите введите количество часов, когда выходили: ")
    holidaysInput[day] = hours
    nextHoliday += 1

print(holidaysInput)

# num_key = []
# arraySun = []
# arraySat = []
# normalRateHour = 0
# higherRateHour = 0
#
# for key in holidays:
#     num_key.append(key)
#
# print(num_key)
#
# for key, item in holidays.items():
#     print('дата: ', key)
#     print("часов: ", item)
#     if num_key.count(key + 1) != 0:
#         print('суббота')
#         print('*' * 50)
#         arraySat.append(item)
#         continue
#
#     if num_key.count(key - 1) != 0:
#         print('воскресенье')
#         print('*' * 50)
#         arraySun.append(item)
#         continue
#
#     print('Одиночный день')
#     print('*' * 50)
#     normalRateHour += item
#
# print('Парные вых. Субботы: ', arraySat)
# print('Парные вых. Воскресение: ', arraySun)
#
# arraySum = map(sum, zip(arraySat, arraySun))
# arraySumList = list(arraySum)
# print(arraySumList)
#
# for el in arraySumList:
#     print(el)
#     if el > 7:
#         normalRateHour += 7
#         higherRateHour += el - 7
#
# print('Нормальная ставка :', normalRateHour, 'Повышенная ставка :', higherRateHour)
#
#
# hourPrice = 287
# overPriceToHolidays = normalRateHour * hourPrice + higherRateHour * 2 * hourPrice
# print('Деньги за выходные: ', overPriceToHolidays, 'руб.')
