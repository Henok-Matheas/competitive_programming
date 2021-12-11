
"3 min 1 submit"
s = "Myself2 Me1 I4 and3"


def sortSentence(s):
    listi = [0]*8
    final = ""
    temp = " "
    for  i in s:
        try:
            inti = int(i)
            listi[inti-1] = temp
            temp = " "
        except:
            if i != " ":
                temp += i
                print(temp)
    for i in listi:
        if i != 0:
            final += i+" "

    return final.rstrip()


sortSentence(s)
print(sortSentence(s))
