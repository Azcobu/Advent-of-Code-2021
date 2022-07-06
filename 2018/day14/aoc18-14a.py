def find_scores(target):
    e1pos, e2pos = 0, 1
    scores = [3, 7]

    while len(scores) < target + 10:
        scores += [int(x) for x in str(scores[e1pos] + scores[e2pos])]
        e1pos = (e1pos + 1 + scores[e1pos]) % len(scores)
        e2pos = (e2pos + 1 + scores[e2pos]) % len(scores)
    return ''.join([str(x) for x in scores[target:target+10]])

def main():
    assert find_scores(9) == '5158916779'
    assert find_scores(5) == '0124515891'
    assert find_scores(18) == '9251071085'
    assert find_scores(2018) == '5941429882'
    print(find_scores(640441))

if __name__ == '__main__':
    main()
