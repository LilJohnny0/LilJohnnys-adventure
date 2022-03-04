
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
                        answer = input("The village gives you free stuff. You decide to live with them. You've completed the story. ")

                    

                       
            elif answer == "hide":
                answer = input("You enter a cave, would you like to camp there? (yes/no?) ")


                if answer == "yes":
                    print("You got radioactive posioning and died. GAMEOVER")

                elif answer == "no":
                    answer = input("You exit the cave and the forest is on fire. Would you like to leave the forest, or put out the fire (leave/putout) ")

                    if answer == "leave":
                        answer = input("You leave the forest, and go into a desert. You're very thirsty and need water. Would you like to look for water or keep walking? (look/walk) ")

                        if answer == "look":
                            print("you look for water and you stumble across Posedion. He takes you hostage and you live with him.")
                            print("You completed the story!")

                        elif answer == "walk":
                            print("You get too dizzy and walk into a cactus. GAMEOVER")


                    elif answer == "putout":
                        answer = input("You put out the fire and some people living near by thank you! they give you food, and they ask you if you would like to live with them. (yes/no) ")
                        
                    if answer == "yes":
                        print("You live with the people nearby, and you completed the story.") 

                    elif answer == "no":
                        print("You keep walking and stumble across a group of indians. You are taken hostage and forced to live with them.")
                        print("You end up enjoying being one of them, and live with them. You completed the story.")




                


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

                if answer == "yes":
                    print("you now live with Jimmy the farmer, you've completed your story.")

                elif answer == "no":
                    print("you go on your way, away from Jimmy the farmer")
                    answer = input("before you can think about where to go next a pack of wolvs surround you!!! would you like to fight or pray (fight/pray) ")

                    if answer == "pray":
                        print("You see God, and you ascended up into heaven. You've completed the story.")

                    elif answer == "fight":
                        print("You succefully kill the pack of wolves, but you bleed out and die. GAMEOVER")

                        
                    

                
                        



             if answer == "disarm":
                 print("The farmer stabbed you, you bleed to death and die. GAMEOVER")

        elif answer == "run":
            print("The bear cuts you on your arm and bleed to death. GAMEOVER")

            
        
        

            




        

    else:
        print("game terminated!")