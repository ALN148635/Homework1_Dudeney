# -*- coding: utf-8 -*-
import time

SET = set({})
LETTER = [-1 for i in range(8)]


def checkMONEY():
    send = LETTER[0]*1000 + LETTER[1]*100 \
           + LETTER[2]*10 + LETTER[3]
    more = LETTER[4]*1000 + LETTER[5]*100 \
           + LETTER[6]*10 + LETTER[1]
    money = LETTER[4]*10000 + LETTER[5]*1000 \
            + LETTER[2]*100 + LETTER[1]*10 + LETTER[7]
    return send + more == money


def setLetters(p, n):
    if n in SET:
        return
    if p == 0 and n == 0:
        return
    if p == 4 and n == 0:
        return
    # put LETTER[p]=n in SET
    LETTER[p] = n
    SET.add(n)
    if p >= 7:
        #print(LETTER)
        if checkMONEY():
            print('S E N D M O R Y')
            print('{} {} {} {} {} {} {} {}'
                  .format(LETTER[0], LETTER[1], LETTER[2], LETTER[3],
                          LETTER[4], LETTER[5], LETTER[6], LETTER[7]))
        SET.remove(n)
        return
    for i in range(0, 10):
        setLetters(p+1, i)
    SET.remove(n)
    return


print time.asctime(time.localtime(time.time()))
for i in range(0, 10):
    setLetters(0, i)
print time.asctime(time.localtime(time.time()))
