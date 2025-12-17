import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd


def check_vis(i,j):
    current_tree = df.iloc[i][j]
    if i==0 or i==98:
        return True
    elif j==0 or j==98:
        return True
    else:
        if all(current_tree>x for x in df.iloc[i][:j].tolist()):
            return True
        elif all(current_tree>x for x in df.iloc[i][j+1:].tolist()):
            return True
        elif all(current_tree>x for x in df.iloc[:i][j].tolist()):
            return True
        elif all(current_tree>x for x in df.iloc[i+1:][j].tolist()):
            return True
        else:
            return False      

with open("Day8/20221208-AOC-Day8-Input.txt", "r") as f:
    l = f.read().strip().split()

rows=len(l)
cols = len(l[0])
data=[]
for line in l:
    data.append([int(x) for x in line])
my_array=np.array(data)

#plt.figure(figsize = (15,15))
#ax = sns.heatmap(my_array, linewidths=0.5, cmap='Greens', cbar=False, yticklabels=False, xticklabels=False)
#plt.show()

# part 1

df = pd.DataFrame(data)

counter=0
for i in range(rows):
    for j in range(cols):
        if check_vis(i,j)==True:
            counter+=1
print(counter)

# part 2

def check_left(i,j):
    current_tree=df.iloc[i][j]
    lst = df.iloc[i][:j].tolist()
    for x in range(len(lst)):
        if lst[-1]<current_tree:
            lst.pop()
        elif lst[-1]==current_tree:
            lst.pop()
            break
        elif lst[-1]>current_tree:
            lst.pop()
            break
    num = j-len(lst)
    return num

def check_right(i,j):
    current_tree=df.iloc[i][j]
    lst = df.iloc[i][j+1:].tolist()
    lst.reverse()
    num=0
    for x in range(len(lst)):
        if lst[-1]<current_tree:
            lst.pop()
            num = x+1
        elif lst[-1]==current_tree:
            lst.pop()
            num = x+1
            break
        elif lst[-1]>current_tree:
            lst.pop()
            num = x+1
            break
    
    return num

def check_up(i,j):
    current_tree=df.iloc[i][j]
    lst = df.iloc[:i][j].tolist()
    for x in range(len(lst)):
        if lst[-1]<current_tree:
            lst.pop()
        elif lst[-1]==current_tree:
            lst.pop()
            break
        elif lst[-1]>current_tree:
            lst.pop()
            break
    num = i-len(lst)
    return num

def check_down(i,j):
    current_tree=df.iloc[i][j]
    lst = df.iloc[i+1:][j].tolist()
    lst.reverse()
    num=0
    for x in range(len(lst)):
        if lst[-1]<current_tree:
            lst.pop()
            num = x+1
        elif lst[-1]==current_tree:
            lst.pop()
            num = x+1
            break
        elif lst[-1]>current_tree:
            lst.pop()
            num = x+1
            break
        
    return num

scenic_score=[]
for i in range(rows):
    for j in range(cols):
        scenic_score.append(check_left(i,j)*check_right(i,j)*check_up(i,j)*check_down(i,j))
print(max(scenic_score))
