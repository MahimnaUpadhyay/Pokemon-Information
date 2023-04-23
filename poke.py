import pokebase as pb
import webbrowser


def fetch_info():

    name=input("Enter pokemon name: ") 
    print("fetching info")
    pokeinfo=pb.pokemon(name)

    print("Command list:\n 1.height \n 2.weight \n 3.image ")
    cmd=int(input(("Enter what do you want? ")))

    if cmd==1:
        print(pokeinfo.height)

    elif cmd==2:
        print(pokeinfo.weight)

    elif cmd==3:
        webbrowser.open(pokeinfo.sprites.front_default)

    else:
        print("Enter correct command")

fetch_info()