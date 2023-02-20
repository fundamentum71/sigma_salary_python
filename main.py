
holidaysInput = {}
nextHoliday = 1
# day = 0
# hours = 0
mounth = input('Введите месяц: ')
# while type(day) != int or type(hours) != int:
try:
    while nextHoliday != 0:
        day = int(
            input("Введите введите число, когда выходили в выходной день (если больше не выходили введите '0'): "))
        nextHoliday = int(day)
        if nextHoliday == 0:
            break
        hours = int(input("Введите введите количество часов, когда выходили: "))
        holidaysInput[day] = hours
except ValueError:
    print('Ты ввел не число, дурачёк')


print(holidaysInput)

num_key = []
arraySun = []
arraySat = []
normalRateHour = 0
higherRateHour = 0

for key in holidaysInput:
    num_key.append(key)

# print(num_key)

for key, item in holidaysInput.items():
    print('дата: ', key, mounth)
    print("часов: ", item)
    if num_key.count(key + 1) != 0:
        print('суббота')
        print('*' * 50)
        arraySat.append(item)
        continue

    if num_key.count(key - 1) != 0:
        print('воскресенье')
        print('*' * 50)
        arraySun.append(item)
        continue

    print('Одиночный день')
    print('*' * 50)
    normalRateHour += item

# print('Парные вых. Субботы: ', arraySat)
# print('Парные вых. Воскресение: ', arraySun)

arraySum = map(sum, zip(arraySat, arraySun))
arraySumList = list(arraySum)
# print(arraySumList)

for el in arraySumList:
    # print(el)
    if el > 7:
        normalRateHour += 7
        higherRateHour += el - 7

print('Нормальная ставка :', normalRateHour, 'Повышенная ставка :', higherRateHour)

hourPrice = 287
overPriceToHolidays = normalRateHour * hourPrice + higherRateHour * 2 * hourPrice
print('Деньги за выходные: ', overPriceToHolidays, 'руб.')
