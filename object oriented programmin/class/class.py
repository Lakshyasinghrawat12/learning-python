#1
class test:
    pass

a= test()
print(type(a))


#2
class pwskills:
    def msg(self):
        print("Wlecome")

rohan= pwskills()
print(type(rohan))
rohan.msg()

#3
class pwskills1:
    def __init__(self, phone_num, emailid, std_id):
        self.phone_number= phone_num
        self.email= emailid
        self.stdid= std_id

    def return_detail(self):
        return self.stdid, self.email, self.phone_number
    
rohaan= pwskills1(34892749729, 'laskyah@gmail.com', 213141)
rohaan.return_detail()