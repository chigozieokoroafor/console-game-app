import json


def questioneer(data, x):
    while x != len(data["questions"]):
        question_position = data["questions"][x]
        print(question_position["question"])
        print(question_position["options"])
        ans = input(">> ").upper()
        x = x + 1
    return ans


def scorer(data, answer, x, score):
    question_position = data["questions"][x]
    if answer == question_position["correct"]:
        score = score+5
        print("correct", score)
    elif answer != question_position["correct"]:
        print("wrong", score)
    return score



def log(name, data, x, score_log, checkpoint_log):
    if  name in score_log:
        answer = questioneer(data, checkpoint_log[name])
    elif name not in score_log:
        answer = questioneer(data, x=0)
    return answer

def quit(name,quit, x, score,score_log, checkpoint_log):
    if quit =="Y":
        score_log[name] = score
        checkpoint_log[name] = x
    elif quit == "N":
        pass



file = open("questions.json")

json_file = json.load(file)



name_score_log = {}
name_checkpoint_log = {}

score = 0
x = 0
name = input("name: ")
answer = log(name, json_file, x,name_score_log, name_checkpoint_log)
score =  scorer(json_file, answer, x, score)





