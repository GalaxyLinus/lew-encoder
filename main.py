inputtextraw = input("What to en/decrypt?\n").lower()
inputtext = inputtextraw
shortraw = "lew"
short = "@"
# shortraw = input("What short?\n").lower()


if "a" + shortraw + "a" in inputtext or "e" + shortraw + "e" in inputtext or "i" + shortraw + "i" in inputtext or "o" + shortraw + "o" in inputtext or "u" + shortraw + "u" in inputtext:
    # DECODE
    try:
        inputtext = inputtext.replace(shortraw, short)
        inputtext = inputtext.replace("e" + short + "e", "e")
        inputtext = inputtext.replace("a" + short + "a", "a")
        inputtext = inputtext.replace("i" + short + "i", "i")
        inputtext = inputtext.replace("o" + short + "o", "o")
        inputtext = inputtext.replace("u" + short + "u", "u")
        result = inputtext
    except:
        print("error")
    print('\n"' + inputtextraw + '" means:\n' + result + '\n')
else:
    # ENCODE
    try:
        inputtext = inputtext.replace("e", "e" + short + "e")
        inputtext = inputtext.replace("a", "a" + short + "a")
        inputtext = inputtext.replace("i", "i" + short + "i")
        inputtext = inputtext.replace("o", "o" + short + "o")
        inputtext = inputtext.replace("u", "u" + short + "u")
        result = inputtext.replace(short, shortraw)
    except:
        print("error")
    print('\n"' + inputtextraw + '" in ' + shortraw + ' code is:\n' + result + '\n')
