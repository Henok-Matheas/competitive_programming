
"3 min 1 submit"
s = "QcGZ4 TFJStgu3 HvsRImLBfHd8 PaGqsPNo9 mZwxlrYzanuVOUZoyNjt1 fzhdtYIen6 mV7 LKuaOtefsixxo5 pwdEK2"


def sortSentence(s):
    listi = [0]*9
    final = ""
    temp = " "
    for  i in range(len(s)):
        try:
            inti = int(s[i])
            print(s[i])
            if inti == 9:
                print("I have found nine!")
            
            listi[inti-1] = temp
            temp = " "
        except:
            if s[i] != " ":
                temp += s[i]

    for i in listi:
        if i != 0:
            final += i+""

    return final.rstrip().lstrip()


# sortSentence(s)
print(sortSentence(s))
