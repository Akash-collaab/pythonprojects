# a dictionary that stores  questions and answer
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong 
# show the final result when is completed

quiz = {
    "question1": {
        "question": "What is the capital of India",
        "answer": "delhi"
    },
    "question2": {
        "question": "Who is the person you loved the most?",
        "answer": "mom"
    },
    "question3": {
        "question": "What .py stands for ?",
        "answer": "python"
    },
    "question4": {
        "question": "Whom you miss the most",
        "answer": "dad"
    },
    "question5": {
        "question": "What's my favourite color?",
        "answer": "white"
    }
    
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is " + str(score))
        print("")
        print("")

    else:
        print("Wrong:")
        print("The answer is : "+ value['answer'])
        print("Your score is :"+ str(score))
        print("")
        print("")

    print("You get "+ str(score) + "out of 5 ")
    print("Your percentage is "+ str(score/5*100) +"%")

    