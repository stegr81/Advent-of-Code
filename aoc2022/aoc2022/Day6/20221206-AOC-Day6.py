with open("Day6/20221206-AOC-Day6-Input.txt", "r") as f:
    r = f.read()
    
def check(chars):
    start=0
    end=start+chars
    for letters in r:
        if len(set([x for x in r[start:end]]))<chars:
            start+=1
            end+=1
        else:
            return end
            break

# part 1 - given a string of characters, how many letters must pass before hitting a sequence of 4 unrepeated characters.
print(check(chars=4))
# part 2 - given the same string, how many letters must pass before hitting a sequence of 14 unrepeated characters.
print(check(chars=14))



