if __name__ == "__main__":
    with open("02") as f:
        games = ["".join(l.split()) for l in f]

    score = {
        "AA" : 4, "AB" : 8, "AC" : 3,
        "BA" : 1, "BB" : 5, "BC" : 9,
        "CA" : 7, "CB" : 2, "CC" : 6
    }

    map1 = {
        "AX" : "AA", "AY" : "AB", "AZ" : "AC",
        "BX" : "BA", "BY" : "BB", "BZ" : "BC",
        "CX" : "CA", "CY" : "CB", "CZ" : "CC"
    }

    map2 = {
        "AX" : "AC", "AY" : "AA", "AZ" : "AB",
        "BX" : "BA", "BY" : "BB", "BZ" : "BC",
        "CX" : "CB", "CY" : "CC", "CZ" : "CA"
    }

    part1 = sum(score[map1[g]] for g in games)
    part2 = sum(score[map2[g]] for g in games)

    print("Part 1:", part1)
    print("Part 2:", part2)