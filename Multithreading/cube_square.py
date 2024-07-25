import threading
import time


def square_num(number):
    for i in number:
        print(f'square: {i*i} \n')
        time.sleep(1)    

def cube_num(number):
    for i in number:
        time.sleep(1)
        print(f'cube: {i*i*i} \n')
    
number= [1, 2, 3, 4, 5]


thread1= threading.Thread(target= square_num, args= (number,))
thread2= threading.Thread(target= cube_num, args= (number,))

#start the thread
thread1.start()
thread2.start()




#wait till both threads complete
thread1.join()
thread2.join()
print("Both threads have sucessfully completed")