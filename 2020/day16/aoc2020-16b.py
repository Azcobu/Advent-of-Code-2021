# AoC 2020 Day 16a
from parse import parse
from itertools import chain

def load_data():
    fieldrules = {}
    tickets = []
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    for line in d:
        parsestr = '{}: {}-{} or {}-{}'
        if ' or ' in line:
            field, x1, x2, y1, y2 = parse(parsestr, line)
            fieldrules[field] = [(int(x1), int(x2)), (int(y1), int(y2))]
        elif ',' in line:
            tickets.append([int(x) for x in line.split(',')])
    return fieldrules, tickets

def is_valid_ticket(allrules, ticket):
    for num in ticket:
        for rule in allrules:
            if rule[0] <= num <= rule[1]:
                break
        else:
            return False
    return True

def is_valid_field(tickets, rule, fieldnum):
    for t in tickets:
        if not (rule[0][0] <= t[fieldnum] <= rule[0][1] or rule[1][0] <= t[fieldnum] <= rule[1][1]):
            return False
    else:
        return True

def purge_dict(indict, key, val):
    for k, v in indict.items():
        if k != key and val in v:
            v.remove(val)
    return indict
    
def find_field_mapping(fieldrules, tickets):
    purged = []
    ticketval = 1
    myticket = tickets[0]

    allrules = list(chain.from_iterable(fieldrules.values()))
    fieldmap = {k: [] for k in fieldrules}
    tickets = [x for x in tickets[1:] if is_valid_ticket(allrules, x)]

    for fieldname, fieldnums in fieldmap.items():
        for fieldnum in range(len(fieldrules)):
            if is_valid_field(tickets, fieldrules[fieldname], fieldnum):
                fieldnums.append(fieldnum)

    for x in range(len(fieldmap)):
        for k, v in fieldmap.items():
            if len(v) == 1 and v[0] not in purged:
                purge_dict(fieldmap, k, v[0])
                purged.append(v[0])

    for k, v in fieldmap.items():
        if 'departure' in k:
            ticketval *= myticket[v[0]]

    print(ticketval)
            
def main():
    find_field_mapping(*load_data())

if __name__ == '__main__':
    main()
