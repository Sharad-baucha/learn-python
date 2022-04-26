quiz = {
    1 : {
        "question" : "What is the first name of Iron Man?",
        "answer" : {
            "a" : "Tony",
            "b" : "Sharad",
            "c" : "Noob",
            "d" : "Mike"
        } ,
        "correct_ans" : "a"
    },
    2 : {
        "question" : "Who is called the god of lightning in Avengers?",
        "answer" : {
            "a" : "Tony",
            "b" : "Sharad",
            "c" : "Thor",
            "d" : "Mike"
        }
        ,
        "correct_ans" : "c"
    },
    3 : {
        "question" : "Who carries a shield of American flag theme in Avengers?",
        "answer" : {
            "a" : "Tony",
            "b" : "Batman",
            "c" : "Captain America",
            "d" : "Black Panther"
        }
        ,
        "correct_ans" : "c"
    },
    4 : {
        "question" : "Which avenger is green in color?",
        "answer" : {
            "a" : "Tony",
            "b" : "Vision",
            "c" : "Spider Man",
            "d" : "Hulk"
        }
        ,
        "correct_ans" : "d"
    },
    5 : {
        "question" : "Which avenger can change it's size?",
        "answer" : {
            "a" : "Ant Man",
            "b" : "Sharad",
            "c" : "Motu Ashish",
            "d" : "Pidarp vai"
        }
        ,
        "correct_ans" : "a"
    },
    6 : {
        "question" : "Which Avenger is red in color and has mind stone?",
        "answer" : {
            "a" : "Spider Man",
            "b" : "Super Man",
            "c" : "Iron Man",
            "d" : "Vision"
        }
        ,
        "correct_ans" : "d"
    }
}
score = 0
q_no = 1

def check_ans(question, ans ,score,q):
    if quiz[question]["correct_ans"] == ans.lower():
        if q == 6:
            print("\n\t\t\tCorrect Answer!")
        else:
            print("\n\t\t\tCorrect Answer!\tOn to the next question-->>")
        return True
    else:
        if q == 6:
            print("\n\t\t\tWrong Answer :(")
        else:
            print("\n\t\t\tWrong Answer :(\tTry the next question-->>")
        return False

for question in quiz:
 
    print("\n")
    print(f"\t\t#Question Number:{q_no}")
    print(quiz[question]['question'])
    print("a =", end=' ')
    print(quiz[question]["answer"]["a"], end=' ' "\t\t")
    print("b =", end=' ')
    print(quiz[question]["answer"]["b"], end=' ' "\t\t")
    print("c =", end=' ')
    print(quiz[question]["answer"]["c"], end=' ' "\t\t")
    print("d =", end=' ')
    print(quiz[question]["answer"]["d"], end=' ' "\t\t")
    print("\n")
    answer = input("Enter your choice a or b or c or d: ")
                
    check = check_ans(question, answer, score, q_no)
    if check:
        score += 1
    
    q_no += 1

print("\n\t\t\t\tThe Quiz is over!!!!!!!")        
if score == 0:
    print("\t\t\t\tYou only scored 0. Good Luck next time :)\n")

elif score == 1 or score ==2 or score == 3:
    print(f"\t\t\t\tYour score is {score}.You did well.\n\t\t\t\tYou can do better !!!!!\n")

elif score == 4 or score == 5:
    print(f"\t\t\t\tYour score is {score}.You did very well.Congratulaions!!!!!!\n")

else:
    print(f"\t\t\t\tYour score is {score}.\n\t\t\t\tCongratulations!!!! You beat the quiz.\n\n\t\t\t\tYOU WILL GET REAL JUICE AS A PRIZE.\n")

