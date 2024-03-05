import time

treelord = 25
you = 20
other_other_ending_bool = False #bool to skip ending code
bad_ending_bool = True #bool to skip other ending code
axe_bool = True #bool to check if axe exists
other_axe_bool = False #another bool to check if axe exists
items = []
item1 = input("Choose an item to begin your journey p320 9mm pistol (P), remington 700 bolt action rifle (B), KaBar knife (K), Sheild (S), or mysterious tube of liquid (L): ") #asks the user for their first item choice
item1 = item1.upper()
items.append(item1)
time.sleep(1)
item2 = input("Choose another item: money($), Medic kit (M) or frying pan (F): ")
item2 = item2.upper()
items.append(item2)
time.sleep(1)
choice1 = input("You are walking at a park and find a out of place cobblestone path leading to some trees you've never seen before do you follow (F) it or go on your way (G)?: ") #asks the user for the 2nd item choice
if choice1 == "G": #checks if you go into the woods
  time.sleep(1)
  print("The boring ending: You go about your day normally.")
elif choice1 == "F": #if you go into the woods the game starts
  print("You enter the woods an the entrance seems to close behind you in a thick grove.")
  time.sleep(1)
  path = input("Do you go on the left (L), right (R) or middle path (M)?: ")
  if path.upper() == "L": #incomplete checks for path left is taken
    print("You take the left path")
    time.sleep(1)
    print("No-one is there but you hear rusteling noise")
    time.sleep(1)
    path1 = input("There is another path divergence do you go towards the ruselting noise (T) or away from it (A): ") #path input
    path1 = path1.upper()
    if path1 == "A":
      time.sleep(1)
      bush_choice = input("Do you try to go through the bushes (G) or cut through them (C): ")
      bush_choice = bush_choice.upper()
      if bush_choice == "C":
        if item1 != "K": #checks for knife if the user wants to cut
          for bush_choice in "G":
            time.sleep(1)
            print("You don't have a knife.")
            time.sleep(1)
            bush_choice = input("Do you try to go through the bushes (G) or cut through them (C): ")
            
        else: #checks for if you want to heal
         time.sleep(1)
         heal = input("You see a person lying on the ground almost dead do you continue (C) or heal the person (H): ")
         heal = heal.upper()
         if heal.upper() == "H":
           if items[1].upper() == "M": #checks if the user has a medkit
             time.sleep(1)
             print("The even better ending: the person blesses you with good luck for saving him you continue into a light getting home satfley. You have slightly better luck from now on!")
           else: #if the user dosen't have a medkit
             time.sleep(1)
             print("The slightly less good ending: you coudldn't heal the person so you walked into a light teleporting home while feeling guilty that you didn't bring a medic kit.")
         if heal.upper() == "C": #if the user decides to heal
           if items[1].upper() == "M": #if the user dosen't have a medkit
             time.sleep(1)
             print("The neutral ending: You decided not to heal the person you feel guilty for a while aftering returning home via walking further along the path into a light.")
           else: #if the user has a medkit
             time.sleep(1)
             print("The slightly less good ending: you coudldn't heal the person so you walked into a light teleporting home while feeling guilty that you didn't bring a medic kit.")
      
      elif bush_choice == "G": #if the user decides to go through the bush 
        time.sleep(1)
        print("Backrooms ending: You no-clip due to the density of the bushes and are now in the backrooms")
    elif path1 == "T": #if the user goes toward the sound
      time.sleep(1)
      print("You see a mysterious figure rapidly going toward you")
      time.sleep(1)
      quicktime = input("Do you run (R) or hide (H): ")
      if quicktime.upper() == "R": #if the user decides to run
        time.sleep(1)
        run_choice = input("Do you do a quiet jog (J) or a loud sprint (S): ")
        if run_choice.upper() == "J": #if the users tries to jog quietly
          time.sleep(1)
          print("The stealth ending: You stealthily get away from the mysterious figure and are teleported back home.")
          
        else: #if user tries to run loudly
          time.sleep(1)
          print("The stupid ending: the mysterious figure hears you and kills you since you couldn't outrun him")
          
      if quicktime.upper() == "H": #if the user tries to hide
        time.sleep(1)
        print("The did you think that one out ending: He finds your hiding location that you frantically made and he kills you.")
        
  elif path.upper() == "R": #checks for path input
    time.sleep(1)
    print("You meet a large statue of a man with a bucket on his head with a pan.")
    time.sleep(1)
    print("You hear a voice in your head that says \"greetings my friend do you have any pans or oil\" ") #print statement with quotes inside it
    time.sleep(1)
    no_choice = input("Do you leave (L) or stay (S): ")
    if no_choice.upper() == "L":
      for no_choice in "L": #forces the user into a loop they can't leave unless they stay with the statue
        time.sleep(1)
        print("You cannot leave a force compels you.")
        time.sleep(1)
        no_choice = input("Do you leave (L) or stay (S): ")
    if items == ['L','F']: 
      time.sleep(1)
      print("The statue is very pleased with due to your appreacation of the superior objects of a frying pans and oil.")
      time.sleep(1)
      print("The best but stupid ending: You asscend due to showing the statue a pan with special oil in it and you achive acension.")
    elif items[0].upper() == "L": #checks for oil
      print("The statue looks midly pleased with you since you brough mysterious oil.")
      time.sleep(1)
      print("The stupid but good ending: The statue waves his pan and he teleports you to the doostep of your house.")
    elif items[1].upper() == "F": #checks for frying pan
      print("The statue looks midly pleased with you since you brough a frying pan.")
      time.sleep(1)
      print("The other stupid but good ending: The statue waves his pan and he teleports you to the doostep of your house.")
      #ending
    else:
      print("The statue is very displeased with you.")
      time.sleep(1)
      print("The worst but stupid ending: You are dammed for eternity by not having a pan or oil.")
      #ending
  elif path.upper() == "M":
    print("You arrive at a village")
    time.sleep(1)
    print("The villagers seem distressed")
    time.sleep(1)
    print("One of the villagers tells you that the tree lord is torrizing the town!")
    time.sleep(1)
    shop = input("There's a shop nearby do you go to it (G) or continue (C): ")
    time.sleep(1)
    if shop.upper() == "G":
      if item2 != "$":
        print("You don't have money to spend.")
        #checks if the user has money
      elif item2 == "$":
        shop_item = input("Buy one of these: mysterious potion (P) or axe (A): ")
        shop_item = shop_item.upper()
        #shows shop items
        items.append(shop_item)
        if shop_item.upper() == "A":
          axe_bool = False
          other_axe_bool = True
    time.sleep(1)
    print("You find the tree lord.")
    if items[0].upper() != "P":
      #checks for pistol
      if items[0].upper() != "B":
        #checks for bolt action rifle
        if items[0].upper() != "K":
          #checks for knife
          if axe_bool: #if the user dosen't have a weapon and bought something other than the axe they can't fight the tree lord
            time.sleep(1)
            print("The bad ending: you die from the tree lord because you couldn't fight it")
            bad_ending_bool = False #makes it so that it skips the combat code

    if items[0].upper() == "P": #esablishes variables for weapon
      l = "pistol "
      b = "P"
    elif items[0].upper() == "B": #establishes variables for weapon to refer to
      l = "remington 700 "
      b = "B"
    elif items[0].upper() == "K": #establishes weapon for combat to refer to
      l = "knife "
      b = "K"


    treelord_bool = True #bool that checks if the treelord's hp is above 0
    you_bool = True #bool that checks if your hp is above 0
    #establishes variables for the battle
    while treelord_bool and you_bool and bad_ending_bool: #checks if the hp of treelord is above 0
      treelord_attack = 4  #restores treelord's attack if the user has blocked the last turn
      option = input("Do you: 1. attack or 2. block: ")
      if option == "1":
        if "A" in items and items[0] != "S" and items[0] != "L": #checks if axe is in the items
          attack_option = input("Do you attack with your " + l + "(" + b + ")" " or your axe (A): ") #if the user has a main weapon and a axe
          attack_option = attack_option.upper()
          if attack_option.upper() == "P":
            if "P" in items: #checks for pistol option
              print("You shoot the treelord with your pistol dealing 6 damage to it!")
              treelord -= 6
              time.sleep(1)
              print("The treelord attacks and you took 5 damage!")
              time.sleep(1)
              print("Your hp is ", you)
              time.sleep(1)
              print("The treelord's hp is ", treelord)
            else: #if the user dosen't pick pistol it picks axe
              print("You hit the treelord with your axe dealing 8 damage to it")
              treelord -= 8
              time.sleep(1)
              print("The treelord attacks and you took 6 damage")
              you -= 6
              print("Your hp is ", you)
              time.sleep(1)
              print("The treelord's hp is ", treelord)
          elif attack_option.upper() == "B":
            if "B" in items: #checks for bolt action rifle
              print("You shoot the treelord with your remington 700 dealing 4 damage to it!")
              treelord -= 4
              time.sleep(1)
              print("The treelord attacks and you took 3 damage!")
              you -= 3
              time.sleep(1)
              print("Your hp is ", you)
              time.sleep(1)
              print("The treelord's hp is ", treelord)
          elif attack_option.upper() == "A":
            if "A" in items:

              print("You hit the treelord with your axe dealing 8 damage to it")
              treelord -= 8
              time.sleep(1)
              print("The treelord attacks and you took 6 damage!")
              you -= 6
              time.sleep(1)
              print("Your hp is ", you)
              time.sleep(1)
              print("The treelord's hp is ", treelord)
            else:
              print("item dosen't exist")
          elif attack_option.upper() == "K":
            if "K" == items[0]: #checks for kabar
              time.sleep(1)
              print("You hit the treelord with your knife dealing 3 damage to it!")
              treelord -= 3
              time.sleep(1)
              print("The treelord attacks and you took 6 damage!")
              you -= 6
              time.sleep(1)
              print("Your hp is ", you)
              time.sleep(1)
              print("The treelord's hp is ", treelord)
            else:
              print("Item dosen't exist")
          elif attack_option.upper() == "dummy_function_since_I_couldn't_debug_an_issue_where_it_said_the_last_item_in_this_didn't_exist": #dummy if statement I had an issue where the item check before the else statment would return that it dosen't exist even if the item does
            if "Afwefejfwinvrvaiwfeujff" in items:
              print("You hit the treelord with your axe dealing 9999999999999 damage to it")
              treelord -= 99999999999999999
              time.sleep(1)
              print("The treelord attacks and you took 1 damage!")
              you -= 1
              time.sleep(1)
              print("Your hp is ", you)
              time.sleep(1)
              ("The treelord's hp is ", treelord)
          else: #if the user enters a letter for a weapon that dosen't exist
            print("Item does not exist")
            time.sleep(1)
        else:
          if items[0] == "P": #checks for pistol
            print("You shoot the treelord with your pistol dealing 6 damage to it!")
            treelord -= 6
            time.sleep(1)
            print("The treelord attacks and you took 5 damage!")
            you -= 5
            time.sleep(1)
            print("Your hp is ", you)
            time.sleep(1)
            print("The treelord's hp is ", treelord)
          elif items[0] == "B": #checks for bolt action rifle
            print("You shoot the treelord with your remington 700 dealing 4 damage to it!")
            treelord -= 4
            time.sleep(1)
            print("The treelord attacks and you took 3 damage!")
            you -= 3
            time.sleep(1)
            print("Your hp is ", you)
            time.sleep(1)
            print("The treelord's hp is ", treelord)
          elif items[0] == "K": #checks for ka bar
            print("You hit the treelord with your knife dealing 3 damage to it!")
            treelord -= 3
            time.sleep(1)
            print("The treelord attacks and you took 6 damage!")
            you -= 6
            time.sleep(1)
            print("Your hp is ", you)
            time.sleep(1)
            print("The treelord's hp is ", treelord)
          elif other_axe_bool: #checks for axe if the user dosen't have a item in the first slot
            print("You hit the treelord with your axe dealing 8 damage to it")
            treelord -= 8
            time.sleep(1)
            print("The treelord attacks and you took 6 damage!")
            you -= 6
            time.sleep(1)
            print("Your hp is ", you)
            time.sleep(1)
            print("The treelord's hp is ", treelord)

      elif option == "2": #checks for blocking options
        if items[0].upper() == "S": #checks for sheild
          print("You block the attack with your sheild. The treelord only deals 0.5 damage!")
          you -= 0.5
          time.sleep(1)
          print("The treelord takes 1 damage in recoil!")
          treelord -= 1
          time.sleep(1)
          print("Your hp is ", you)
          time.sleep(1)
          print("The treelord's hp is ", treelord)
        else: #does normal block if it isn't
          print("You block the attack with your fists. The treelord deals 1.5 damage.")
          you -= 1.5
          time.sleep(1)
          print("The treelord takes 1 damage in recoil!")
          treelord -= 1
          time.sleep(1)
          print("Your hp is ", you)
          time.sleep(1)
          print("The treelord's hp is ", treelord)

      else: #if the user dosen't enter in a valid attack
        print("That's not valid")
        time.sleep(1)
      if you <= 0: #what happens if the player's hp reaches 0
        you_bool = False
        other_other_ending_bool = True

      if treelord <= 0: #what if the treelord reaches 0 hp
        treelord_bool = False
        other_other_ending_bool = True


other_ending_bool = True

if you <= 0 and treelord <= 0:
  
  if "P" in items and other_other_ending_bool == True:
    print("The suprisingly good ending: Both you and the treelord die fighting but the shopkepper you bought from rushes to your corpse and gives you the mysterious potion, saving you!")
    
  elif "P" not in items and other_other_ending_bool == True: #checks for various variables for the endings
    print("The kind of bad ending: Both you and the treelord land one last strike on each other killing you both the village makes a statue in your honor.")
    other_ending_bool = False
if you <= 0 and other_ending_bool == True and other_other_ending_bool == True: #checks for various variables for the endings
  print("The bad ending: you died trying to fight the treelord")
  other_ending_bool = False
if treelord <= 0 and other_ending_bool == True and other_other_ending_bool == True: #checks for various variables for the endings
  print("The good ending: you defeated the treelord and the village is saved you are rewarded a bottle that teleports you back home.")
  other_ending_bool = False
