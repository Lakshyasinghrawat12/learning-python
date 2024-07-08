import os, sys
from os.path import dirname, join, abspath


# sys.path.insert(index, object)
sys.path.insert(0, abspath(join(dirname(__file__),'..')))
# We use the above three liner code to avoid this error that is prominent without this 
# Traceback (most recent call last):
#  File "c:\Users\laksh\Desktop\python\Data sciene\File handeling\import and module statement\pwskills\course\course_details.py", line 8, in <module>
#    from payment import payment_details
# ModuleNotFoundError: No module named 'payment'


from payment import payment_details


def qcourse():
    print("this is my course details")


payment_details.payment()
