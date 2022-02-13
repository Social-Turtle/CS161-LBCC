term_to_match = 'alphabetical'
#term we need the user to type
for i in term_to_match: 
    #to be honest, I'm not entirely sure how I got this to work, just messed around enough to get something servicably working indefinitely, but I'd love your explanation as to what it's actually doing here...
    input_string = str(input("Input a word! "))
    #user input
    if term_to_match == input_string:
        print("pbil")