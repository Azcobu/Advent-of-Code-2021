from functools import reduce

def load_data():
    answers = []
    with open('input.txt') as infile:
        data = infile.read().strip().split('\n\n')
    for d in data:
        answers.append([x for x in d.split('\n')])
    return answers

def sum_answers(answers):
    total = 0
    for a in answers:
        total += len(list(reduce(set.intersection, [set(x) for x in a])))
    return total

def main():
    print(sum_answers(load_data()))

if __name__ == '__main__':
    main()
