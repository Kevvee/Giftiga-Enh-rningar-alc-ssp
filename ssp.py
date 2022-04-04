print("Välkommen till Sten, Sax, Påse!")
svar = input("[1] Spela\n[2] Avsluta\n")

if svar == "1":
    print("Du valde att spela spelet!")

if svar == "2":
    print("Du valde att avsluta spelet!")
    exit()

namn = input("Vad vill du heta? ")

print(f"Välkommen till spelet {namn}!")


spelare = 0
bot_score = 0 


while spelare < 3 and bot_score < 3:
    gamer = int(input("Välj\n [1]sten\n [2]sax\n [3]påse\n"))
    import random
    bot = random.randint (1,3)

    if gamer == bot:
        print('Ni valde samma! ingen vann rundan')
    elif gamer == 1: 
        if bot == 2: 
            print(f"{namn} vann rundan! \n Du valde sten \n Boten valde sax")
            spelare += 1
        else: 
            print("Bot vann rundan! \n Du valde sten \n Boten valde påsen")
            bot_score += 1
    elif gamer == 2:
        if bot == 3:
            print(f"{namn} vann rundan! \n Du valde sax \n Boten valde påse")
            spelare += 1
        else:
            print("Bot vann rundan! \n Du valde sax \n Boten valde sten")
            bot_score += 1
    elif gamer == 3:
        if bot == 1:
            print(f"{namn} vann rundan! \n Du valde påse \n Boten valde sten")
            spelare += 1
        else:
            print("Bot vann rundan! \n Du valde påse \n Boten valde sax")
            bot_score += 1

    if spelare == 3: 
        print(f"{namn} grattis du vann!")
        exit()

    if bot_score == 3:
        print(f"Boten vann spelet!")
        exit()

