from io import StringIO
import pandas as pd

def create_stacks(df):
    one=[]
    two=[]
    three=[]
    four=[]
    five=[]
    six=[]
    seven=[]
    eight=[]
    nine=[]
    stacks={}
    names = [one,two,three,four,five,six,seven,eight,nine]
    for each in df.columns:
        names[each-1].append(df[each].tolist())
        names[each-1][0].pop()
        names[each-1][0] = [x.strip() for x in names[each-1][0]]
        names[each-1][0] = [x for x in names[each-1][0] if len(x)>1]
        names[each-1][0].reverse()
        stacks[str(each)]=names[each-1][0]
    return stacks

with open("20221205-AOC-Day5-Input.txt", "r") as f:
    r=f.read()
    f.close()

string_data = (r.split('\n\n')[0]).split('\n')
instruction = (r.split('\n\n')[1]).split('\n')
instruction=[x for x in instruction if len(x)>0]

colnames=[1,2,3,4,5,6,7,8,9]

df = pd.DataFrame(columns=colnames)
for row in r.split('\n\n')[0].split('\n'):
    test = ';'.join(row[i:i+4] for i in range(0,len(row),4))
    test = StringIO(test)
    temp_df=pd.read_csv(test, names=colnames,sep=';')
    df=df.append(temp_df)

stacks=create_stacks(df) # generate original stack configuration
print('Part 1')
for each in instruction:
    moves = int(each.split(' ')[1])
    _from = each.split(' ')[3]
    _to = each.split(' ')[5]
    for i in range(0,moves):
        crate = stacks[_from].pop()
        stacks[_to].append(crate)
print(stacks)

# part 2 - Move crates from stacks to other stacks as per instructions. Crates are now moved in stacks so order is retained when moving stacks.
print('Part 2')
stacks=create_stacks(df) # re-generate original stack configuration

for each in instruction:
    moves = int(each.split(' ')[1])
    _from = each.split(' ')[3]
    _to = each.split(' ')[5]
    crates = stacks[_from][-moves::]
    for i in range(0,moves):
        stacks[_from].pop()
        stacks[_to].append(crates[i])
print(stacks)

