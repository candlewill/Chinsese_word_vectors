# -*- coding: utf-8 -*-
import csv
import itertools, unicodedata

def group_words(s):
    # This is a closure for key(), encapsulated in an array to work around
    # 2.x's lack of the nonlocal keyword.
    sequence = [0x10000000]

    def key(part):
        val = ord(part)
        if part.isspace():
            return 0

        # This is incorrect, but serves this example; finding a more
        # accurate categorization of characters is up to the user.
        asian = unicodedata.category(part) == "Lo"
        if asian:
            # Never group asian characters, by returning a unique value for each one.
            sequence[0] += 1
            return sequence[0]

        return 2

    result = []
    for key, group in itertools.groupby(s, key):
        # Discard groups of whitespace.
        if key == 0:
            continue

        str = "".join(group)
        result.append(str)

    return result


if __name__ == "__main__":

    inp = '/home/hs/Data/wikipedia/wiki.zh.text.simplified'
    outp = '/home/hs/Data/wikipedia/wiki.zh.text.simplified.character'

    out = []
    with open(inp, 'r', newline='\n', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            out.append(" ".join(group_words(str(line))))

    with open(outp, 'w', encoding='utf-8') as wf:
        for l in out:
            wf.write(str(l[2:-2])+'\n')
