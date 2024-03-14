import random
responses={
    "hi":["hello!!"],
     "How are you?":["i am fine"],
     "bye":["Good bye!"],
     "tell me one joke":["i am not good in joke listen someone ask maths that why you are always sad, maths told i have so many problems"]
}
def get_responses(user_input):
    if user_input.lower() in responses:
        return random.choice(get_responses[user_input.lower()])
    else:
        return "sorry i didn't get you!"
def main():
    print("welcome to chatBot")
    print("Enter 'bye' to exit ")
    while True:
        user_input=input('you: ')
        if user_input.lower()=='bye':
            print(get_responses(user_input))
            break
        else:
            print(get_responses(user_input))
if __name__=="__main__":
   main()