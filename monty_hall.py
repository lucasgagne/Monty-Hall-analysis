import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
''' We will analyze the Monty Hall problem, visualizing the probability law of large numbers, and understanding the superior game strategy.

    The game has 3 doors, one of which contains a prize. Contestants choose a door, after which a door without the prize is opened. 
    Players then have the option to stick with their originally chosen door, or switch doors. 
    
    I will represent the doors as an array of booleans, [False, False, True], where true is the prize door. 
    The prize door and player door will be randomly selected with uniform probability using the Random library. 
'''
def assign_values(doors):
    #Assigns a true value to a random door, returns the index of the true door. 
    doors = [False, False, False]
    x = random.randint(0,2)
    for i in range(len(doors)):
        if i == x:
            # print("test i: ", i)
            doors[i] = True
            # print("updated doors: ", doors)
            
    return x, doors
            
def choose_door(doors):
    x = random.randint(0,2)
    return x

def keep_door(doors, player_door):
    #return the value of the door the player chose, it won't matter whether or not the new door was opened Because the player doesn't switch. 
    return doors[player_door]

def switch_door(player_door, correct_door):
    #There are two possibilities, if the player_door is the correct_door, switching is a loss, so we return false
    #if the player door is not the correct door, the third door is opened, and the player switches to the correct door, so we return true
    return correct_door != player_door
        

def sample_switch_door(repetitions):
    #Calclulate the proportion of wins given a number of repetitions/ trials
    doors = [False, False, False]

    outcomes = []
    for i in range(repetitions):
        prize_door = assign_values(doors)[0]
        player_door = choose_door(doors)
        outcome = switch_door(player_door, prize_door)
        outcomes.append(outcome)
    
    #count the total wins with this strategy and divide by the number of samples
    count = 0
    for outcome in outcomes:
        if outcome == True:
            count +=1
    return count / len(outcomes)

def sample_keep_door(repetitions):
    #Calclulate the proportion of wins given a number of repetitions/ trials
    some_doors = [False, False, False]
    outcomes = []
    for i in range(repetitions):
        some_doors = assign_values(some_doors)[1]
        # print("doors after choosing: ", some_doors)
        player_door = choose_door(some_doors)
        # print("the door the player will choose: ", player_door)
        outcome = keep_door(some_doors, player_door)
        # print("The outcome: ", outcome)
        outcomes.append(outcome)
    
    #count the total wins with this strategy and divide by the number of samples
    count = 0
    for outcome in outcomes:
        if outcome == True:
            count +=1
    return count / len(outcomes)

def create_graph():
    #visualize the difference in outcomes between the two different game strategies. 
    # This analysis displays the probability law of large numbers and gives an intuitive visualization of why switching doors is the 
    #superior game strategy for the Monty Hall problem. 
    x_axis = []
    y_axis = []
    y_axis2 = []
    for i in range(1000):
        #only check every 10 repetitions
        if i %10 == 0 and i != 0:
            x_axis.append(i)
            y_axis.append(sample_keep_door(i))
            y_axis2.append(sample_switch_door(i))
            
    plt.plot(x_axis, y_axis)
    plt.plot(x_axis, y_axis2)

    plt.xlabel("Number of Games Played")
    plt.ylabel("Proportion of Games Won")
    plt.title('Monty Hall problem, switch v.s. no switch')
    legend_drawn_flag = True
    plt.legend(["Keep Doors", "Switch Doors"], loc=0, frameon=legend_drawn_flag)

    plt.show()
create_graph()