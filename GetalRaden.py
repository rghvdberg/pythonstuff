hoog = 100
laag = 0
getal = int((hoog - laag)/2 + laag)
Geraden = False
geheim_getal=input("Kies een getal tussen de 1 en 100 en druk op [ENTER] om verder te gaan.")

while Geraden == False:
    vraag = "Is het getal hoger of lager of gelijk aan "+str(getal)+"(h/l/g)? "
    hl=input(vraag)

    if hl == "g" :
        print ("Het getal is "+str(getal)+".")
        Geraden = True

    if hl == "l" :
        print("U koos lager")
        hoog = getal

    if hl == "h":
        print("U koos hoger")
        laag = getal

    getal = int((hoog - laag)/2 + 0.5 + laag)
    if hoog - laag == 2:
        print ("Het getal moet "+str(getal)+" zijn!")
        Geraden = True
