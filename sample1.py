list_of_temperature =

[37,38,40,13,0]

class Deep_data: def
    __init__(self,message1,temp1):

        self.message1 = message1
        self.temp1 = temp1

    def         disp_data(self):
        print("normal temperature\r\n\r")
        self.message1 = "cool!!"
        print(self.message1)
    
    def print_na(self): print("temperature description" + self.message1 + "temp" + self.temp1)


deep1 = Deep_data("Normal temp here","22")
deep1.disp_data()
deep1.print_na()


d = random.choice([23,23,24,40,27,28,37])

print("this is the temperature now"+"-","-",d) if(d in the list_of_temperature):
print("opppsss too high!!!")
else:
    deep1.disp_data()


