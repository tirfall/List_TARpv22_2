from random import *


#Ülesanne 0
word = str(input(""))
while True:
    print("Menu:")
    print("1 1")
    print(" 2")
    print(" 3")
    print(" 4")
    print(" 5")
    print(" 6")
    print(" 7")
    print(" 8")
    print(" 9")
    print(" 10")
    print("0 - stop")

    choice = int(input("Sinu valik: "))

    if choice == 1:
        
        pass
    elif choice == 2:
        
        pass
    elif choice == 3:
        
        pass
    elif choice == 4:
        
        pass
    elif choice == 5:
        
        pass
    elif choice == 6:
        
        pass
    elif choice == 7:
        
        pass
    elif choice == 8:
        
        pass
    elif choice == 9:
        
        pass
    elif choice == 10:
        
        pass
    elif choice == 0:
        print("Head aega!")
        break
    else:
        print("Valik error")

#Ülesanne 1
#nimi_list = []
#for x in range(5):
#    nimi = str(input("Sisse nimi:"))
#    nimi_list.append(nimi)
#nimi_list.sort()
#print(nimi_list)
#print("Viimane nimi:", nimi)

#Ülesanne 2
#opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
#print(opilased)
#while True:
#    vastus = int(input(" 1-Kustuta nimi\n 2-Lisa nimi\n 3-stop programmi\n"))
#    if vastus==1:
#        kustnimi = (input("Sisse nimi:"))
#        opilased.remove(kustnimi)
#        print(opilased)
#    elif vastus==2:
#        appnimi = (input("Sisse nimi:"))
#        opilased.append(appnimi)
#        print(opilased)
#    elif vastus==3:
#        print("Head aega!")
#        break

#Ülesanne 3
#studentid = ["Kati","Mario","Viki","Kati","Nikolas","Nikolas"]
#print(studentid)
#print()
#x=i=len(studentid)
#while i>=0:
#    i-=1
#    x=len(studentid)-1
#    while x>=0 and i>=0:
#        if x!=i and studentid[x]==studentid[i]:
#            studentid.pop(x)
#            if len(studentid)==i:
#                i-=1
#        x-=1
#print(studentid)

#Ülesanne 4
#while True:
#    try:
#        yesno = str(input("Tere! Kas sa tahad alustada programmi?  jah või ei: "))
#        break
#    except ValueError:
#        print("Vali õige vastu")
#if yesno == "jah":
#    vanus_list = []
#    for x in range(20):
#        vanus = randint(1, 100)
#        vanus_list.append(vanus)
#    print("\n")
#    print(vanus_list)
#    print(max(vanus_list),"Maksimaalne vanus")
#    print(min(vanus_list) ,"Minimaalne vanus")
#    print(sum(vanus_list), "Kogusumma vanus")
#    print(sum(vanus_list) / len(vanus_list), "Keskmine vanus")
#else:
#    print("Head aega!")


#Ülesanne 5
#linumb = []
#x = 1
#while x == 1:
#    ansnumb = int(input("Tere, mis numbrid sa tahad?\n"))
#    linumb.append(ansnumb)
#    anskoik = (input("Kas see on kõik? jah või ei:"))
#    if anskoik == ("jah"):
#        x = 2
#    if anskoik == ("ei"):
#        x = 1
#print(linumb)
#for i, item in enumerate (linumb):
#    print("*"*linumb[i-1])
#print()
