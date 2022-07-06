def find_scores(target):
    e1pos, e2pos = 0, 1
    scores = '37'

    while target not in scores[-8:]:
        scores += str(int(scores[e1pos]) + int(scores[e2pos]))
        e1pos = (e1pos + 1 + int(scores[e1pos])) % len(scores)
        e2pos = (e2pos + 1 + int(scores[e2pos])) % len(scores)
    return scores.index(target)

def main():
    assert find_scores('51589') == 9
    assert find_scores('01245') == 5
    assert find_scores('92510') == 18
    assert find_scores('59414') == 2018
    print(find_scores('640441'))

if __name__ == '__main__':
    main()
