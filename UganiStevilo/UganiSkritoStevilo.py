#-*- coding: utf-8 -*-
import random

def main():
    secret = random.randint(1, 20)


    while True:
        guess = int(raw_input("Vnesi skrito število:"))
        if secret == guess:
              print("Bravo uganil si skrito število! Skrito število je: "+str(secret))
              break

        elif guess > secret:
            print("Vneseno število ni pravo! Število je preveliko.")
        else:
            print("Vneseno število ni pravo! Število je premajhno.")

if __name__ == "__main__":
    main()