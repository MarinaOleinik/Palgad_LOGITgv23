from PalgadeMoodul import *


palgad=[1200,2500,750,395,1200,2500]
inimesed=["A","B","C","D","E","D"]

while True:
    print("0-Andmed ekraanile\n1-Andmete lisamine\n2-Andmete eemaldamine\n")
    vastus=int(input())
    if vastus==0:
        naita_andmed(inimesed,palgad)
    elif vastus==1:
        inimesed,palgad=andmete_lisamine(inimesed,palgad)
    elif vastus==2:
        inimesed,palgad=andmete_kustutamine(inimesed,palgad)
