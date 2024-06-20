"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
import code

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


def print_all_states():
    global code
    max_state = max(len(state) for state in CODE_TO_NAME.keys())
    for code in CODE_TO_NAME.keys():
        print(f"{code:{max_state}} is {CODE_TO_NAME[code]}")
    """print((code, 'is', CODE_TO_NAME[code]) for code in CODE_TO_NAME.keys())
       Why is the output an address"""


print_all_states()
