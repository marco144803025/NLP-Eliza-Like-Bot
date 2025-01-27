import re
import random

def read_shakespeare_text(file_path="shakes.txt"):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text  # For demonstration, we'll only show the first 10000 characters

# ------------------------------------------------------------------------
# Question 1
# ------------------------------------------------------------------------

def question1_1_all_alphabetic(file_path="shakes.txt"):

    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'[A-Za-z]')  # Entire line: one or more alphabetic chars

    print("\n--- Question 1.1: All Alphabetic Lines ---")
    for line in lines[:10]:
        if pattern.match(line):
            print(line)
    print("-------------------1.1---------------------------\n")

def question1_2_lowercase_ending_in_b(file_path="shakes.txt"):
   
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'[a-z]+b$')  # All lowercase, must end with 'b'

    print("\n--- Question 1.2: Lowercase Lines Ending in 'b' ---")
    for line in lines[:1000]:
        for word in line.split():
            if pattern.match(word):
                print(word)
    print("-------------------1.3---------------------------\n")

def question1_3_bab_condition(file_path="shakes.txt"):

    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'b*(bab)b*')  #

    print("\n--- Question 1.3: Strings Where Each 'a' Is Surrounded by 'b' ---")
    for line in lines:
        for word in line.split():
            if pattern.match(word):  
               print(word)
    print("-------------------1.3---------------------------\n")

# ------------------------------------------------------------------------
# Question 2
# ------------------------------------------------------------------------

def question2_1_two_consecutive_repeated_words(file_path="shakes.txt"):
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'\b([A-Za-z]+)\b\s+\1\b')

    print("\n--- Question 2.1: Lines with Two Consecutive Repeated Words ---")
    for line in lines[:20000]:
        match = pattern.search(line)
        if match:
            repeated_words = match.group(0)
            print(repeated_words)
    print("-------------------2.1---------------------------\n")

def question2_2_starts_with_integer_ends_with_word(file_path="shakes.txt"):
   
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'^\d+.*\b\w+\b$')
    print("\n--- Question 2.2: Lines Starting with an Integer, Ending with a Word ---")
    for line in lines:
        if pattern.match(line):
            print(line)
    print("--- End Question 2.2 ---\n")

def question2_3_contain_grotto_and_raven(file_path="shakes.txt"):
 
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'(?=.*\bgrotto\b)(?=.*\braven\b)')

    print("\n--- Question 2.3: Lines Containing Both 'grotto' and 'raven' ---")
    for line in lines[:100]:
        if pattern.match(line):
            print(line)
    print("--- End Question 2.3 ---\n")

def question2_4_capture_first_word(file_path="shakes.txt"):
   
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'^[^A-Za-z]*([A-Za-z]+)')

    print("\n--- Question 2.4: Capturing the First Word in Each Line ---")
    for line in lines[:10]:
        match = pattern.match(line)
        if match:
            # match.group(1) is the first captured word
            captured_word = match.group(1)
            print(f"Line: {line}\n --> First word captured: '{captured_word}'\n")
    print("--- End Question 2.4 ---\n")



if __name__ == "__main__":
    
    # question1_1_all_alphabetic()
    # question1_2_lowercase_ending_in_b()
    # question1_3_bab_condition()

    # question2_1_two_consecutive_repeated_words()
    # question2_2_starts_with_integer_ends_with_word()
    # question2_3_contain_grotto_and_raven()
    question2_4_capture_first_word()
