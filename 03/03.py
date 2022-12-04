from typing import Iterator

def common_items(*items: tuple[str]) -> str:
    common = set(items[0])
    for item in items[1:]:
        common &= set(item)
    return "".join(common)

def compartment_failure(items: str) -> str:
    l = len(items) // 2
    return common_items(items[:l], items[l:])

def priority(item: str) -> int:
    return ord(item) - 38 if item.isupper() else ord(item) - 96

if __name__ == "__main__":
    with open("03") as f:
        lines = f.read().splitlines()

    part1 = sum(priority(compartment_failure(l)) for l in lines)
    print("Part 1:", part1)

    def grouper(items: list[str]) -> Iterator:
        args = [iter(items)] * 3
        return zip(*args)

    part2 = sum(priority(common_items(*l)) for l in grouper(lines))
    print("Part 2:", part2)