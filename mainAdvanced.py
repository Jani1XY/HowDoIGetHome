import time

hely = None
ido = None
eso = False




def printResult(ido1, ido2, telepules1, telepules2, allomas1, allomas2, busz1, busz2, erkezes1, erkezes2, seta):
    # print("Pécs,             15:30-kor            a            8-as kocsiállásról budapesti busz, Bonyhádig")
    stm = telepules1+", "+ ido1+ "-kor a "+ allomas1 + " kocsiállásról " + busz1 + "i busz, " + erkezes1

    if seta == True:
        stm = stm + "\n|" + "\n|" + "\nV"
        stm = stm + erkezes1 + ", séta hazáig"
    else:

        if telepules2 != None:

            stm = stm + "\n|" + "\n|" + "\nV"
            stm = stm + telepules2+", "+ ido2+ "-kor a "+ allomas2 + " kocsiállásról " + busz2 + "i busz, " + erkezes2
        
    print(stm)

#printResult("15:30", None,  "Pécs", None, "8-as", None, "budapest", None, "Bonyhádig", None, False)

def timeToMin(time):
       minute = time.split(":")
       minutes = int(minute[0])*60 + int(minute[1])
       return minutes

def timeToMinRev(minute):
       time = str((minute // 60)) + ":" + str(minute%60)
       return time


def correctFormat(cucc):
    try:
        time.strptime(cucc, '%H:%M')
        return True
    except ValueError:
        return False

def userInput():
    global hely
    global ido
    global eso
    order = False

    hely = input("Hol van Jani? (Pécs / Bonyhád)\n")
    hely = hely.capitalize()
    if hely == "Pécs" or hely == "Bonyhád":
        pass
    else:
        hely = input("Mégegyszer? (Pécs / Bonyhád)\n")
        hely = hely.capitalize()
        if hely == "Pécs" or hely == "Bonyhád":
            pass
        else:
            print("Az szar ügy")
            exit()
    while True:
        ido = input("Hány óra van? (óó:pp)\n")
        if correctFormat(ido) == True:
            if timeToMin(ido) > 985:
                print("Az már túl késő!")
                exit()
            else:
                break


    while True:
        temp = input("Esett az eső az elműlt 4 napban? (igen / nem)\n")
        if temp == "igen":
            eso = True
            break
        if temp == "nem":
            eso = False
            break

def egyorasi():
    global hely

    if hely == "Pécs":
        print("Pécs, 13:30-kor a 8-as kocsiállásról budapesti busz, Bonyhádig")
        print("|")
        print("V")
        print("Bonyhádon, 14:40-kor 7-es kocsiállás, Kismányokig")
    else:
        print("Bonyhádon, 13:35-kor 7-es kocsiállás, kismányoki elágázásig")
        print("|")
        print("V")
        print("kismányoki elágazásnál, séta hazáig")

def ketorasi():
    global hely
    global eso


    if hely == "Pécs":
        if eso == True:
            print("Pécs, 14:30-kor a 9-as kocsiállásról bonyhádi busz, Hidas-ig")
            print("|")
            print("V")
            print("Hidason, séta hazáig")
        else:
            print("14:30-kor a 9-as kocsiállásról bonyhádi busz")
            print("Bonyhádon, 15:45-kor 10-es kocsiállás, kismányoki elágazásig")
            print("|")
            print("V")
            print("kismányoki elágazásnál, séta hazáig")
    else:
        print("Bonyhádon, 14:40-kor 7-es kocsiállás, kismányokig")


def haromorasi():
    global hely

    if hely == "Pécs":
        print("Pécs, 15:30-kor a 8-as kocsiállásról budapesti busz, Bonyhádig")
        print("|")
        print("V")
        print("Bonyhádon, 16:25-kor 6-es kocsiállás, Kismányokig")
    else:
        print("Bonyhádon, 15:45-kor 10-es kocsiállás, kismányoki elágazásig")
        print("|")
        print("V")
        print("kismányoki elágazásnál, séta hazáig")

def negyorasi():
    print("Pécs, 16:30-kor a 8-as kocsiállásról budapesti busz, Bonyhádig")
    print("|")
    print("V")
    print("Bonyhádon, anya hazavisz")


print(timeToMin("13:35"))

print("Iskola után Jani hogy megy haza?\n")

userInput()

if hely == "Pécs":
    tm = timeToMin(ido)
    if tm < 2:
        pass

    elif timeToMin(ido) <  810: # timeToMin(13:30)
        print()
        egyorasi()

    elif timeToMin(ido) < 870: # 14:30
        print()
        ketorasi()

    elif timeToMin(ido) < 930: #15:30
        print()
        haromorasi()

else:

    if timeToMin(ido) <  815: # 13:35
        print()
        egyorasi()

    elif timeToMin(ido) < 880: # 14:40
        print()
        ketorasi()

    elif timeToMin(ido) < 945: # 15:45
        print()
        haromorasi()

    elif timeToMin(ido) < 990: # 16:30
        print()
        negyorasi()



#      Pécs                     Bonyhád
#   13:30 Budai 8-as  -->     2:40 Kismányoki 7-es
#   
#      Pécs                    Erdő          Bonyhád          Kismányoki eágazás
#   14:30 Bonyhadi 9-es -->     séta     VAGY 3:45 10-es  -->     séta
#
#       Pécs                       Bonyhád
#   15:30 Budapesti 8-as  -->     4:25 6-os
        
# adatbekérés
# van 1 minta     %time% %település% + "i" %állomás%    HA VAN "-->"     %time% %település% + "i" %állomás%
        
