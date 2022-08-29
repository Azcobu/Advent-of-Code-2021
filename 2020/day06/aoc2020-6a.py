
def load_data():
    answers = []
    with open('input.txt') as infile:
        data = infile.read().split('\n\n')
    for d in data:
        answers.append([x for x in d.split('\n')])
    return answers

def sum_answers(answers):
    return sum([len(set(''.join(a))) for a in answers])

def main():
    print(sum_answers(load_data()))

if __name__ == '__main__':
    main()
