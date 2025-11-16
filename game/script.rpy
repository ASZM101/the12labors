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

label maatScene:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene maat

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    # Dialogue format:
    # characterVariable "Dialogue"
    five "In order to succeed in life you need to settle disputes and maintain order."
    
    menu:

        five "Are you ready to be the seeker of justice?"

        "Yes":
            five "Excelent"

        "I don't Know...":
            five "ok then parish"
            return


label danuScene:


    scene danu

    six "I love plants! Which one is your favorite?"

    menu:

        "Uh. Flowers?":

            six "Which kind?"

            menu:

                "um. the colorful kind?":
                    six "I don't like you *Smites you*"
                    return

                "Chrysanthemum!":
                    six "Nice! Me Too!"

                "Lavender!":
                    six "Cool!"

        "I Love Trees!":
            six "Which kind?"

            menu:

                "Oak":
                    six "NICE"

                "Willow":
                    six "Me Too!"

                "Coconut":
                    six "Interesting"

    six "Let's see if you're a true plant lover!"




label swatiScene:

    scene swati

    seven "I am the Hindu goddess of art and knowledge. To test both, you have to name the paintings."

    menu:
        "I'm ready!":
            "jump guessPainting"

        "I'm not ready!!!":
            seven "Ok then parish *Smites you* 67 67 67 "
            return


label kannonScene:
    scene kannon

    eight "Do you have compassion in your heart?"

    menu:
        "Yes":
            eight "We shall see."

        
        "Yes?":
            eight "You are  unsure of yourself. Nevertheless, we shall see."

        "No":
            eight "We shall see..."








#label badEnding:














