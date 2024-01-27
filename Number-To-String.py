fix = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}
ten = {
    "2" : "twenty",
    "3" : "thirty",
    "4" : "forty",
    "5" : "fifty",
    "6" : "sixty",
    "7" : "seventy",
    "8" : "eighty",
    "9" : "ninety"
}

def checkvalid(number):
    if number.startswith("0") or n == '':
        return False
    else:
        for ch in number:
            if n.isdigit():
                continue
            else:
                return False
        return True

n = str(input())

if checkvalid(n) == False:
    print("ERROR")
else:
    if int(n) > 999 or int(n) < 0:
        print("ERROR")
    else:
        c = len(str(n))
        if c == 1:
            print(fix[n])
        elif c == 2:
            if int(n) < 20:
                print(fix[n])
            else:
                if int(n) % 10 == 0:
                    print(ten[n[0]])
                else:
                    print(f"{ten[n[0]]}-{fix[n[1]]}")
        else:
            if int(n) % 100 == 0:
                print(f"{fix[n[0]]}-hundred")
            else:
                if int(n) % 10 == 0:
                    if n[1] == "1":
                        print(f"{fix[n[0]]}-hundred-{fix[n[1:3]]}")
                    else:
                        print(f"{fix[n[0]]}-hundred-{ten[n[1]]}")
                else:
                    if n[1] == "0":
                        print(f"{fix[n[0]]}-hundred-{fix[n[2]]}")
                    else:
                        if int(n[1:3]) < 20:
                            print(f"{fix[n[0]]}-hundred-{fix[n[1:3]]}")
                        else:
                            print(f"{fix[n[0]]}-hundred-{ten[n[1]]}-{fix[n[2]]}")