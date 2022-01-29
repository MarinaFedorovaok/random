#Задача: Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
                                    # Алгоритм:
                                    # 1. Форируем массив случайых чисел, запуская
                                    #  бота в чат и запрашивая число.
                                    # бот @fedmari_test_bot работает, массив
                                    #  чисел собран в файл numbers.txt
                                    # 2. При запросе случайного числа нам нужен индекс 
                                    # массива - его привязываем ко времени запроса.

import time
def my_bot_random(): # выдает случайное число в интервале от х до y
                                # создаем список на основе данных файла
    import math
    list = []
    filePath = 'D:\\Razrabitchik\\python\\telegram_bot\\numbers.txt'
    file = open(filePath, 'r')
    for line in file:
        list.append(line)
                                #print(list)
                                #print(len(list))
                                # получем нужный индекс
    index = int(time.time())
                                #print(index)
    while index>len(list):
        index = index%len(list)
                                #print(index)
        index_res=math.fabs(index)
                                #print(index_res)
    file.close()
    return(list[int(index_res)])
print('Ваше число:' + my_bot_random())
 
    
    




    

    





