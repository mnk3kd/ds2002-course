#!/bin/bash


clear
echo "Let's build a mad-lib!"

read -p "1. Tell me your name:" NAM
read -p "2. What is your favorite color?" COL
read -p "3. What state are you in?" STATE
read -p "4. Tell me your favorite ice cream flavor:" FLAV
read -p "5. Pick one: enraged or angry." MAD
read -p "6. Chocolate or candy?" SWEET
read -p "7. What country would you like to visit?" COUNTRY
read -p "8. How old are you?" AGE

echo "Last week, I started a non-profit called the $NAM organization. They are based in the state of $STATE and focus on helping impoversished children in $COUNTRY. However, we are already having issues. The NPO is $AGE people large, but instead of creating progress and change, I've noticed several problems  in the budget. It seems that my employees having been ordering excessvie amounts of $FLAV $SWEET. I have never been more $MAD." 
