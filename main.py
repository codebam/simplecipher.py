import sys
from random import randint

def make_rot(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

def argv2str(argv):
    output = ''
    for arg in sys.argv[1:]:
        output = str(output + arg + ' ')
    output = output[:-1]
    return output

def encrypt(argv):
    output = ''
    rand_rot = randint(1,25)
    rand_rot2 = randint(1,25)
    # output = str('rotation is ' + str(rand_rot) + '\n')
    # output = output + str('rotation2 is ' + str(rand_rot2) + '\n')
    rot = make_rot(rand_rot)
    rot2 = make_rot(rand_rot2)
    rotated_string = ''
    userString = argv2str(argv)
    for count, character in enumerate(userString, 1):
        if count % 2 == 0:
            rotated_string = rotated_string + rot2(character)
        else:
            rotated_string = rotated_string + rot(character)
    output = rotated_string
    return output

def main():
    if len(sys.argv) == 1:
        print("Not enough arguments")
        return
    else:
        print(encrypt(sys.argv))

if __name__ == "__main__":
    main()
