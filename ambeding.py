student_1={"name":"Lakshya",
    "phone_number":[901929120,12124343545],
    "adresss":"gomti nagar",
    "city":"lucknow",
    "state":"UP",
    "pincode":"226022"}
student_2={"name":"Lakshya",
    "phone_number":[901929120,12124343545],
    "adresss":"mahanagr",
    "city":"lucknow",
    "state":"UP",
    "pincode":"226022"}
lst=[student_1,student_2]
student_3={"name":"Lakshya",
    "phone_number":[901929120,12124343545],
    "adresss":{"city":"lucknow"},
    "state":"UP",
    "pincode":"226022"}
lst.append(student_3)
print(lst)