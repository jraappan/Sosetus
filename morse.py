#!/usr/bin/env python
# coding=utf-8

morse_table = {
                    "a": u"\u2022 \u2013",
                    "b": u"\u2013 \u2022 \u2022 \u2022",
                    "c": u"\u2013 \u2022 \u2013 \u2022",
                    "d": u"\u2013 \u2022 \u2022",
                    "e": u"\u2022",
                    "f": u"\u2022 \u2022 \u2013 \u2022",
                    "g": u"\u2013 \u2013 \u2022",
                    "h": u"\u2022 \u2022 \u2022 \u2022",
                    "i": u"\u2022 \u2022",
                    "j": u"\u2022 \u2013 \u2013 \u2013",
                    "k": u"\u2013 \u2022 \u2013",
                    "l": u"\u2022 \u2013 \u2022 \u2022",
                    "m": u"\u2013 \u2013",
                    "n": u"\u2013 \u2022",
                    "o": u"\u2013 \u2013 \u2013",
                    "p": u"\u2022 \u2013 \u2013 \u2022",
                    "q": u"\u2013 \u2013 \u2022 \u2013",
                    "r": u"\u2013 \u2022 \u2013",
                    "s": u"\u2022 \u2022 \u2022",
                    "t": u"\u2013",
                    "u": u"\u2022 \u2022 \u2013",
                    "v": u"\u2022 \u2022 \u2022 \u2013",
                    "w": u"\u2022 \u2013 \u2013",
                    "x": u"\u2013 \u2022 \u2022 \u2013",
                    "y": u"\u2013 \u2022 \u2013 \u2013",
                    "z": u"\u2013 \u2013 \u2022 \u2022",
                    ".": u"\u2022 \u2013 \u2022 \u2013 \u2022 \u2013",
                    ",": u"\u2013 \u2013 \u2022 \u2022 \u2013 \u2013",
                    "?": u"\u2022 \u2022 \u2013 \u2013 \u2022 \u2022",
                    "/": u"\u2013 \u2022 \u2022 \u2013 \u2022",
                    "@": u"\u2022 \u2013 \u2013 \u2022 \u2013 \u2022",
                    "1": u"\u2022 \u2013 \u2013 \u2013 \u2013",
                    "2": u"\u2022 \u2022 \u2013 \u2013 \u2013",
                    "3": u"\u2022 \u2022 \u2022 \u2013 \u2013",
                    "4": u"\u2022 \u2022 \u2022 \u2022 \u2013",
                    "5": u"\u2022 \u2022 \u2022 \u2022 \u2022",
                    "6": u"\u2013 \u2022 \u2022 \u2022 \u2022",
                    "7": u"\u2013 \u2013 \u2022 \u2022 \u2022",
                    "8": u"\u2013 \u2013 \u2013 \u2022 \u2022",
                    "9": u"\u2013 \u2013 \u2013 \u2013 \u2022",
                    "0": u"\u2013 \u2013 \u2013 \u2013 \u2013"
                    }


def encode_to_morse(text_to_morse):
    print "***encode_to_morse"
    morse_result_list = []
    for letter in text_to_morse:
        if letter.lower() in morse_table:
            morse_result_list.append(morse_table[letter.lower()].encode('utf-8'))
        else:
            if letter == ' ':
                morse_result_list.append(' ')
            else:
                print "Not valid letter %s" % letter

    morse_result = ".".join(morse_result_list)
    return morse_result


def decode_to_text(morse_to_text):
    print "***decode_to_text"
    text_result = ""
    tmp_morse_table = {}

    test = morse_to_text.split('.')
    for key in morse_table:
        new_key = repr(morse_table[key].encode('utf-8'))
        tmp_morse_table[new_key] = key

    for code in test:
        if repr(code) in tmp_morse_table:
            text_result = text_result + tmp_morse_table[repr(code)]
        elif code == ' ':
            text_result = text_result + ' '
        else:
            print "Not valid mark"

    return text_result.upper()


def get_sample_text():
    print "***get_sample_text"
    sample_text = ""
    try:
        with open("Text.txt", "r") as r:
            sample_text = r.read()
            print sample_text
    except EnvironmentError as e:
        print e
    return sample_text


def get_sample_morse():
    print "***get_sample_morse"
    sample_morse = ""
    try:
        with open("Morse.txt", "r") as r:
            sample_morse = r.read()
            print sample_morse
    except EnvironmentError as e:
        print e

    return sample_morse


def save_result(result_item):
    print "***save_result"
    status = True
    try:
        with open("Morse.txt", "wb") as w:
            w.write(str(result_item))
            print "File saved"
    except Exception as e:
        print "save_result/error %s" % e
        status = False

    return status


def main():

    text_to_morse = get_sample_text()  # Get the sample text
    if text_to_morse:
        morse_result = encode_to_morse(text_to_morse)  # Encode the sample to morse
        status = save_result(morse_result)  # Save result to file
        print status
    else:
        print "No text to encode"

    print "*** morse to text"
    morse_to_text = get_sample_morse()  # Get sample morse
    if morse_to_text:
        text_result = decode_to_text(morse_to_text)  # Decode the sample to text
        print "text_result %s" % text_result
    else:
        print "No morse to decode"


if __name__ == '__main__':
    main()
