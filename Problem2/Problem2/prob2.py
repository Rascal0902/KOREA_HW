##################################################
# COSE215 Problem 2. Extracting special patterns #
##################################################

import re

def main():
    # Open the input file and read its content!!
    with open('input2.txt', 'r', encoding = "UTF-8") as file:
        content = file.read()

    pattern = r'[A-Z]+\d+'
    matches = re.findall(pattern, content)

    for match in matches:
        print(match[0], end='')

""" EXECUTE """
if __name__ == "__main__":
    main()