#console game starts

import random
import json

def name_in_log(name):
    if name in log:
       print(name, log[name])
    else:
        pass

def continue_or_start_again(choice):
    if choice == "continue":
        pass


jsonfile = '''{

  "questions": [
    {
      "number": 1,
      "question": "Eighteen thousandths, written as a decimal, is:",
      "answers": [
        "0.0018",
        "0.018",
        "0.18"
      ],
      "correct_answer": 0.0018
    },
    {
      "number": 2,
      "question": "The next number in the sequence 1, 3, 6, 10,  is:",
      "answers": [
        "12",
        "13",
        "14",
        "15"
      ],
      "correct_answer": 15
    }
  ]
}
'''

score = 0
data = json.loads(jsonfile)

opened = True

count = -1
log ={

}
while opened:
    name = input("your name: ")
    if name in log:
       print(name, log[name])
    for question in data["questions"]:
        print((question["question"] ))
        print("options", ":", question["answers"])
        answer = float(input(">>"))
        if answer == question["correct_answer"]:
            score = score+5
            print("correct answer")
            print("your score is ", score)
            
        continue_or_quit = input("continue or quit: ")
        if continue_or_quit == "continue":
            continue
        elif continue_or_quit == "quit":
            log[name] = score
            print(log)
            break


