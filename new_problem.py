import random

def game():
    
    #creating new txt file
    
    num = "0"
    with open("highscore.txt", "w") as f:
        f.write(num)
    
    #generating the score
    
    score = random.randint(1,100)
    print(f"your high score is: {score}")
    
    # fetching the highscore from txt file
    
    with open("highscore.txt") as file:
        highscore = file.read()
        print(f"preivous high score is:{highscore}")
        
    # Conditons
    
    if(str(score)>str(highscore)):
        with open("highscore.txt","w") as file:
            file.write(f"{score}")
            
game()
            
        
    
    
    