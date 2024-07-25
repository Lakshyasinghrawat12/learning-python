import time
import threading

def print_number():
    for i in range(0,6):
        print(f'number: {i}')
        time.sleep(1)

def print_letter():
    for i in 'abcdef':
        print(f'letter: {i}')
        time.sleep(1)
'''
Python time sleep function is used to add delay in the execution of a program. We can use python sleep function to halt 
the execution of the program for given time in seconds. Notice that python time sleep function actually stops the 
execution of current thread only, not the whole program.
'''
# Create two threads
thread1= threading.Thread(target=print_number)
thread2= threading.Thread(target=print_letter)


# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("both threads have successfully completed")