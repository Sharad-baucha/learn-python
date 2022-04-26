quiz = {
    1 : {
        "question" : "What is the first name of Iron Man?",
        "answer" : "Tony"
    },
    2 : {
        "question" : "Who is called the god of lightning in Avengers?",
        "answer" : "Thor"
    },
    3 : {
        "question" : "Who carries a shield of American flag theme in Avengers?",
        "answer" : "Captain America"
    },
    4 : {
        "question" : "Which avenger is green in color?",
        "answer" : "Hulk"
    },
    5 : {
        "question" : "Which avenger can change it's size?",
        "answer" : "AntMan"
    },
    6 : {
        "question" : "Which Avenger is red in color and has mind stone?",
        "answer" : "Vision"
    }
}

def check_ans(question, ans, attempts, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        if attempts - 1 == 0:
            print("Wrong Answer :( \n You have 0 attempts left! \n Try the next question")
        else:
            print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
            return False

score = 0

for question in quiz:
    attempts = 3
    while attempts > 0: 
        print("\n")
        print(quiz[question]['question']) # this will print the current interation of for loop
        answer = input("Enter Answer: ")
                
        check = check_ans(question, answer, attempts, score)
        if check:
            score += 1
            break
        attempts -= 1
    # if attempts == 0:
    #     print("Next question -->>")

