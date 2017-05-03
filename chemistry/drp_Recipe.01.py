# drp_Q_Recipe.01.py
#
# This is intended to be a template for teachers to use if they want to include
# questions with randomized values.
# To include this question in a quiz, click the Share button, Link. Under Run Option
# select "Run code only".  Under Link Options, select "Only show output (hide the code)".
# Then copy the link, and paste it into the Title or Description field of a paragraph-type
# question.  If you have to enter an actual html link, here's the tag format:
# <a href="https://www.w3schools.com/" target="_blank">Visit W3Schools!</a>

from math import *
from random import *

def dec(var):
  if var < 10:
    return "%.2f" % var
  if var < 100:
    return "%.1f" % var
  else:
    return "%.0f" % var

def sci(var):
  return "%.2e" % var
  
def acceptable_answers(x):
 dig = 6 # did not investigate effects of changing DIG
 signif = round(pow(10, round(log(x, 10), dig) % 1), dig)

 power_term = log(x, 10)//1

 if signif < 1.010:
  min_signif = signif - 0.006
  max_signif = signif + 0.01  

 elif signif == 1:    
   min_signif = signif - 0.001
   max_signif = signif + 0.01

 elif signif > 9.991:    
   min_signif = signif - 0.01
   max_signif = signif + 0.06

 else:
   min_signif = signif - 0.01
   max_signif = signif + 0.01
 
 min_signif = round(min_signif, dig)
 max_signif = round(max_signif, dig)

 return [sci(min_signif * pow(10, power_term)),sci(signif * pow(10, power_term)),sci(max_signif * pow(10, power_term)),]

#answer = 9999 # for testing  

# this code works: 9999 down through 1005
# not:  1004 through 1002  
# this code works: 1001, 1000
                                                            #
#### above should stay unchanged ############################
max_submissions = 3
help_submissions = 2

cups_per_tbs = 1/16
servings = randrange(200, 800, 100) * 10  #/10
tbs_per_serving = randrange(1, 4, 1)  #/10   
cp_density = randrange(150, 200, 1)/1000
cc_density = randrange(150, 200, 1)/100

substance_table = [\
["chili powder", cp_density],\
["cream cheese", cc_density],\
]

i = randrange(0,1,1)   # testing
substance = substance_table[i][0]
density   = substance_table[i][1]

question = "A recipe calls for exactly " + str(10 * tbs_per_serving) + " tablespoons of " + substance + " \
per 10 servings.  Assume there are exactly 16 tablespoons of " + substance + " in a cup \
and that the density of " + substance + " is about " + str(density) + " pounds per cup.\n\n\
How many pounds of chili pepper do you need to feed one serving to each of " + str(servings) + " people?\n\n\
Express your answer in 'hyper-scientific' notation to three significant \
digits. For example: 1.23e+4, 4.56e+0 or 7.89e-12. Don't include units.\n\n"


answer = servings * tbs_per_serving * cups_per_tbs * density

provided_answer = str("The procedure calls for " + \
sci(answer) + " pounds of " + \
substance +". \
Acceptable numerical answers are " + \
str(acceptable_answers(answer)[0]) + ", " + \
str(acceptable_answers(answer)[1])  + " and " +  \
str(acceptable_answers(answer)[2]) + ".\n")

#### Should stay unchanged ####################################
                                                              #
submission = 1
wrong = True
print(answer)
#print(acceptable_answers(answer))
#print(provided_answer)

print(question)
while wrong and submission <= max_submissions:
  response = input("Your answer is: ")
  if response in acceptable_answers(answer):
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
