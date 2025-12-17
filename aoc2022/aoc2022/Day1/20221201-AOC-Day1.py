with open("first_input.txt", "r") as f:
    cals = f.read()
cals_list = cals.split("\n")
cals_dict={}
temp_list=[]
elf_desig=1
for val in cals_list:
    if val!='':
        temp_list.append(int(val))
    elif val=='':
        cals_dict[elf_desig]=sum(temp_list)
        temp_list=[]
        elf_desig+=1
max_val = max(cals_dict.values())
max_cal_elf = max(cals_dict,key=cals_dict.get)
print(f"top elf and the calories in their sack {max_cal_elf},{max_val}")

#part 2 - top 3 elves
top3=sorted(cals_dict.values(), reverse=True)[:3]
print(sum(top3))
    
