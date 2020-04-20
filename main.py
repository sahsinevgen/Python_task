import argparse


def caesar(text, key):
    result = ""
    for i in range(len(text)):
        if ord("a") <= ord(text[i]) and ord(text[i]) <= ord("z"):
            result += chr(ord("a") + (ord(text[i]) -  ord("a") + key) % 26)
        else:
            result += text[i]
    return result

def vigenere(text, key):
    result = ""
    for i in range(len(text)): 
        cur_key = ord(key[i % len(key)]) - ord("a")
        if ord("a") <= ord(text[i]) and ord(text[i]) <= ord("z"):
            result += chr(ord("a") + (ord(text[i]) -  ord("a") + cur_key) % 26)
        else:
            result += text[i]
    return result

def do_target():
    if args.target == "encode":
        text = input_file.read()
        if args.cipher == "caesar":
            result = caesar(text, int(args.key))
        if args.cipher == "vigenere":
            result = vigenere(text, args.key)
        output_file.write(result)

    if args.target == "decode":
        text = input_file.read()
        if args.cipher == "caesar":
            result = caesar(text, 26 - int(args.key))
        if args.cipher == "vigenere":
            real_key = ""
            for i in args.key:
                real_key += chr(ord("z") + 1 - (ord(i) - ord("a")))
            result = vigenere(text, real_key)
        output_file.write(result)
    
    if args.target == "get_frequencies":
        text = input_file.read()
        text.lower()
        frequencies = [0] * 26
        cnt = 0
        for i in text:
            if ord("a") <= ord(i) and ord(i) <= ord("z"):
                frequencies[ord(i) - ord("a")] += 1
                cnt += 1
        for i in frequencies:
            output_file.write(str(i/cnt) + "\n")
    
    if args.target == "hack":
        text = input_file.read()
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
            dist = 0;
            for i in range(26):
                dist += (real_frequencies[(i + key) % 26] - frequencies[i]) ** 2
            if key == 0 or best_dist > dist:
                best_key = key
                best_dist = dist
        result = caesar(text, int(best_key))
        output_file.write(result)

parser = argparse.ArgumentParser(description='')

parser.add_argument('target', type=str)
parser.add_argument('--input_file', action="store", dest="input_file", type=str)
parser.add_argument('--output_file', action="store", dest="output_file", type=str)
parser.add_argument('--frequencies_file', action="store", dest="frequencies_file", type=str)
parser.add_argument('--cipher', action="store", dest="cipher", type=str)
parser.add_argument('--key', action="store", dest="key")

args = parser.parse_args()
print(args)

print(args.key)

input_file = open(args.input_file, "r")
output_file = open(args.output_file, "w")

do_target()

input_file.close()
output_file.close()

#rc, message = ping_ip(args.ip, args.count)
#print(message)
