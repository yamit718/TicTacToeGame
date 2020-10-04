import random

def toss():
    '''This funtion is use for toss'''
    tosschoice =input(f"{pler1} and {pler2} please choose head and Tale respectively: ").split(" ")
    while not('head' in tosschoice and 'tale' in tosschoice):
        tosschoice = input("Please Re-enter Head and Tale by giving single space: ").lower().split(" ")
    coin_f = random.choice(tosschoice)
    if coin_f == tosschoice[0]:
        print(f"it's{coin_f}, {pler1} you won the toss.")
        return pler1
    else:
        print(f"it's{coin_f}, {pler2} you won the toss.")
        return pler2

def matchReplay():
    return input("Do you wanna play again(Y/N)?").upper().startswith('Y')
        
def plyMarkChoice(tosswinner):   
    markers=''
    while not(markers=='X' or markers=='O'):
        ply1 = input(f"As {tosswinner} you won the Toss so Please choose 'X' or 'O': ").upper()
        if not(ply1 == 'X' or ply1 == 'O'):
            plyMarkChoice(tosswinner)
        else:
            if ply1 == 'X':
                print(f"{tosswinner} As a Toss winner you Chose 'X'. So, second player will have 'O'.")
                return ('X','O')
            else :
                print(f"{tosswinner} As a Toss winner you Chose 'O', So, second player will have 'X'.")
                return ('O','X')

def creat_Tble(mark_position,markers):
    num_ls[mark_position] = markers
    print(num_ls[7]+' | '+num_ls[8]+' | '+num_ls[9])
    print('--|---|--')
    print(num_ls[4]+' | '+num_ls[5]+' | '+num_ls[6])
    print('--|---|--')
    print(num_ls[1]+' | '+num_ls[2]+' | '+num_ls[3])

def player1_choice():
    mark_p = int (input('You are Player1, where do you wanna to mark on 1-9: '))
    if mark_p not in range(1,10):
        player1_choice()
    if num_ls[mark_p] != " ":
        print("This place is already taken. Please mark somewhere else within range")
        player1_choice()
    return mark_p

def player2_choice():
    mark_p = int (input('You are Player2, where do you wanna to mark on 1-9: '))
    if mark_p not in range(1,10):
        player2_choice()
    if num_ls[mark_p] != " ":
        print("This place is already taken. Please mark somewhere else within range")
        player2_choice()
    return mark_p

def check_Space():
    if " " in num_ls:
        return True
    else:
        print("Just kidding!\nMatch Draw!")
        
def winnercheck():
    if((num_ls[1]== 'X'and num_ls[2]== 'X' and num_ls[3]== 'X') or 
       (num_ls[4]== 'X'and num_ls[5]== 'X' and num_ls[6]== 'X') or
       (num_ls[7]== 'X'and num_ls[8]== 'X' and num_ls[9]== 'X') or
       (num_ls[1]== 'X'and num_ls[4]== 'X' and num_ls[7]== 'X') or
       (num_ls[2]== 'X'and num_ls[5]== 'X' and num_ls[8]== 'X') or
       (num_ls[3]== 'X'and num_ls[6]== 'X' and num_ls[9]== 'X') or
       (num_ls[1]== 'X'and num_ls[5]== 'X' and num_ls[9]== 'X') or
       (num_ls[3]== 'X'and num_ls[5]== 'X' and num_ls[7]== 'X') or
       (num_ls[1]== 'O'and num_ls[2]== 'O' and num_ls[3]== 'O') or 
       (num_ls[4]== 'O'and num_ls[5]== 'O' and num_ls[6]== 'O') or
       (num_ls[7]== 'O'and num_ls[8]== 'O' and num_ls[9]== 'O') or
       (num_ls[1]== 'O'and num_ls[4]== 'O' and num_ls[7]== 'O') or
       (num_ls[2]== 'O'and num_ls[5]== 'O' and num_ls[8]== 'O') or
       (num_ls[3]== 'O'and num_ls[6]== 'O' and num_ls[9]== 'O') or
       (num_ls[1]== 'O'and num_ls[5]== 'O' and num_ls[9]== 'O') or
       (num_ls[3]== 'O'and num_ls[5]== 'O' and num_ls[7]== 'O')):
       return True

while True:   
    num_ls = ['1'," "," "," "," "," "," "," "," "," "]
    print('Lets Play the Tic Tac toe Game\n')
    pler1 = input("Please Enter 1st player name: ")
    pler2 = input("Please Enter 2st player name: ")
    print("First lets have Toss\n")
    

    tosswinner =toss()
    ply1,ply2 = plyMarkChoice(tosswinner)
    
    while check_Space() == True:
        
        mark_positionforply1 = player1_choice()
        creat_Tble(mark_positionforply1, ply1)
        if winnercheck() == True:
            print(" You Won!")
            break
            
        mark_positionforply2 = player2_choice()
        creat_Tble(mark_positionforply2, ply2)
        if winnercheck() == True:
            print(" You Won!")
            break
    
    if not matchReplay():
        break