#!/usr/bin/python3


FAV_SONG = input('What is your favorite song? ')
ETHNICITY = input('What is your ethnicity? ')
ALLERGY_TO_NUTS = input('True or false, are you allergic to nuts? ' )

import os
os.environ["MY_FAV_SONG"] = FAV_SONG
os.environ["MY_ETHNICITY"] = ETHNICITY
os.environ["MY_ALLERGY_TO_NUTS"] = ALLERGY_TO_NUTS


print("My favorite song is :", os.getenv("MY_FAV_SONG"))
print("My ethnicity is :", os.getenv("MY_ETHNICITY"))
print("The claim that I have a nut allergy is ", os.getenv("MY_ALLERGY_TO_NUTS"))


