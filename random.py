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
#print([my_bot_random()])
    
    




    

    





