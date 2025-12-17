with open("Rock_Paper_Scissors_input.txt", "r") as f:
    strat = f.read()
    round_break = strat.split("\n")
    #print(round_break)

opp_dict={'A':1,'B':2,'C':3}
my_dict={'X':1,'Y':2,'Z':3}
lose=0
draw=3
win=6
total_points=0

for _round in round_break:
    if len(_round)>=3:
        opponent_choice,my_choice=_round.split(" ")
        opp_score=(opp_dict[opponent_choice])
        my_score=(my_dict[my_choice])
    
        if my_choice=='X' and opponent_choice=='A':
            result=draw
        if my_choice=='X' and opponent_choice=='C':
            result=win
        if my_choice=='X' and opponent_choice=='B':
            result=lose
        if my_choice=='Y' and opponent_choice=='B':
            result=draw
        if my_choice=='Y' and opponent_choice=='A':
            result=win
        if my_choice=='Y' and opponent_choice=='C':
            result=lose
        if my_choice=='Z' and opponent_choice=='C':
            result=draw
        if my_choice=='Z' and opponent_choice=='B':
            result=win
        if my_choice=='Z' and opponent_choice=='A':
            result=lose

        total_points+=sum([result+my_score])
print(f"first method {total_points}")

sec_total_points = 0
for _round in round_break:
    if len(_round)>=3:
        opponent_choice,my_choice=_round.split(" ")
        #opp_score=(opp_dict[opponent_choice])
        #my_score=(my_dict[my_choice])
    
        if my_choice=='X' and opponent_choice=='A':
            my_score=3
            result=lose
        if my_choice=='X' and opponent_choice=='C':
            my_score=2
            result=lose
        if my_choice=='X' and opponent_choice=='B':
            my_score=1
            result=lose
        if my_choice=='Y' and opponent_choice=='B':
            my_score=2
            result=draw
        if my_choice=='Y' and opponent_choice=='A':
            my_score=1
            result=draw
        if my_choice=='Y' and opponent_choice=='C':
            my_score=3
            result=draw
        if my_choice=='Z' and opponent_choice=='C':
            my_score=1
            result=win
        if my_choice=='Z' and opponent_choice=='B':
            my_score=3
            result=win
        if my_choice=='Z' and opponent_choice=='A':
            my_score=2
            result=win

        sec_total_points+=sum([result+my_score])
print(f"second method {sec_total_points}")

    
