ma = ("Maandag")
di = ("Dinsdag")
wo = ("Woensdag")
do = ("Donderdag")
vr = ("Vrijdag")
za = ("Zaterdag")
zo = ("Zondag")
while True:
    Dag = input("Vraag een dag van de week op : ")
    if Dag == "maandag":
        print(ma)
        break
    elif Dag == "dinsdag":
        print(ma, di)
        break
    elif Dag == "wonesdag":
        print(ma, di, wo)
        break
    elif Dag == "donderdag":
        print(ma, di, wo, do)
        break
    elif Dag == "vrijdag":
        print(ma, di, wo, do, vr)
        break
    elif Dag ==  "zaterdag":
        print(ma, di, wo, do, vr, za)
        break
    elif Dag == "zondag":
        print(ma, di, wo, do, vr, za, zo)
        break
    else:
        print("Sorry probeer nog een keer :")
        
           