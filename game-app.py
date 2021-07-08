#console game starts

import random
import json


jsonfile = {
  "module": {
    "number": 1,
    "name": "Mathematics",
    "questions": 30,
    "revision": "2017-08-13"
  },
  "questions": [
    {
      "number": 1,
      "question": "Eighteen thousandths, written as a decimal, is:",
      "answers": [
        "0.0018",
        "0.018",
        "0.18"
      ],
      "correct_answer": 1
    },
    {
      "number": 2,
      "question": "The next number in the sequence <b>1, 3, 6, 10, </b> is:",
      "answers": [
        "12",
        "13",
        "14",
        "15"
      ],
      "correct_answer": 4
    }
  ]
}



class Questions:
    def __init__(self, questions, options, answers ):
        self.options = options
        self.answers = answers
        self.questions = questions

    def question(self):
        print(self.questions)

    def answers(self):
        print(" continue")

Questions(jsonfile["questions"][1],jsonfile["questions"][1], jsonfile["questions"][1])