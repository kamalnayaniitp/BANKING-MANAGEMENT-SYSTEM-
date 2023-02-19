
 #I assume that:

#The Twitter tweets are stored in a text file, with one tweet per line.
#The list of racial slurs is stored in a text file, with one slur per line.
#We want to check for partial matches of the slurs in the tweets, so we don't need to match the entire word. For example, if "asian" is a slur, the program should flag tweets that contain "Asian", "Asians", "asians", etc.
import re

# Load the list of racial slurs into a set
with open('racial_slurs.txt', 'r') as f:
    slur_set = set(line.strip().lower() for line in f)

# Define a function to check the profanity level of a sentence
def check_profanity(sentence):
    # Split the sentence into words and convert them to lowercase
    words = sentence.lower().split()
    
    # Count the number of slurs in the sentence
    num_slurs = 0
    for word in words:
        if any(re.search(r'\b{}\b'.format(re.escape(slur)), word) for slur in slur_set):
            num_slurs += 1
    
    # Determine the profanity level based on the number of slurs
    if num_slurs == 0:
        return "Clean"
    elif num_slurs == 1:
        return "Mild"
    elif num_slurs <= 3:
        return "Moderate"
    else:
        return "Severe"

# Open the file of Twitter tweets and check the profanity level of each sentence
with open('tweets.txt', 'r') as f:
    for line in f:
        line = line.strip()
        profanity_level = check_profanity(line)
        print("{}: {}".format(profanity_level, line))
        
        
        """This program first loads the list of racial slurs into a set for efficient lookups. It then defines a function check_profanity that takes a sentence as input and returns the profanity level based on the number of slurs in the sentence. The function first splits the sentence into words, converts them to lowercase, and then checks each word to see if it matches any of the slurs using regular expressions. The function then determines the profanity level based on the number of slurs found.

The program then opens the file of Twitter tweets and checks the profanity level of each sentence using the check_profanity function. It prints out the profanity level and the original sentence for each tweet. You can modify this program to write the results to a file or to store them in a data structure for further analysis.
"""
