#console game starts

import random
import json

def name_in_log(name):

    if name in name_score_log:
       print(name, name_score_log[name])
    else:
        pass


def quit(x):
    if x == "N":
        name_score_log[name] = score
        name_question_log[name] = question["question"]
    elif x == "Y":
        pass



def questioneer(data):
    score = 0
    for question in data["questions"]:
        print((question["question"]))
        print("options", ":", question["options"])
        answer = input(">> ").upper()
        if answer == question["correct"]:
            score = score + 5
            print("correct answer")
            print("your score is ", score)
            quit = input("quit (y/n) >>").upper()
            quit(quit)
#def checkpoint(name):
#    if name_in_log(name) and name in  name_question_log:





file = open("questions.json")


data = json.load(file)


count = -1
name_score_log = {

}
name_question_log = {

}
opened = True
while opened:
    name = input("your name: ")
    if name in name_score_log:
        print("Restart (y/n)")
        info = input(">> ").upper()
        if info == "Y":
            questioneer(data)



        elif info=="N":
            pass



    # elif info == "N":

    elif name not in name_score_log:
        score = 0
        for question in data["questions"]:
            print((question["question"] ))
            print("options", ":", question["options"])
            answer = input(">> ").upper()
            if answer == question["correct"]:
                score = score+5
                print("correct answer")
                print("your score is ", score)


                continue_or_quit = input("continue or quit: ")
                if continue_or_quit == "continue":
                    continue
                elif continue_or_quit == "quit":


                    name_score_log[name] = score
                    name_question_log[name] = question["question"]
                break






