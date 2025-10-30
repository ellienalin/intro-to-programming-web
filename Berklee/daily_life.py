import time
from itertools import cycle

def have_class():
    return False  

def have_assignment():
    return False  

def friend_calls():
    return False 


daily_life = cycle(["intonation", "Donna Lee in 12 keys", "classical repertoire",
                    "orchestra pieces", "jazz standards", "recordings"])

def go_class():
    print("going to class...")

def do_assignment():
    print("doing assignments...")

def hangout():
    print("hanging out with friends(<3)")

def practice():
    item = next(daily_life)
    print(f"practicing... {item}")

def main():
    while True:
        if have_class():
            go_class()
        elif have_assignment():
            do_assignment()
        elif friend_calls():
            hangout()
        else:
            practice()
        time.sleep(0.1)

main() 