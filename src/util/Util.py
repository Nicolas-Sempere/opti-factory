ROUND_PRECISION = 2
THIN_SPACE = " "


def roundNumber(x):
    return round(x, ROUND_PRECISION)


# Pads a string to the right with spaces
# "Hello" -> "Hello   "
def addSpaces(string, maxLength):
    return string + " " * (maxLength - len(string))


# Adds spaces every three digits
# 1000 -> 1 000
def readableInteger(number):
    number_str = str(number)[::-1]
    spaced_number = THIN_SPACE.join(
        number_str[i : i + 3] for i in range(0, len(number_str), 3)
    )
    spaced_number = spaced_number[::-1]
    return spaced_number.strip()
