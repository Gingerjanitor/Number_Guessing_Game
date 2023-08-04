#A game that:
#1) Asks your name
#2) refers to you by name
#3) randomly draws a number
#3) asks for an input
#5) if the input is too high, it tells you.
#6) if the input is too low, it tells you too.
#7) after a number of tries, it quits and tells you the number.

#my tweaks for added challenge.
#8) in the end, it tells you if you want to play again.
#9) validate inputs- they must be #s
#10) let them define the range
#11) modify the number of chances they get based on the range.
#12) Make it say "last chance!" when they are down to the wire.
#13) Make it randomly sometimes give them a bonus last guess when they run out.
#14) Keep note of how many times they've won/lost across games?
import random
from time import sleep


name=str(input("What is your name?"))
print(f"\n hi {name}! This is a game where I'll pick a number. Then, you will take a guess. \n You've only get a "
      f"limited number of guesses, depending on how hard the game is. Let's do it!"), sleep(.1)
difficulty=(input(("\n first, Pick a difficulty. Enter easy, medium, or hard")))
while difficulty.lower() not in ["easy", "medium", "hard"]:
    difficulty = (input(("\n Something went wrong, you didn't enter the difficulty right. Select a difficulty. Enter easy, medium, or hard")))
print(f"ok, {difficulty} it is!")

if difficulty.lower() in ["easy"]:
    low=1
    high=51
    attempts=6
    print(f"\n {difficulty} mode selects a number between {low} and {high-1}. You've got {attempts} guesses.")

elif difficulty.lower() in ["medium"]:
    low=1
    high=101
    attempts=7
    print(f"\n {difficulty} mode selects a number between {low} and {high-1}. You've got {attempts} guesses.")

elif difficulty.lower() in ["hard"]:
    low=1
    high=201
    attempts=9
    print(f"\n {difficulty} mode selects a number between {low} and {high-1}. You've got {attempts} guesses.")

rounds=int(input("\n One last thing- how many rounds do you want this game to go before I declare a winner? \n"))

def guessgame(low,high, attempts, rounds):


    print(f"\n \n \n \n \nok, let's gooooooO! You're going DOWN, {name}!\n"),sleep(2)
    turn=1
    done = 0
    robotscore = 0
    yourscore = 0
    mercy=0
    while turn<=rounds:
        if done==1:
            print(f"the current score is {robotscore} for me and {yourscore} for you"), sleep(2)
            print("\nAll right, give me a second to come up with a number your puny brain can comprehend..."), sleep(3)
        print(f"\n \n \nRound {turn} go!"), sleep(1)

        thenumber=random.randint(low,high)
        luck=random.randint(1,4)
        guess=0
        tried=1
        done=0
        while tried<=attempts and done!=1:
            if tried<attempts:
                print(f"\n This is guess number {tried}!\n"), sleep(.5)
            if tried == attempts:
                print("\n Last chance!\n"), sleep(2)
                if luck==2 & mercy!=1:
                    print(f"\n Look, I know this is hard for your little human brain. \n"), sleep(2)
                    print(f"\n I'll make it easier for you."), sleep(2)
                    print(f"\n Have another turn. You still won't win.")
                    tried-=1
                    mercy=1
            try:
                guess=int(input(f"Ok, give me a guess! {low} to {high-1}!")), sleep(2)
            except ValueError:
                guess=int(input(f"something went wrong. Give me a guess! {low} to {high-1}!")), sleep(2)
            if guess!=thenumber and tried==attempts:
                randomreply = random.randint(1, 2)
                if randomreply == 1:
                    print(f"BWAHAHA! I win! The number was {thenumber}"), sleep(2)
                if randomreply == 2:
                    print(f"Nope! Looks like I'm the winner! You'd never have figured out that it was {thenumber}!"), sleep(2)
                done=1
                robotscore+=1
                break
            elif guess>thenumber:
                randomreply=random.randint(1,2)
                if randomreply==1:
                    print("Nice try! The number is lower!"), sleep(2)
                if randomreply==2:
                    print("Nope! the number is lower!"), sleep(2)
                tried+=1
            elif guess<thenumber:
                randomreply = random.randint(1, 2)
                if randomreply == 1:
                    print("You whiffed it! The number is higher!"), sleep(2)
                if randomreply == 2:
                    print("You're NEVER gonna get this! The number is higher!"), sleep(2)
                tried+=1
            elif guess==thenumber:
                randomreply = random.randint(1, 2)
                if randomreply == 1:
                    print("You got it! I can't believe it!"), sleep(2)
                if randomreply == 2:
                    print("That's it! You won't beat me again!"), sleep(2)
                yourscore+=1
                done=1
                break

        turn+1
    if robotscore>yourscore:
        print("Nice try, human! At least we had fun, right?")
    elif robotscore<yourscore:
        print("No way! How could I lose?!?!?!\n"),sleep(2)
        print("Error"), sleep(1)
        print("Error"), sleep(1)
        print("Error"), sleep(1)
        print("Restarting systems"), sleep(3)

guessgame(low, high, attempts, rounds)

again=input("Shall we play again? y/n?")
while again.lower()=="y":
    guessgame(low, high, attempts, rounds)
    again = input("Shall we play again? y/n?")



print("All right then, I see how it is."), sleep(2)
print("Coward.")
