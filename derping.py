hoog = 100
laag = 0
getal = int((hoog - laag)/2 + laag)
print (getal)
geheim_getal=int(input("Kies een getal tussen de 1 en 100 :"))
#print (type(geheim_getal))
while True:
    vraag = "Is het getal hoger of lager dan "+str(getal)+"(h/l)? "
    hl=input(vraag)
    print (hl)
    if hl == "l" :
        print("U koos lager")
        hoog = getal
    if hl == "h":
        print("U koos hoger")
        laag = getal
    getal = int((hoog - laag)/2 + 0.5 + laag)
    if hoog - laag == 2:
        print ("Het getal moet "+str(getal)+" zijn!")
    print (hoog,laag,getal)
