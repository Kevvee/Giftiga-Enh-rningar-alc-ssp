#print("Välkommen till Sten, Sax, Påse!")
#svar = input("[1] Spela\n[2] Avsluta\n")

#if svar == "1":
    #print("Du valde att spela spelet!")

#if svar == "2":
    #print("Du valde att avsluta spelet!")
    #exit()

#namn = input("Vad vill du heta? ")

#print(f"Välkommen till spelet {namn}!")

import random
gamer = input("Välj\n [1]sten\n [2]sax\n [3]påse\n")

bot = random.randint (1,3)
if gamer == bot:
    print('lika')
