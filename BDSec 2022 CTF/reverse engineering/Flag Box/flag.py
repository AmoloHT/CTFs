frag = open('frag.txt', 'r').read().splitlines()
for character in frag:
    print(character[33], end='')
