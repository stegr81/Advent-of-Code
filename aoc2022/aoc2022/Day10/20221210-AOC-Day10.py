with open("Day10/20221210-AOC-Day10-Input.txt", "r") as f:
    inst = f.read().strip().split('\n')

val_dict = {}
cycle = 1
x_register = 1
for line in inst:
    match line.split():
        case [x] if x=='noop':
            val_dict[cycle] = x_register
            cycle+=1
        case [_,a]:
            val_dict[cycle] = x_register
            cycle+=1
            val_dict[cycle] = x_register
            x_register+=int(a)
            cycle+=1

# part 1
strength_vals = []
for num in [20,60,100,140,180,220]:
    strength_vals.append(val_dict[num] * num)
print(sum(strength_vals))

x_register = 1 # centre of sprite position, covers 0,1,2
cycle_range=[y for x in range(6) for y in range(40)]
cycle=0
img = ''
for line in inst:
    match line.split():
        case [x] if x=='noop':
            if cycle_range[cycle]==x_register or cycle_range[cycle]==x_register-1 or cycle_range[cycle]==x_register+1:
                img+='#'
            else:
                img+='.'
            cycle+=1
        case [_,a]:
            if cycle_range[cycle]==x_register or cycle_range[cycle]==x_register-1 or cycle_range[cycle]==x_register+1:
                img+='#'
            else:
                img+='.'
            cycle+=1
            if cycle_range[cycle]==x_register or cycle_range[cycle]==x_register-1 or cycle_range[cycle]==x_register+1:
                img+='#'
                x_register+=int(a)
            else:
                img+='.'
                x_register+=int(a)
            cycle+=1
# part 2
start=0
for end in [40,80,120,160,200,240]:
    print(img[start:end])
    start=end 