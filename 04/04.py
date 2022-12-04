import re

def regex_match(pattern: str, string: str) -> list[str]:
    return re.match(pattern, string).groups()

def strs_to_ints(strings: list[str]) -> list[int]:
    return list(map(int, strings))

def check_includes(begf, endf, begs, ends) -> bool:
    return begf <= begs <= ends <= endf or \
        begs <= begf <= endf <= ends

def check_overlaps(begf, endf, begs, ends) -> bool:
    return begf <= begs <= endf or \
        begs <= begf <= ends

if __name__ == "__main__":
    with open("04") as f:
        r = "([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)"
        sections = [strs_to_ints(regex_match(r, l)) for l in f]
    
    part1 = sum(1 for s in sections if check_includes(*s))
    print("Part 1:", part1)

    part2 = sum(1 for s in sections if check_overlaps(*s))
    print("Part 2:", part2)