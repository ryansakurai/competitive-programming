"""
Flíper

https://neps.academy/br/exercise/87
"""

def main():
    door_p, door_r = map(int, input().split())
    if door_p == 0:
        print("C")
    elif door_p == 1 and door_r == 0:
        print("B")
    else:
        print("A")

if __name__=="__main__":
    main()
