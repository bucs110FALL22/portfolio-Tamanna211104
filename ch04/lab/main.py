import random                                   
player = int(input("How many players? "))         
throws = int(input("How many throws per player? "))            
score_list = []

                                                
for i in range(player):                    
    player_score = []                           
    for j in range(throws):                
        score = random.randrange(1, 50)        
        player_score.append(score)             
    score_list.append(player_score)             
                                                
i = 0                                           
j = 0

for i in range(player):                                    
    print("Player " + str(i + 1) + " got these points: ")    
    for j in range(throws):
        print(str(score_list[i][j]))                             

i = 0
j = 0

for i in range(player):
    sum = 0
    biggest_sum = 0
    for j in range(throws):
        sum += score_list[i][j]
    print(f"Player {i+1} got {sum} points in total")
    if sum >= biggest_sum:
        biggest_sum = sum
 print(f"Player {i+1} got the most points and won!")