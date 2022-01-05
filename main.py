# Get user input
inputtextraw = input("What to en/decrypt?\n")  # .lower()
# Get short input
shortraw = input("What short to use?\n")

# set the message to be translated (inputtext)
inputtext = inputtextraw
# set the short
shortraw = "lew"
# list of characters to check
vList = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']


def is_encoded(inputtext, shortraw):
    for c in vList:
        if c + shortraw + c in inputtext:
            return True

    return False


def decode_string(inputtext, shortraw):
    for c in vList:
        inputtext = inputtext.replace(c + shortraw, '')
    return inputtext


def encode_string(inputtext, shortraw):
    data = []

    for c in inputtext:
        if c in vList and not data:
            data.append(c + shortraw + c)
        elif c in vList and shortraw not in data[-1]:
            data.append(c + shortraw + c)
        else:
            data.append(c)

    return ''.join(data)


if is_encoded(inputtextraw, shortraw):
    result = decode_string(inputtext, shortraw)

    print('\n"' + inputtextraw + '" means:\n' + result + '\n')
else:
    result = encode_string(inputtext, shortraw)

    print('\n"' + inputtextraw + '" in ' + shortraw + ' code is:\n' + result + '\n')
