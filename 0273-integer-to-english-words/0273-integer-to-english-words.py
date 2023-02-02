class Solution:
    def hundConverter(self,num):
        dict = {
                   0 : "",
                   1:"One",
                   2:"Two",
                   3: "Three",
                   4: "Four",
                   5: "Five",
                   6: "Six",
                   7 : "Seven",
                   8 : "Eight",
                   9 : "Nine",
                10 : "Ten",
                11 : "Eleven",
                12 : "Twelve",
                13 : "Thirteen", 
                14 : "Fourteen",
                15 : "Fifteen",
                16 : "Sixteen",
                17 : "Seventeen",
                18 : "Eighteen",
                19 : "Nineteen",
                20 : "Twenty",
                30 : "Thirty",
                40 : "Forty",
                50 : "Fifty",
                60 : "Sixty",
                70 : "Seventy",
                80 : "Eighty",
                90 : "Ninety",
                100 : "Hundred",
                   }
        hund = num // 100
        add_hund = dict[hund] + " Hundred " if hund != 0 else ""
        
        tens = (num - (hund * 100))
        
        if tens in dict:
            return add_hund + dict[tens]
        else:
            tns = tens // 10
            ones = tens - (tns * 10)
            add_tens = dict[tns * 10] +" " + dict[ones]
            return add_hund + add_tens
    def numberToWords(self, num: int) -> str:
        stringy = str(num)
        
        if num == 0:
            return "Zero"
        
        elif len(stringy) < 4:
            return str(self.hundConverter(num)).strip(" ").replace("  "," ")
                 
        elif len(stringy) > 3 and len(stringy) < 7 :
            hund = stringy[-3 : ]
            thousand = stringy [ : -3]
            return str(self.hundConverter(int(thousand)) + (" Thousand " if int(thousand) != 0 else "") + self.hundConverter(int(hund))).strip(" ").replace("  "," ")
                 
        elif len(stringy) > 6 and len(stringy) < 10 :
            hund = stringy[-3 : ]
            thousand = stringy [-6 : -3]
            mil = stringy [ : -6]
            return str(self.hundConverter(int(mil)) + (" Million " if int(mil) != 0 else "") + self.hundConverter(int(thousand)) + (" Thousand " if int(thousand) != 0 else "") + self.hundConverter(int(hund))).strip(" ").replace("  "," ")
                 
        else:
            hund = stringy[-3 : ]
            thousand = stringy [-6 : -3]
            mil = stringy [-9 :-6]
            bil = stringy [0]
            return str(self.hundConverter(int(bil)) + (" Billion " if int(bil) != 0 else "") + self.hundConverter(int(mil)) + (" Million " if int(mil) != 0 else "") + self.hundConverter(int(thousand)) + (" Thousand " if int(thousand) != 0 else "") + self.hundConverter(int(hund))).strip(" ").replace("  "," ")