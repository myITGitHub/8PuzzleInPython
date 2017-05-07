#d初始化一个八数码
import random
def init():
    initial=[]
    while len(initial)<9:
        b = random.randint(0, 8)
        if b in initial:
            continue
        initial.append(b)
    return initial