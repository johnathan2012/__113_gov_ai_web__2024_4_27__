''''class BMI
field -> name,weight,height
property -> bmi
instance method -> status
輸入
請輸入姓名
體重
身高
輸出
徐國堂您好,BMI:26.12,體重:過重
'''

class BMI():
    def __init__(self,n:str):
        self.name = n
    
 #   def __repr__(self):
 #       return f"這是Person的實體,我的名字是{self.name}" #字串插補
    
class Human(BMI):
    def __init__(self,name:str,height:int,weight:int):
        super().__init__(name)
        self.__height = height
        self.__weight = weight
     
    
    @property
    def height(self):
        return self.__height
    
    @property
    def weight(self):
        return self.__weight
    
    def __repr__(self):
        message = ""
     #   message += "這是Student的實體\n"
        message += f"{self.name}先生/女士，您好!\n"
        message += f"身高:{self.chinese}cm\n"
        message += f"體重:{self.english}kg\n"
        return message
    
    def bmi(self) -> float: #實體的method
        return round(self.__weight / (self.__height/100)**2,ndigits=2)
    
 #   def average(self) -> float:
 #       return self.sum() / 3

s1 = ("陳添盛",158,79)
#print(type(s1))
print(s1.name)
print(f"BMI:{s1.bmi()}")
#print(f"平均:{round(s1.average(),ndigits=2)}")
print(s1)