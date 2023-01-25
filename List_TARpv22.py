from random import *

#Ülesanne 0


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