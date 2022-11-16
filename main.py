answer_text_file = open("wyniki4.txt", "w")

#Odczytanie danych z pliku
def read():
    text_file = open("Dane_PR2/przyklad.txt", "r")
    lines = text_file.read()
    data = lines.split("\n")
    return data

#zadanie 4.1
def zad41():
    text_file = open("Dane_PR2/liczby.txt", "r")
    lines = text_file.read()
    data = lines.split("\n")
    liczby=0
    for x in data:
        m=3
        while int(x) > m:
            m*=3
        if int(x) == m:
            liczby+=1
    #answer_text_file = open("wyniki4.txt", "w")
    answer_text_file.write(f"Zadanie 4.1:\n\tLiczba takich liczb to: {liczby}\n")

#zadnie 4.2
def zad42():
    text_file = open("Dane_PR2/liczby.txt", "r")
    lines = text_file.read()
    data = lines.split("\n")
    liczby = []
    for x in data:
        sumac = 0
        for y in x:
            suma = 1
            m = int(y)
            while m>0:
                suma*=m
                m-=1
            sumac+=suma
            if sumac == int(x):
                liczby.append(sumac)
    #answer_text_file = open("wyniki4.txt", "w")
    answer_text_file.write(f"Zadanie 4.2:\n\tTakie liczby to: {liczby}\n")

#zadanie 4.3
def zad43():
    def NWD(a, b):
        if b > 0:
            return NWD(b, a % b)
        return a
    
    
    def searchMaxLen():
        text_file = open("Dane_PR2/liczby.txt", "r")
        lines = text_file.read()
        data = lines.split("\n")
        allLength = 0
        firstElem = 0
        returnedNWD = 0
        length = len(data)
    
        for i in range(length - 1):
            minNWD = data[i]
            first = data[i]
            k = 1
    
            for j in range(i + 1, length):
                n = NWD(int(minNWD), int(data[j]))
    
                if n > 1:
                    minNWD = n
                    k += 1
    
                if n == 1 or length - 1 == j:
                    if k > allLength:
                        returnedNWD = minNWD
                        firstElem = first
                        allLength = k
                    break
        answer_text_file.write(f"Zadanie 4.3:\n\tPierwszy element ciągu to {firstElem}, ciag trwa {allLength}, NWD wysnosi {returnedNWD}\n")
    searchMaxLen()

zad41()
zad42()
zad43()