# part 1 - check to see if 2 pairs of numbers are contained completely within another
def check_subset(x,y):
    if set(x).issubset(y):
        return True
    elif set(y).issubset(x):
        return True
    else:
        return False

with open("20221204-AOC-input.txt", "r") as f:
    assignments=f.read().split('\n')

assignments=[x for x in assignments if len(x)>0] #removing spurious empty string
assignment_subset=[]

for pair in assignments:
   elf1,elf2 = pair.split(',')
   start,stop=elf1.split('-')
   elf1 = [i for i in range(int(start),int(stop)+1)]
   start,stop=elf2.split('-')
   elf2 = [i for i in range(int(start),int(stop)+1)]
   if check_subset(elf1,elf2)==True:
       assignment_subset.append(pair)
print(len(assignment_subset))

# part 2 - if given 2 ranges of numbers, check to see if they overlap at all
def check_overlap(x,y):
    if len(set(x).intersection(set(y)))>0:
        return True
    else:
        return False
assignment_overlap=[]

for pair in assignments:
   elf1,elf2 = pair.split(',')
   start,stop=elf1.split('-')
   elf1 = [i for i in range(int(start),int(stop)+1)]
   start,stop=elf2.split('-')
   elf2 = [i for i in range(int(start),int(stop)+1)]
   if check_overlap(elf1,elf2)==True:
    assignment_overlap.append(pair)
print(len(assignment_overlap))
