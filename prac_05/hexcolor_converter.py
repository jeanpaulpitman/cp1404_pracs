"""
CP1404/CP5632 Practical
Hexcolor dictionary lookup
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
HEXCOLOR_CODES = {"chartreuse1": "#7fff00", "coral": "#ff7f50", "DarkGreen": "#006400", "DarkOrange": "#ff8c00",
                  "DarkOrchid": "#9932cc", "DeepPink1": "#ff1493", "firebrick": "#b22222"}
# print(HEXCOLOR_CODES)
max_length = max(len(color) for color in HEXCOLOR_CODES)
for color in HEXCOLOR_CODES:
    print("{:{}} is {}".format(color, max_length, HEXCOLOR_CODES[color]))
color = input("Enter color name: ")
while color != "":
    if color in HEXCOLOR_CODES:
        print("{:{}} is {}".format(color, len(color), HEXCOLOR_CODES[color]))
    else:
        print("Invalid color name")
    color = input("Enter color name: ")
