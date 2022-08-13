from UI.ui import *


def main():
    ui = UI()
    ui.welcome()
    ui.play()
    check = input("Do you want to play again?(y/n) ")
    if check == 'y':
        main()


if __name__ == "__main__":
    main()
