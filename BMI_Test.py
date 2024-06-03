name = str(input("請輸入姓名:")) 
height = int(input("請輸入身高(cm):")) 
weight = int(input("請輸入體重(kg):"))


#BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)
BMI = weight / (height/100)**2 

print("=====================================")
print(name+" 先生/女士,您好!")
print("您的身高:",height,"cm")
print("您的體重:",weight,"kg")
print("您的BMI值為:",round(BMI,2),"(kg/m2)") 

if BMI < 18.5:
    print("您的身體質量:過輕")     #體重過輕 BMI<18.5
elif 18.5 <= BMI < 24:
    print("您的身體質量:正常")     #正常範圍 18.5≦BMI＜24
elif 24 <= BMI < 27:
    print("您的身體質量:過重")     #過重 24≦BMI＜27
elif 27 <= BMI < 30:
    print("您的身體質量:輕度肥胖") #輕度肥胖 27≦BMI＜30
elif 30 <= BMI < 35:
    print("您的身體質量:中度肥胖") #中度肥胖 30≦BMI＜35
else:
    print("您的身體質量:重度肥胖") #重度肥胖 BMI≧35
print("=====================================")










