# Connect Four

This is a connect four python game displayed in the console. It allows for multiple players -- representing different colors -- and other customizations. (Board size, Num in a row to win).

I made this because I was curious how to add color in python print statements and it taught me ANSI escape codes. 


## Features

- Multiple Players
- Customizeable Board size
- Customizeable required in a row to win
- Quick to Play
- Fast Algorithms


## How-To-Play

#### Requirments:
- Python 3.0~ installed
- Know how to download a python file and launch it in a terminal
    - You can use vscode, thats what I do

#### Next:
Ignore all the other files in the repo and download `Connect-Four.py` then launch the python file. 
> or you can copy and paste the code into a python file and run that. 
    
## Roadmap

- Save player customizations 

- Increase max size of board allowed


## FAQ

#### How do I change the number of players?

Once you run the python file you will be asked `Would you like to customize your game?` then asnwer with `yes` you will be asked the dementions of the board (you can change these if you'd like) but then after that you will be asked `Number of Players?` and you can imput all the way up to 6 (inclusive) 

#### Does it save my custom game preferences?

No, mostly because when showming people my game I always changed it and did not structure that inmind. It is currently on the road map because I have to restucutre the main game() function for it to save them. 


## Optimizations

What optimizations did you make in your code? 
- I put the color codes inside a class so the code is more readable
- Instead of copy and pasteing the disctionary holding all the color keys i made a function to simply return it, making code more readable
- I made all the algorithms for checking for wins stop imeditly if there was not a peice in line
- I made the win checking algoritms indivdual instead of all in one
- I only passed a cordanate to the check_for_win() function if it had a peice in it 
- I put the customize questions into a dictionary to allow me to change or add them in the future. Keep in mind the min and max and defaults for the questions are stored in the dictionary also. 


## Appendix

Hope you have fun!
