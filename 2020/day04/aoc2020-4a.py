
def load_data():
    passports = []
    with open('input.txt', 'r') as infile:
        data = infile.read().split('\n\n')
        data = [x.replace('\n', ' ').split() for x in data]
        for person in data:
            passports.append(dict(fields.split(':') for fields in person))
    return passports

def count_valid(data):
    return sum(1 for x in data if len(x) == 8 or (len(x) == 7 and 'cid' not in x.keys()))

def main():
    d = load_data()
    print(count_valid(d))

if __name__ == "__main__":
    main()