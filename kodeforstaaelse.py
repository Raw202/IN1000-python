a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
#1-Dette er greit med variabel, input og if-test, men dette er
#ikke lovlig kode fordi vi kan ikke slå sammen str og int. Det vil gi error
#2-Vi får et problem for at vi ikke klarer å printe b som er int med ordet Hei
#fordi man kan ikke printe et int og str på samme linje. 
