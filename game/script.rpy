# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define one = Character("Athena")
define two = Character("Artemis")
define three = Character("Parvati")
define four = Character("Guanyin")
define five = Character("Ma'at")
define six = Character("Danu")
define seven = Character("Saraswati")
define eight = Character("Kannon")
define nine = Character("Amaterasu")
define ten = Character("Seshat")
define eleven = Character("Minerva")
define twelve = Character("Bellona")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

  
    # Dialogue format:
    # characterVariable "Dialogue"


label trial_8:       
    $ score = 0
    nine "lets see how much you know about the Sun. If you know enough, I might let you move on"
    nine "first question, how old is the Sun?"
    menu: 
        "6-7 billion years":
           "Incorrect. Lets try another" 

        "4.5 billion years":
            "CORRECT. Keep going!"
            $ score +=1

    nine "next question, how long does it take the sun to rotate on its axis?"
    menu:
        "27 days": 
            nine"Correct, one more!"
            $ score +=1
        "18 days":
            nine"Incorrect, Try one more time"

    nine "last question, do you love Mr.Sun?"
    menu:
        "Yes":
           nine"Thank you for not putting no. You don't know how many people put that answer"
           $ score +=1 
        "No":
           nine "You humans are ungrateful. Moving on . . ."
    if score>1:
        nine "congratulations! You are able to pass to the next level!"
    else:
        "You have failed the test and will suffer a horrible fate. Sorry"


label trial_9:
    $ score=0
    ten "What someone knows affects their decisions. Prove your knowledge in this test and show your worth"
    ten "Your first question shall be . . . what is the definition of CAMADERIE?"
    menu:
        "social and friendly":
            ten "Correct!!!Keep going"
            $ score +=1
        "formal and neutral":
            ten "No, do better"
    ten "Next question! What does ACCOLADE mean?"
    menu:
        "Harsh and mean":
            ten"Incorrect; I am NOT accolade when I say that this is why your grades are so low"
        "Praise and attention":
            ten "Correct! Last one!"
            $ score +=1
    ten "The Big question . . . What does IDK mean?!"
    menu:
        "I Don't Know":
            ten "Actually, I Don't Kare! HA . . Just kidding, I'll give it to you"
            $ score +=1
        "I Don't Kare":
            ten "We need to talk about your spelling"
    if score>1:
        ten "Yes! You have made it passed my vocabulary quiz and may go forward on your journey"
    else:
        ten "Whomp Whomp. Your dead. Bye"
    eleven "What we do in life must be based on strategy. Choose the best move in Chess"
    twelve""

    # This ends the game.

    return
