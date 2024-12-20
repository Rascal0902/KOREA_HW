###############################################
# COSE215 Problem 1. Extracting phone numbers #
###############################################

import re

def main():
    # Open the input file and read its content!!
    with open('input1.txt', 'r', encoding = "UTF-8") as file:
        content = file.read()

    pattern = r"\+82-10-(\d{4})-(\d{4})"
    matches = re.findall(pattern, content)

    for match in matches:
        
        front, back = match
        
        front_sum = sum(int(digit) for digit in front)
        back_sum = sum(int(digit) for digit in back)

        if back_sum >= front_sum:
            continue

        last = None
        for digit in back:
            last = digit

        print(last, end='')


""" EXECUTE """
if __name__ == "__main__":
    main()