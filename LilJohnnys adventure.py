
answer = input("would you like to play? yes or no ")

if answer.lower().strip() == "yes":
        
    answer = input("You are hiking and find a dead end, all there is, is a cliff. (turnaround or jump?)").lower().strip()
       
        #jump
       
    if answer == "jump":
        answer = input("You got swooped up by a velociraptor, scream for help or try to break free (scream/breakfree?) ")

        if answer == "scream":
            print("You angered the velocirapter and it dropped you to your death. GAMEOVER")
        elif answer == "breakfree":
            answer = input("You escaped the velocirapter successfully, would you like to keep running or hide? (run/hide?) ")

            if answer == "run":
                answer = input("You found a mystery berry, would you like to eat it? (yes/no?) ")

                if answer == "yes":
                    print("You just ate a poisonus berry. GAMEOVER")

                elif answer == "no":
                    answer = input("you find a village, would you like to rob or be friendly (rob/friendly?) ")

                    if answer == "rob":
                        print("you made the village mad, and got shot 14 times. GAMEOVER")

                    elif answer == "friendly":
                        answer = input("The village gives you free stuff. Would you like to stay or leave? (stay/leave?) ")

                    if answer == "stay":
                        print("you live with the villagers and now you've completed your story.")

                    elif answer == "leave":
                        print("where would you like to go? (lake/forest) ")

                        if answer == "lake":
                            print("you went to the lake and got eaten by a giant fish. GAMEOVER")

                        elif answer == "forest":
                            print("the forest is on fire and you burned to death. GAMEOVER")



                    




            elif answer == "hide":
                answer = input("You enter a cave, would you like to camp there? (yes/no?) ")


                if answer == "yes":
                    print("You got radioactive posioning and died. GAMEMOVER")

                elif answer == "no":
                    answer = input("you find a deer, would you like to kill it or leave it alone? (kill/leave) ")

                    if answer == "kill":
                        print("The dear killed you. GAMEOVER")

                    elif answer == "leave":
                        print("The dear thought you were ugly and killed you. GAMEOVER")


                


        #turnaround

    elif answer == "turnaround":
        answer = input("You encounter a bear. (run/fight) ")

        if answer == "fight":
            answer = input("The bear takes you into his cave. (plead/escape?) ")
        
        if answer == "plead":
                print("You plead with the bear, you offer it berries, the bear eats your whole arm. GAMEOVER")

        elif answer == "escape":
           print("you passed out for 3 days...")
           answer = input("you wake up on a farm, theres a farmer standing over you with a pitchfork. Disarm or ask for food? (disarm/food")

           if answer == "food":
             print("The farmer give you food.")
             print("The farmer invites you to live with him, and tells you his name is Jimmy.")
             answer = input("what is your name? the farmer asks, tell him or don't tell him. (yes/no?) ")

             if answer == "yes":
                 print("my name is LilJohnny! - you say")
                 answer = input("That is awesome! Would you like to live with me? - Jimmy the farmer says? (yes/no?) ")

                 if answer == "yes":
                     print("you live with Jimmy and now you've completed your story.")

             elif answer == "no":
                print("that's okay, can I just call you friend? - Jimmy says. (yes/no) ")

                if answer == "yes":
                    print("That is fine, I go by anything really. - you say")
                    answer = input("would you like to live with me friend? - Jimmy the farmer says (yes/no) ")

                elif answer == "no":
                    print("you go on your way, away from Jimmy the farmer")
                    print("before you can think about where to go nexta pack of wolvs surround you!!!")
                    print("Jimmy comes and protects you!")
                    print("I changed my mind... Can I live with you? - you exlaim!")
                    print("Jimmy says, OFCOURSE YOU CAN! FRIEND!!")
                    print("you now live with jimmy... you've completed the story")

                
                        



             if answer == "disarm":
                 print("The farmer stabbed you, you bleed to death and die. GAMEOVER")

        elif answer == "run":
            print("The bear cuts you on your arm and bleed to death. GAMEOVER")

            
        
        

            



        else: 
            "Invalid answer..."

        

    else:
        print("game terminated!")