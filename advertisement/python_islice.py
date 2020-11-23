import itertools

with open('campaigns.csv', 'r') as file:
    sliced_file = itertools.islice(file, 4, 9, 4)
    for s in sliced_file:
        print(s, end='')
