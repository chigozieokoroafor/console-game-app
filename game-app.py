#console game starts

import random
import json

class Questions:
    def __init__(self, questions, options, answers ):
        self.options = options
        self.answers = answers
        self.questions = questions

    def question(self, questions):
        self.questions = questions
        print(self.questions)

    def answers(self):
        print(" continue")


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

count = 0
data = json.loads(jsonfile)

for question in data["questions"]:
    print((question["question"] ))
    print("options", ":", question["answers"])
    answer = float(input(">>"))
    if answer == question["correct_answer"]:
        count = count+5
        print("correct answer")
        print("your score is ", count)
