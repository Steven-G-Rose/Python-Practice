import random

#These variables are used later on in main loop.
discard_selection = 0
card_attack = 0
discard_value = 0

#These arrays create the deck of cards that player will pull from
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

#This array combines the suits and faces to finish creating the "tavern" deck, then shuffles them
tavern = []
for suit in suits:
    for face in faces:
        tavern.append((face, "of", suit))
##        random.shuffle(tavern)
        
#This list is the discard pile.
discard = []
        
#Similar to cards array, but just for jacks.
jacks = []
for suit in suits:
    jacks.append(("Jack", "of", suit))
    random.shuffle(jacks)
    
#Similar to jacks array, but just for queens.
queens = []
for suit in suits:
    queens.append(("Queen", "of", suit))
    random.shuffle(queens)

#Similar to queens array, but just for kings.
kings = []
for suit in suits:
    kings.append(("King", "of", suit))
    random.shuffle(kings)

boss_deck = jacks + queens + kings

#This creates the array to store the player's cards and creates the player's hand with a hand size of 8.
player = []
hand = 0
while hand != 8:
    player.append(tavern[hand])
    tavern.pop(hand)
    hand += 1

#This variable starts the game with the first boss which will be the first card in the Jacks deck.
current_boss_select = 0
current_boss = boss_deck[current_boss_select]
boss_hp = 20
boss_attack = 10
print("Current boss is " + str(current_boss))

#This loop is the logic for playing cards for the current boss.
while hand > 0:
    
    #This prints information about the current boss and the player's hand.    
    print("Boss HP: " + str(boss_hp))
    print("Boss Attack: " + str(boss_attack))

    #Print player's hand in an easy to read format.
    print("Your hand is: ")
    card = 0
    while card != hand:
        #The +1 here is to make it easier to read (so that cards 1 through 8 aren't printed as 0 through 7)
        print(str(card + 1) + ":" + str(player[card]))
        card += 1

    user_selection = int(input("Enter card to play: "))
    played_card = player[user_selection - 1]

    #Logic for player cards.
    if "A" in played_card:
        card_attack = 1  
    if "2" in played_card:
        card_attack = 2
    if "3" in played_card:
        card_attack = 3
    if "4" in played_card:
        card_attack = 4
    if "5" in played_card:
        card_attack = 5
    if "6" in played_card:
        card_attack = 6
    if "7" in played_card:
        card_attack = 7
    if "8" in played_card:
        card_attack = 8
    if "9" in played_card:
        card_attack = 9
    if "10" in played_card:
        card_attack = 10
    if "Jack" in played_card:
        card_attack = 10
    if "Queen" in played_card:
        card_attack = 15
    if "King" in played_card:
        card_attack = 20

    if "Spades" in played_card:
        boss_hp -= card_attack
        boss_attack -= card_attack
    if "Clubs" in played_card:
        boss_hp -= card_attack * 2
##    if "Hearts" in played_card:
         

    print("You have played: " + str(played_card))
    player.pop(user_selection - 1)
    hand -= 1
    
    print("Boss does " + str(boss_attack) + " damage.")
    boss_damage = boss_attack
 
    while boss_damage > discard_value:
        print("Choose which card to discard to take damage.")
        card = 0
        while card != hand:
            #The +1 here is to make it easier to read (so that cards 1 through 8 aren't printed as 0 through 7)
            print(str(card + 1) + ":" + str(player[card]))
            card += 1
        user_selection = int(input("Enter card to discard: "))
        played_card = player[user_selection - 1]
        if "A" in played_card:
            discard_value += 1  
        if "2" in played_card:
            discard_value += 2
        if "3" in played_card:
            discard_value += 3
        if "4" in played_card:
            discard_value += 4
        if "5" in played_card:
            discard_value += 5
        if "6" in played_card:
            discard_value += 6
        if "7" in played_card:
            discard_value += 7
        if "8" in played_card:
            discard_value += 8
        if "9" in played_card:
            discard_value += 9
        if "10" in played_card:
            discard_value += 10
        if "Jack" in played_card:
            discard_value += 10
        if "Queen" in played_card:
            discard_value += 15
        if "King" in played_card:
            discard_value += 20
        discard.append(player[user_selection])
        player.pop(user_selection - 1)
        hand -= 1
        if boss_damage > discard_value:
            print("Remaining value to discard is: " + str(boss_damage - discard_value))

    print("Tavern deck: " + str(len(tavern)))
    print("Discard pile: " + str(len(discard)))

    discard_value = 0
    
    if boss_attack < 0:
        boss_attack = 0
    if boss_hp <= 0:
        print("Boss defeated!")
        current_boss_select += 1
        current_boss = boss_deck[current_boss_select]
        if "Jack" in current_boss:
            boss_hp = 20
            boss_attack = 10
        if "Queen" in current_boss:
            boss_hp = 30
            boss_attack = 15
        if "King" in current_boss:
            boss_hp = 40
            boss_attack = 20
        print("Current boss is " + str(current_boss))
