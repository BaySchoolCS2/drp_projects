"""
This is a file dedicated to the chemistry project - I used my proof of concept work from my "misc_projects.py" file,
but have modified them, for instance, to use the 'periodictable' module instead of 'periodic.'
Also, this file will be the one I am working on from now on for this problem
-David Yawata
"""
import random
import periodictable


def question(correct_answer):
    """
    queries the user for an answer, printing congratulations and returning true if it is correct,
    and printing encouragement and giving them another shot if not
    """
    if str(input("Your answer: ")) == str(correct_answer): return 0 #asks for the user's answer. If it's correct, 0 is returned
    else: #else, meaning that the answer was incorrect
        print("Try again!")
        return 1+question(correct_answer) #gives the user another chance, but adds one to the return value, which ends up being the amount of times they got it wrong

def chem_question():
    """
    picks a random number, which becomes an element, and asks a question randomly from a list about properties of that element
    """
    correct_element = periodictable.elements[random.randint(1,100)] #chooses which element the person will be asked about
    question_ls = [["What is the name of the element with the atomic number "+str(correct_element.number)+"?", correct_element.name], ["What is the atomic number of the element \'"+correct_element.name+"\'?", correct_element.number]] #list of all possible quesitons - easily expandable
    question_number = random.randint(0, len(question_ls)-1) #randomly picks which question will be asked
    #question_number = 1 #FOR USE IN DEBUGGING
    print(question_ls[question_number][0]) #prints the question
    score = question(question_ls[question_number][1]) #lets the user input answers until they get it right, records how many times they got it wrong
    if score == 0: print("0 incorrect answers") #these three print out statements based on how well they do - numbers are adjustable
    elif score < 3: print("1-2 incorrect answers")
    else: print("3+ incorrect answers")
    return #could use this to keep track of score across multiple questions

print("-------------------------------------------------------------------------------")
print("Keep in mind that all element names must be all lowercase,")
print("and that all element symbols must be all uppercase")
print("-------------------------------------------------------------------------------")
