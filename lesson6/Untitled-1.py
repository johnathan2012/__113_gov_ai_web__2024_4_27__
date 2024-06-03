try:
    scores = int(input("請輸入學生分數(最高300):"))
    if scores <= 300 and scores >= 0:
        is_add = input("學生是否符合加分條件?(y,n)")

        if is_add == 'y':
            scores *= 1.05
            if scores > 300:
                scores = 300

        print("目前學生的分數", round(scores))
    else:
        print("輸入分數超過300或小於0")
except:
    print("格式錯誤")
print("應用程式結束")