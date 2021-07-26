import json


def questioneer(data, x=None, score=None):
    while x != len(data["questions"]):
        question_position = data["questions"][x]
        print(question_position["question"])
        print(question_position["options"])
        answer = input(">> ").upper()
        question_position = data["questions"][x]
        if answer == question_position["correct"]:
            score = score + 5
            print("correct", score)
        elif answer != question_position["correct"]:
            print("wrong", score)
        x = x + 1
        
    return score, x


def log(name, data, score_log, checkpoint_log):

    if name in score_log:
        answer = questioneer(data, x=checkpoint_log[name], score=score_log[name])

    elif name not in score_log:
        answer = questioneer(data, x, score)

    return answer


def quit(name, x, score, score_log, checkpoint_log):
    quit = input("quit>> ").upper()
    if quit == "Y":
        score_log[name] = score
        checkpoint_log[name] = x
    elif quit == "N":
        pass


file = open("questions.json")

json_file = json.load(file)

name_score_log = {"m":5}
name_checkpoint_log = {"m":5}

score = 0
x = 0
name = input("name: ")
answer = log(name, json_file, name_score_log, name_checkpoint_log)

