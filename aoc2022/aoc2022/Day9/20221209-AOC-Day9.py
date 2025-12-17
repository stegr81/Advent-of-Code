with open("Day9/20221209-AOC-Day9-Input.txt", "r") as f:
    inst=f.read().strip().split('\n')

locations = []
head = (0,0)
tail = (0,0)
locations.append(tail)

def check_delta(head,tail):
    delta_x = head[0]-tail[0]
    delta_y = head[1]-tail[1]
    return delta_x, delta_y

def basic_move(direction,end):
    x,y=end
    if direction == 'R':
        x+=1
    elif direction == 'L':
        x-=1
    elif direction == 'U':
        y+=1
    elif direction == 'D':
        y-=1
    end=(x,y)
    return end

def diag_move(tail, *args): 
    a,b = tail
    if 'upright' in args:
        a+=1
        b+=1
    elif 'downright' in args:
        a+=1
        b-=1
    elif 'upleft' in args:
        a-=1
        b+=1
    elif 'downleft' in args:
        a-=1
        b-=1
    tail = (a,b)
    return tail

# loop through all the commands
for line in inst:
    direction,moves = line.split()

    for _ in range(int(moves)):
        head = basic_move(direction, head)
        
        delta_x,delta_y = check_delta(head,tail)

        if abs(delta_x)==1 and abs(delta_y)==1:
            continue
        elif delta_x>1 and delta_y==0 and direction == 'R': 
            tail = basic_move(direction,tail)
        elif delta_x<-1 and delta_y==0 and direction == 'L':
            tail = basic_move(direction,tail)
        elif delta_x == 0 and delta_y > 1 and direction  == 'U':
            tail = basic_move(direction,tail)
        elif delta_x == 0 and delta_y < -1 and direction == 'D':
            tail = basic_move(direction,tail)
        elif (delta_x>1 and delta_y==1) or (delta_x==1 and delta_y>1):
            tail = diag_move(tail, 'upright')
        elif (delta_x>1 and delta_y==-1) or (delta_x==1 and delta_y<-1):
            tail = diag_move(tail,'downright')
        elif (delta_x<-1 and delta_y==1) or (delta_x==-1 and delta_y>1):
            tail = diag_move(tail, 'upleft')
        elif (delta_x==-1 and delta_y<-1) or (delta_x<-1 and delta_y==-1):
            tail = diag_move(tail, 'downleft')
        locations.append(tail)

print(len(set(locations)))