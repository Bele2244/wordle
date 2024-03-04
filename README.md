# Wordle
#### Video Demo:  <https://youtu.be/WG57XrPWbVI>
#### Description:
The program is created as a Harvard CS50 final project using the Python programming language. 
It is run in the command prompt (cmd). After running the program, the user can choose the 
difficulty and subject from which a random word is selected. The user can then try to guess 
the word.

### Features

## Difficulty
The user can choose the difficulty level of the program, which determines the number of  
attempts allowed:  
Easy: The user will have 9 tries to guess the randomly selected word from the chosen subject.  
Medium: The user will have 6 tries to guess the randomly selected word from the chosen subject.
Hard: The user will have 3 tries to guess the randomly selected word from the chosen 
subject.     

## Subject
The user can choose from 5 subjects:
1.Animals  
2.Countries  
3.Disney movies  
4.Vegetables  
5.Fruits  
Once the user selects a subject and the input is valid, the subject is passed to the 
'get_word' function, which calls the 'load_csv' function. The 'load_csv' function returns a   
list of words for the given subject. Subsequently, the 'get_word' function utilizes the 
random   
module to select a word randomly from the list and returns it. 

## Game
When the game starts, the program will display the length of the randomly chosen word. The 
user can then try to guess the word by typing the whole word. After the user inputs their 
guess, each character in the user input is compared to the corresponding character in the 
word.  
If the character in the user input matches the character in the word and is in the same  
position, the character is colored green using the Colorama module.  
If the character in the user input matches a character in the word but is in a different  
position, the character is colored yellow.  
If the character in the user input is not in the word at all, the character is colored red.  

## Resources
All data downloaded from https://copylists.com/  
