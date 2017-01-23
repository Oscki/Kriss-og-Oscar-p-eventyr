#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    # SKRIV DIN KODE HER
    decks = mergee(sum(decks, []))
    svar = ''
    for i in decks:
        svar += i[1]
    return svar


def mergee(decks):
    res = []
    if len(decks) > 1:
        mid = int(len(decks) / 2)
        uno = mergee(decks[0:mid])
        dos = mergee(decks[mid:])
        # print('uno: {0}, dos: {1}'.format(uno, dos))
        i = 0
        j = 0
        while True:
            # print ('len(uno): {0}\nlen(dos): {1}\ni: {2}\nj: {3}'.format(len(uno), len(dos), i, j))
            if uno[i:] and dos[j:]:
                if uno[i][0] < dos[j][0]:
                    res.append(uno[i])
                    i += 1
                else:
                    res.append(dos[j])
                    j += 1
            elif uno[i:]:
                for j in range(i, len(uno)):
                    res.append(uno[j])
                break
            else:
                for i in range(j, len(dos)):
                    res.append(dos[i])
                break
    else:
        return decks
    return res


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
