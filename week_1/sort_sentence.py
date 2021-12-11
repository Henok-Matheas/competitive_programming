
"3 min 1 submit"
s = "QcGZ4 TFJStgu3 HvsRImLBfHd8 PaGqsPNo9 mZwxlrYzanuVOUZoyNjt1 fzhdtYIen6 mV7 LKuaOtefsixxo5 pwdEK2"


def sortSentence(s):
    listi = [0]*8
    final = ""
    temp = " "
    for  i in s:
        print(i)
        # try:
        #     inti = int(i)
        #     print(i)
        #     if inti == 9:
        #         print("I have found nine!")
            
        #     listi[inti-1] = temp
        #     temp = " "
        # except:
        #     if i != " " and i !=' ':
        #         temp += i

    for i in listi:
        if i != 0:
            final += i+""

    return final.rstrip().lstrip()


sortSentence(s)
print(sortSentence(s))
