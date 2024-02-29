# Q3 cook problem (parallel)

if __name__ == "__main__":

    n = 2
    recipe = {
        "A" : 3,
        "B" : 2
    }
    orders = [
        "A 1",
        "A 2",
        "B 3",
        "B 4"
    ]
    done = []

    # initialzie
    for _ in range(len(orders)):
        done.append(False)

    cook1 = 0
    cook2 = 0

    for o in orders:
        menu, time = o.split(" ")

        if cook1 <= time:
            cook1 += recipe[menu]
        elif cook2 <= time:
            cook2 += recipe[menu]

