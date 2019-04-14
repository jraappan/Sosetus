#!/usr/bin/env python
# coding=utf-8

import os
import sys
import re
import logging

logging.basicConfig(filename='morse.log', level=logging.INFO)

# morse key table for encoding and decoding
morse_key_table = {
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
    """
    encode_to_morse() -function encode the given text to morse string.
    :param text_to_morse: text string
    :return: morse_result as morse string
    """
    logging.info("encode_to_morse()")
    morse_result_list = []
    morse_result = ""
    if text_to_morse:
        for letter in text_to_morse:
            if letter.lower() in morse_key_table:  # checks if letter in code table
                morse_result_list.append(morse_key_table[letter.lower()].encode('utf-8'))
                if letter.lower() == '.':
                    morse_result_list.append('\n ')
            else:
                if letter == ' ':  # checks if the letter is white space and adds it as it
                    morse_result_list.append(' ')
                else:
                    logging.debug("encode_to_morse / not valid letter %s" % letter.encode('hex'))

        morse_result = ".".join(morse_result_list)  # adds dot to separate the morse marks

    return morse_result  # returns encoded morse string


def decode_to_text(morse_to_text):
    """
    decode_to_text() -function decodes given morse string to text string
    :param morse_to_text: morse string
    :return: text_result.upper(): text string converted to UPPER CASE
    """
    logging.info("decode_to_text()")
    text_result = ""
    tmp_morse_key_table = {}
    if morse_to_text:
        morse_list = morse_to_text.split('.')  # makes list about the morse string
        for key in morse_key_table:  # creates morse table so we get decoding table
            new_key = repr(morse_key_table[key].encode('utf-8'))  # gets hex value of morse marks
            tmp_morse_key_table[new_key] = key  # saves letter as value

        for code in morse_list:  # decodes morse to letter
            if repr(code) in tmp_morse_key_table:  # checks key value
                text_result = text_result + tmp_morse_key_table[repr(code)]
                if tmp_morse_key_table[repr(code)] == '.':  # checks dot
                    text_result = text_result + '\n'  # adds new line in to text
            elif code == ' ':
                text_result = text_result + ' '  # adds white space in to text
            else:
                logging.debug("decode_to_text / not valid mark %s" % code.encode('hex'))

    return text_result.upper()  # returns decoded text string in UPPER case


def get_sample_text(text_file):
    """
    get_sample_text() -function opens the given text file and save the text content to string variable
    :param text_file: text file path name
    :return: sample_text: content of text file as string
    """
    logging.info("get_sample_text()")
    sample_text = ""
    try:
        with open(text_file, "r") as r:  # opens the file to read
            sample_text = r.read()  # saves file content
            if not re.match('([A-Za-z0-9])', sample_text):  # checks that sample is valid text
                sample_text = ""
    except EnvironmentError as e:
        logging.exception("get_sample_text / error in reading the file")

    return sample_text


def get_sample_morse(test_file):
    """
    get_sample_morse() -function opens the given morse file and save the content to string variable
    :param test_file: morse file path name
    :return: content of morse file as string
    """
    logging.info("get_sample_morse()")
    sample_morse = ""
    try:
        with open(test_file, "r") as r:  # open the file read
            sample_morse = r.read()  # saves file content
            if re.match('([A-Za-z0-9])', sample_morse):  # checks that sample string is valid
                sample_morse = ""
    except EnvironmentError as e:
        logging.exception("get_sample_morse / error in reading the file")

    return sample_morse


def save_result(file_name, result_item):
    """
    save_result() -function saves encoded/decoded string result in the file
    :param file_name: Morse.txt or Text.txt
    :param result_item: string to save in to file
    :return: status: True in success, False in failure
    """
    logging.info("save_result()")
    status = True
    try:
        with open(file_name, "w") as w:  # opens the file to write
            w.write(str(result_item))  # writes the content to file
    except Exception as e:
        logging.debug("save_result / error in writing the file {!s}".format(e))
        status = False

    return status  # returns status info


def simple_cli():
    """
    simple_cli() is simple command line interface
    :return: test_file: file to encode/decode,
             user_selection: user selection (1-3), see below
    """
    print ("Select number:")
    print ("1 - text to morse")
    print ("2 - morse to text")
    print ("3 - exit")
    user_selection = raw_input("Select: ")
    if user_selection == str(1):
        test_file = raw_input("Give text file name: ")
        if not os.path.exists(test_file):
            test_file = ""
            print ("Wrong file or path name")
    elif user_selection == str(2):
        test_file = raw_input("Give morse file name: ")
        if not os.path.exists(test_file):
            test_file = ""
            print ("Wrong file or path name")
    else:
        print ("Goodbye")
        sys.exit()

    return test_file, user_selection  # returns file path name and user selection


def main():
    """
    main() -function implements encoding/decoding the file content given by user using by sub functions
    """
    while True:
        test_file, selection = simple_cli()  # simple user CLI interface
        if test_file and selection == str(1):  # checks text file and use selection
            text_to_morse = get_sample_text(test_file)  # gets the sample text
            if text_to_morse:
                morse_result = encode_to_morse(text_to_morse)  # encodes the sample to morse
                if morse_result:
                    print ("Text to morse: \n %s" % morse_result)
                    status = save_result("Morse.txt", morse_result)  # saves result to file
                    if status:
                        print ("File saved")
                    else:
                        print ("Error in file saving")
                else:
                    print ("Nothing to encode")
            else:
                print ("No text to encode")
        elif test_file and selection == str(2):  # checks morse file and use selection
            morse_to_text = get_sample_morse(test_file)  # get sample morse
            if morse_to_text:
                text_result = decode_to_text(morse_to_text)  # decodes the sample to text
                if text_result:
                    print ("Morse to text: \n %s" % text_result)
                    status = save_result("Text.txt", text_result)  # saves result to file
                    if status:
                        print ("File saved")
                    else:
                        print ("Error in file saving")
                else:
                    print ("Nothing to decode")
            else:
                print ("No morse to decode")


if __name__ == '__main__':
    main()
