"""
 Word Occurrences
 Estimate: 20 minutes
 Actual:   40 minutes
 """
COLOUR_CODES = {"aliceblue": "#f0f8ff", "alizarin crimson": "#e32636 ", "amaranth": "#e52b50", "amber": "#ffbf00",
                "amethyst": "#9966cc", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0",
                "antiquewhite4": "#8b8378", "apricot": "#fbceb", "aqua": "#00ffff",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6"}
print(COLOUR_CODES)
colour_name = input("Enter a colour name: ").lower()
while colour_name != " ":
    try:
        print(COLOUR_CODES[colour_name])
        colour_name = input("Enter a colour name: ").lower()
    except KeyError:
        print("Invalid colour name")
        colour_name = input("Enter a colour name: ") .lower()






                              