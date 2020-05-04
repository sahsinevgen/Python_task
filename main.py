import argparse
import sys


def read_input(name_of_file):
    if name_of_file is None:
        return ''.join(sys.stdin.readlines())
    input_file = open(name_of_file, "r")
    input = input_file.read()
    input_file.close()
    return input


def write_output(name_of_file, output):
    if name_of_file is None:
        print(output)
        return
    output_file = open(name_of_file, "w")
    output_file.write(output)
    output_file.close()


def encode_symbol(symbol, key):
    if ord("a") <= ord(symbol) and ord(symbol) <= ord("z"):
        return chr(ord("a") + (ord(symbol) - ord("a") + key) % 26)
    if ord("A") <= ord(symbol) and ord(symbol) <= ord("Z"):
        return chr(ord("A") + (ord(symbol) - ord("A") + key) % 26)
    return symbol


def caesar(text, key):
    result = ""
    for i in range(len(text)):
        result += encode_symbol(text[i], key)
    return result


def vigenere(text, key):
    result = ""
    for i in range(len(text)):
        current_key = ord(key[i % len(key)]) - ord("a")
        result += encode_symbol(text[i], current_key)
    return result


def do_target():
    if (required_input_text.count(args.target)):
        text = read_input(args.input_file)

    if args.target == "encode":
        if args.cipher == "caesar":
            result = caesar(text, int(args.key))
        if args.cipher == "vigenere":
            result = vigenere(text, args.key)

    if args.target == "decode":
        if args.cipher == "caesar":
            result = caesar(text, 26 - int(args.key))
        if args.cipher == "vigenere":
            real_key = ""
            for i in args.key:
                real_key += chr(ord("z") + 1 - (ord(i) - ord("a")))
            result = vigenere(text, real_key)

    if args.target == "get_frequencies":
        text.lower()
        frequencies = [0] * 26
        result = ""
        cnt = 0
        for i in text:
            if ord("a") <= ord(i) and ord(i) <= ord("z"):
                frequencies[ord(i) - ord("a")] += 1
                cnt += 1
        for i in frequencies:
            result += (str(i/cnt) + "\n")

    if args.target == "hack":
        frequencies_file = open(args.frequencies_file, "r")
        real_frequencies = []
        for line in frequencies_file:
            real_frequencies += [float(line)]
        frequencies = [0] * 26
        cnt = 0
        for i in text:
            if ord("a") <= ord(i) and ord(i) <= ord("z"):
                frequencies[ord(i) - ord("a")] += 1
                cnt += 1
        for key in range(26):
            dist = 0
            for i in range(26):
                dist += (
                    (real_frequencies[(i + key) % 26] - frequencies[i]) ** 2
                )
            if key == 0 or best_dist > dist:
                best_key = key
                best_dist = dist
        result = caesar(text, int(best_key))

    if (required_output_text.count(args.target)):
        write_output(args.output_file, result)


parser = argparse.ArgumentParser(description='')

parser.add_argument('target', type=str)
parser.add_argument('--input_file',
                    action="store",
                    dest="input_file",
                    type=str)
parser.add_argument('--output_file',
                    action="store",
                    dest="output_file",
                    type=str)
parser.add_argument('--frequencies_file',
                    action="store",
                    dest="frequencies_file",
                    type=str)
parser.add_argument('--cipher',
                    action="store",
                    dest="cipher",
                    type=str)
parser.add_argument('--key',
                    action="store",
                    dest="key")

args = parser.parse_args()

required_input_text = ["encode",
                       "decode",
                       "get_frequencies",
                       "hack"]
required_output_text = ["encode",
                        "decode",
                        "get_frequencies",
                        "hack"]

do_target()

