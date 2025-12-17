# part one - identify duplicate items in first and second half of string- obtain priority based on ascii character a-z=1-26 & A-Z=27-52
from string import ascii_lowercase,ascii_uppercase

def get_priority(x):
    halfway=int(len(x)/2)
    i=x[:halfway]
    j=x[halfway:]
    return list(set(i).intersection(j))

pri_dict={}
for i,c in enumerate(ascii_lowercase,1):
    pri_dict[c]=i
for i,c in enumerate(ascii_uppercase,27):
    pri_dict[c]=i

with open("20221203-AOC-input.txt", "r") as f:
    inventory=f.read()
    inventory=inventory.split("\n")

duplicates=list(map(get_priority,inventory))
print(sum([pri_dict[j] for i in duplicates for j in i]))

#part 2 - each 3 lines represent one elf group. Identify duplicate items in each group and pass out the priority based on the previous mapping
inventory=[x for x in inventory if len(x)>0] #spurious empty string removed
start=0
stop=3
badges=[]
for i in range(int(len(inventory)/3)):
    a,b,c=inventory[start:stop]
    item=list(set(a).intersection(b).intersection(c))
    badges.append(pri_dict[item[0]])
    start+=3
    stop+=3
print(sum(badges))





