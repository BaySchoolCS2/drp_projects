# drp_Q_Recipe.01.py
#
# This is intended to be a template for teachers to use if they want to include
# questions with randomized values.
# To include this question in a quiz, click the Share button, Link. Under Run Option
# select "Run code only".  Under Link Options, select "Only show output (hide the code)".
# Then copy the link, and paste it into the Title or Description field of a paragraph-type
# question.  If you have to enter an actual html link, here's the tag format:
# <a href="https://www.w3schools.com/" target="_blank">Visit W3Schools!</a>

import random


def generate_acceptable_answers(correct_answer):
    """ Calculates acceptable answers (answers accurate to e+1)
    Args:
         correct_answer (float)

    Returns:
         list of len 3

    Example:
    >>> generate_acceptable_answers(5)
    ['4.99e0', '5.00e0', '5.01e0']
    >>> generate_acceptable_answers(50)
    ['4.99e1', '5.00e1', '5.01e1']
    >>> generate_acceptable_answers(1001)
    ['9.90e2', '1.00e3', '1.01e3']
    >>> generate_acceptable_answers(0.03)
    ['2.99e-2', '3.00e-2', '3.01e-2']
    """
    correct_answer = convert_to_scientific_notation(correct_answer)
    number, exponent = correct_answer.split("e")
    number = float(number)
    max_number = number + .01
    min_number = number - .01
    max_number = str(max_number) + "e" + exponent
    min_number = str(min_number) + "e" + exponent

    min_number = convert_to_scientific_notation(float(min_number))
    correct_answer = convert_to_scientific_notation(float(correct_answer))
    max_number = convert_to_scientific_notation(float(max_number))

    return [min_number, correct_answer, max_number]


def convert_to_scientific_notation(number):
    """ Converts a number to scientific notation
    Args:
         number (float)

    Returns:
         String

    Example:
    >>> convert_to_scientific_notation(5)
    '5.00e0'
    >>> convert_to_scientific_notation(10)
    '1.00e1'
    >>> convert_to_scientific_notation(-100)
    '-1.00e2'
    >>> convert_to_scientific_notation(0.01)
    '1.00e-2'
    """

    number = "%.2e" % number
    if "+" in number:
        positive = True
        number, exponent = number.split("+")
    else:
        positive = False
        number, exponent = number.split("-")

    exponent = str(int(exponent))  # Removes leading zeros

    if positive:
        return number + exponent
    else:
        return number + "-" + exponent


def is_acceptable_answer(acceptable_answers, response):
    """ Determines if an answer is within the range of acceptable answers
    Args:
        acceptable_answers (list(String))
        response (String)

    Returns:
        bool: True of the answer is acceptable, false otherwise

    """
    response = float(response)
    min_value = float(acceptable_answers[0])
    max_value = float(acceptable_answers[-1])

    if min_value <= float(response) <= max_value:
        return True

    return False


def is_hyper_scientific(number):
    """ Determines if an answer is hyper-scientific
    Args:
        number (String)
    Returns:
        bool: True if is hyper-scientific, False otherwise
    Example:
    >>> is_hyper_scientific("1.00e2")
    True
    >>> is_hyper_scientific("100")
    False
    >>> is_hyper_scientific("1.234e5")
    False
    """
    if convert_to_scientific_notation(float(number)) == number:
        return True
    return False


max_submissions = 3
help_submissions = 2

cups_per_tbs = 1 / 16
servings = random.randrange(200, 800, 100) * 10  # /10
tbs_per_serving = random.randrange(1, 4, 1)  # /10
cp_density = random.randrange(150, 200, 1) / 1000
cc_density = random.randrange(150, 200, 1) / 100

substance_table = {"chili powder": cp_density, "cream cheese": cc_density}

substance, density = random.choice(list(substance_table.items()))  # Change this to random.choice

question = "A recipe calls for exactly " + str(10 * tbs_per_serving) + " tablespoons of " + substance + " \
per 10 servings.  Assume there are exactly 16 tablespoons of " + substance + " in a cup \
and that the density of " + substance + " is about " + str(density) + " pounds per cup.\n\n\
How many pounds of chili pepper do you need to feed one serving to each of " + str(servings) + " people?\n\n\
Express your answer in 'hyper-scientific' notation to three significant \
digits. For example: 1.23e+4, 4.56e+0 or 7.89e-12. Don't include units.\n\n"

answer = servings * tbs_per_serving * cups_per_tbs * density

# TODO remove test
answer = 100

acceptable_answers = generate_acceptable_answers(answer)

provided_answer = "The procedure calls for " + \
                  convert_to_scientific_notation(answer) + " pounds of " + \
                  substance + "." + \
                  "\nAcceptable numerical answers are " + \
                  acceptable_answers[0] + ", " + \
                  acceptable_answers[1] + " and " + \
                  acceptable_answers[2] + "."

# ____________________________Should stay unchanged____________________________

submission = 1
wrong = True
print(answer)
# print(acceptable_answers(answer))
# print(provided_answer)


print(question)
while wrong and submission <= max_submissions:
    response = input("Your answer is: ")
    if is_acceptable_answer(acceptable_answers, response) and is_hyper_scientific(response):
        wrong = False
        print("Your answer is correct (or close enough).")
    elif submission == 1:
        print("Hmm. Try again. It might just be a matter of your notation.\n")
    elif submission in range(2, max_submissions):
        print("Hmm. Try again.\n")
    elif submission == max_submissions:
        print("Sorry, no more submissions.  Try another version.\n")
    submission += 1

print(provided_answer)
if submission > help_submissions:
    print("Make a note that you need help answering this type of question.")
