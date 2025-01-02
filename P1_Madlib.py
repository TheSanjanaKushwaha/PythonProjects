#String Concatenation 
#Suppose we want to create a string that says "Subscribe to ____"
# newsletter="  Weekly Newsletter" #some string variable

# # Three ways to do this
# print("subscribe to" + newsletter) #adding a plus sign
# print("subscribe to {}".format(newsletter)) #string.format(newsletter) : put newsletter into the {} in the string
# print(f"subscribe to {newsletter}") #fstring : prepending an F in front of the string

adj=input("Adjective: ")
verb1=input("Verb: ")
verb2=input("Verb: ")
famous_person=input("Famous person: ")

madlib=f"Computer Programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
