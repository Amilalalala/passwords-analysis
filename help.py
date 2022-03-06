#!/usr/bin/python
import sys

c_seen = {}
all_pos = []
wordlengths = {}

wordmaxlen = 0

f = open(sys.argv[1], "r")


def process_lengths(wordlengths):
    keys2 = sorted(wordlengths)

    print
    "Number of different lengths: " + str(len(keys2))

    for y in keys2:
        print
        str(y) + " " + str(wordlengths.get(y))
    print


def process_dict(c_seen):
    # sort so most frequent characters are first
    keys2 = sorted(c_seen, key=lambda key: c_seen[key], reverse=True)

    print
    "Number of characters: " + str(len(keys2))

    for y in keys2:
        print
        y + " " + str(c_seen.get(y))
    print

    for z in keys2:
        sys.stdout.write(z)
    print
    print


# read in lines -  and check
for x in f.xreadlines():
    x = x.rstrip('\n')
    wordlen = len(x)

    # store all word lengths we see
    if wordlen in wordlengths:
        wordlengths[wordlen] = wordlengths[wordlen] + 1
    else:
        wordlengths[wordlen] = 1

    # store longest word length
    if wordlen > wordmaxlen:
        wordmaxlen = wordlen

    for i in range(wordlen):
        curchar = x[i]

        # calculate an overall frequency
        if curchar in c_seen:
            c_seen[curchar] = c_seen[curchar] + 1
        else:
            c_seen[curchar] = 1

        # calculate a per position frequency
        if (i == len(all_pos)):  # first encounter this position
            l_seen = {}
            l_seen[curchar] = 1
            all_pos.append(l_seen.copy())
        else:  # we have seen this position before
            l_seen = all_pos[i]
            if curchar in l_seen:
                l_seen[curchar] = l_seen[curchar] + 1
            else:
                l_seen[curchar] = 1

print
"Max word length: " + str(wordmaxlen)
print
process_lengths(wordlengths)

print
"Overall frequency:"
print
process_dict(c_seen)
print
for i in range(wordmaxlen):
    print
    "Position " + str(i) + " frequency"
    c_seen = all_pos[i]
    process_dict(c_seen)
    print