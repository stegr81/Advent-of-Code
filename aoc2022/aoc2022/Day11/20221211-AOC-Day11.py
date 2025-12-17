import operator

with open("Day11/20221211-AOC-Day11-Input.txt", "r") as f:
    inst = f.read().strip().split('\n\n')

def get_operators(x:str):
    val_x, op, val_y = x.split()
    if val_x.isnumeric():
        val_x = int(val_x)
    if val_y.isnumeric():
        val_y = int(val_y)
    return val_x, op, val_y

def create_dict(inst):
    monkey_dict={}
    for monkey in inst:
        parts = monkey.split('\n')
        monkey_dict[parts[0].split(':')[0]]={
                            'items':parts[1].split(':')[1].strip().split(', '),
                            'operation':parts[2].split('= ')[1].strip(),
                            'test':int(parts[3].split('by ')[1]),
                            'if true':parts[4].split('to ')[1].capitalize(),
                            'if false':parts[5].split('to ')[1].capitalize(),
                            'inspection':0
                            }
    return monkey_dict

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

monkey_dict = create_dict(inst)

for r in range(20):
    for k,v in monkey_dict.items():
        if len(monkey_dict[k]['items'])>0:
            items = [int(x) for x in reversed(monkey_dict[k]['items'])]
            monkey_dict[k]['items']=[]
            monkey_dict[k]['inspection'] += len(items)
            for item in items:
                val_x, op, val_y = get_operators(monkey_dict[k]['operation'])
                if val_x == 'old':
                    val_x = int(item)
                if val_y == 'old':
                    val_y = int(item)
                new = ops[op](val_x,val_y)
                new = round(new/3)
                if new%int(monkey_dict[k]['test']) == 0:
                    move_to = monkey_dict[k]['if true']
                    monkey_dict[move_to]['items'].append(new)
                else:
                    move_to = monkey_dict[k]['if false']
                    monkey_dict[move_to]['items'].append(new)
            continue

inspections = []
for k,v in monkey_dict.items():
    print(f"{k} conducted {monkey_dict[k]['inspection']} inspections")
    inspections.append(monkey_dict[k]['inspection'])

a,b = sorted(inspections)[-2:]
print(a,b)
a*b