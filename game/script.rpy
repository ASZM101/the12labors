# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define saraswati = Character("Saraswati")
define artemis = Character("Artemis")
define kannon = Character("Kannon")
define bellona = Character("Bellona")
define parvati = Character("Parvati")
define danu = Character("Danu")
define maat = Character("Ma'at")
define seshat = Character("Seshat")
define amaterasu = Character("Amaterasu")
define guanyin = Character("Guanyin")
define minerva = Character("Minerva")
define athena = Character("Athena")

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

    

    # This ends the game.

    return
