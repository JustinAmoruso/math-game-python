import random

def intro():
    """allows the player to choose difficulty"""
    print "\n          **WELCOME TO MATH RACER!**\n"
    level = raw_input ("SELECT LEVEL OF DIFFICULTY: \n 1:Easy \n 2:Medium"\
                            "\n 3:Hard \n LEVEL NUMBER: ")
    while True:                    
        try:
            int(level)
        except ValueError:
            level = (raw_input("\n \n~~~YOU MUST ONLY ENTER A LEVEL NUMBER 1, 2, or 3!~~~ \n\n"\
                              "SELECT LEVEL OF DIFFICULTY: \n 1:Easy \n 2:Medium"\
                                "\n 3:Hard \n LEVEL NUMBER: "))
            continue
        if int(level) not in range(1,4):
            level = (raw_input("\n \n ~~~YOU MUST ONLY ENTER A LEVEL NUMBER 1, 2, or 3!~~~ \n\n"\
                              "SELECT LEVEL OF DIFFICULTY: \n 1:Easy \n 2:Medium"\
                                "\n 3:Hard \n LEVEL NUMBER: "))
            continue
        else:
            return level


def race_track(You_score,Red_score,level):
    """displays the game board with updated score represented by each car moving to the right"""
    print "_"*25*int(level)
    print ' '*You_score + "[YOU]" + " "*distance(You_score,level) + "|F|"
    print "-"*25*int(level) + "|I|"
    print "_"*25*int(level) + "|N|"
    print " "*Red_score + "[RED]" + " "*distance(Red_score,level) + "|I|"
    print "-"*25*int(level) + "|S|"
    print "_"*25*int(level) + "|H|"


def distance(score,level):
    """equates size of game board for race_track() based on level chosen in intro()"""
    if score < 0:
        score = 0
    return int((25*int(level))-(score+5))


def question(level):
    """randomly generates a math problem scaled by the difficulty level chosen in the intro"""
    b = ["*","+", "-",]
    e = 9*int(level)
    a = random.randint(1,e)
    d = random.randint(0,2)
    c = random.randint(1,e)
    if d == 2:
        if c > a:
            a,c = c,a
    return str(a) + b[d] + str(c)

def check_for_valid_answer(user_input,problem):
    """checks user input for number or requests another input"""
    while True:
        try:
            int(user_input)
        except ValueError:
            user_input = raw_input("    ~~~YOU MUST ONLY ENTER A NUMBER~~~ \n\n" + "     **TYPE ANSWER AND PRESS [ENTER]**\n" + problem + "= ")
            continue
        else:
            return str(user_input)

def correct_or_wrong(problem,user_input,answer,You_score,Red_score,level):
    """checks for and prints correct or wrong answer and updates You_score and Red_score"""
    while answer != int(user_input):
            print "\n\n          [-[-[- Wrong! -]-]-]\n"
            game_display(You_score,Red_score,level)
            user_input = check_for_valid_answer(raw_input("     "\
                                                          "**TYPE ANSWER AND PRESS [ENTER]**\n"\
                                                          + problem + "= "),problem)
            You_score,Red_score = game_movement(You_score,Red_score,user_input,answer,level)
            if Red_score >= distance(0,level):
                Red_score = distance(0,level)
                break            
    if answer == int(user_input):
        print "\n\n          <+<+<+ Correct! +>+>+>\n"
        You_score,Red_score = game_movement(You_score,Red_score,user_input,answer,level)
    return You_score,Red_score    


def movement(user_input,answer,level):
    """generates an amount to move each player based on correct or wrong player answer for game_movement()"""
    you_move = 0
    red_move = 0
    if int(user_input) == answer:
        you_move += random.randint(1,(2*int(level)))
        red_move += random.randint(-3,(2*int(level)))
    elif int(user_input) != answer:
        you_move += random.randint((-2*int(level)),0)
        red_move += random.randint(1,(3*int(level)))
    return you_move, red_move

            
def game_movement(You_score,Red_score,user_input,answer,level):
    """updates and returns You_score and Red_score for correct_or_wrong()"""
    you_spaces = movement(user_input,answer,level)[0]
    red_spaces = movement(user_input,answer,level)[1]
    You_score += you_spaces
    Red_score += red_spaces
    if game_end(You_score,Red_score,level) is not True:
        return You_score,Red_score
    if You_score <= 0:
        You_score = 0
    elif Red_score <= 0:
        Red_score = 0
        
    return You_score,Red_score


    

def game_end(You_score,Red_score,level):
    """checks if either player has reached the end of the game"""
    if max(You_score,Red_score) >= distance(0,level):
        if You_score > Red_score:
            You_score = distance(0,level)
            print "\n       <+<+<+<+<+<+<+  YOU WIN!!!  +>+>+>+>+>+>+>"
            return False
        else:
            Red_score = distance(0,level)-1
            print "\n  [-[-[-[-[-[-[-   YOU LOSE...RED WON   -]-]-]-]-]-]-]"
            return False
    return True

def game_display(You_score,Red_score,level):
    """displays the current game board"""
    if min(You_score,Red_score) < 0:
        if You_score < 0:
            You_score = 0
        else:
            Red_score = 0
    if max(You_score,Red_score) >= distance(0,level):
        if You_score > Red_score:
            You_score = distance(0,level)
        else:
            Red_score = distance(0,level)-1
    race_track(You_score,Red_score,level)
    print "Your Sore:",You_score,"\nRed Score:",Red_score


def check_for_play_again(answer):
    """asks player if they want to play again at end of game"""
    loc = "yesno".find(str.lower(answer))
    while loc == -1:
        answer = raw_input("\nWANNA TRY AGAIN?\nY or N: ")
        loc = "yesno".find(str.lower(answer))
        continue
    if "yesno".find(str.lower(answer)) == 0:
        return True
    else:
        print "you said no"
        return False
    

def play_game(level):
    """calls all functions needed to play the game"""
    You_score,Red_score = 0,0
    while game_end(You_score,Red_score,level):
        problem = question(level)
        user_input = check_for_valid_answer(raw_input("     "\
                                                      "**TYPE ANSWER AND PRESS [ENTER]**\n"\
                                                      + problem + "= "),problem)
        answer = eval(problem)
        You_score,Red_score = correct_or_wrong(problem,user_input,answer,You_score,Red_score,level)
        game_display(You_score,Red_score,level)
    return check_for_play_again("J")



def my_first_game():
    """creates a loop to allow continuous playing"""
    while play_game(intro()) is True:
        continue
    #if play_game(intro()) is False:
    else:
        print "THANKS FOR PLAYING MATH RACER"
    return


        
my_first_game()

        
    
    
