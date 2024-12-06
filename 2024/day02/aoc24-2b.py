#AoC 24 Day 2a

def load_data() -> list:
    reports = []
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for line in infile.readlines():
            reports.append([int(x) for x in line.strip().split()])
    return reports

def is_safe(report: list) -> bool:
    allvars = [report] + [report[:i] + report[i+1:] for i in range(len(report))]

    for rep in allvars:
        numrange = range(1, 4) if rep[0] < rep[1] else range(-1, -4, -1)
        for pos, x in enumerate(rep[:-1]):
            if rep[pos+1] - x not in numrange:
                break
        else:
            return True
    return False
    
def main():
    replist = load_data()
    print(sum([1 for rep in replist if is_safe(rep)]))

if __name__ == '__main__':
    main()
