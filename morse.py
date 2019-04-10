#!/usr/bin/env python
# coding=utf-8


def morse():

    morse_table = {
                    "a": u"\u2022\u2013",
                    "b": u"\u2013\u2022\u2022\u2022",
                    "c": u"\u2013\u2022\u2013\u2022",
                    "d": u"\u2013\u2022\u2022",
                    "e": u"\u2022",
                    "f": u"\u2013\u2013\u2022\u2013",
                    "g": u"\u2022\u2022\u2013",
                    }
    for key, value in morse_table.iteritems():
        print "key: %s, value: %s" % (key, value)


def main():
    morse()


if __name__ == '__main__':
    main()
