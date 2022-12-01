if __name__ == "__main__":
    with open("01") as f:
        elves = f.read().split("\n\n")
    
    calories = sorted(sum(map(int, e.strip().split("\n"))) for e in elves)
    print("Part 1:", calories[-1])
    print("Part 2:", sum(calories[-3:]))