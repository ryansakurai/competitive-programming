lamps = {
    "A": False,
    "B": False,
}

def main():
    _ = int(input())
    switches_to_press = input().split(" ")
    for switch in switches_to_press:
        if switch == "1":
            press_lightswitch_1()
        else:
            press_lightswitch_2()

    print("1" if lamps["A"] else "0")
    print("1" if lamps["B"] else "0")

def press_lightswitch_1():
    lamps["A"] = not lamps["A"]

def press_lightswitch_2():
    lamps["A"] = not lamps["A"]
    lamps["B"] = not lamps["B"]


if __name__=="__main__":
    main()
