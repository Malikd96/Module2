#Task1  Below is a piece of Python code with incorrect indentation. 
# Your task is to correct it.

weather = "sunny"
if weather == "sunny":
    print("Wear sunglasses")
else:
    print("Take an unbrella!")

#Task2: Your mood today. Ask the user how they feel today. 
# If they say "happy", print "That's great to hear!", 
# and if they say "sad", print "I hope your day gets better!".

def respond_to_mood(user_mood):
    if user_mood.lower() =="happy":
        print("That's great to hear!")
    elif user_mood.lower() =="sad":
        print("I hope your day gets better.")