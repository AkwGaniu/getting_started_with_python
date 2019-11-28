from question import Questions

question_prompt = [
    "What year did Nigeria gain independence\n(a) 1960 \n(b) 1940 \n(c) 1945 \n(d) 1991",
    "What year was Nigeria amalgamated\n(a) 1960 \n(b) 1940 \n(c) 1945 \n(d) 1991",
    "Who is the first executive governor of Lagos state\n(a) Bola Tinubu \n(b) Sanwo Olu \n"
    "(c) Lateef Jakande \n(d) Rajii Fashola",
    "What year was LASU invented\n(a) 1989 \n(b) 1940 \n(c) 1945 \n(d) 1991"
]

list_of_questions = [
    Questions(question_prompt[0], "a"),
    Questions(question_prompt[1], "b"),
    Questions(question_prompt[2], "c"),
    Questions(question_prompt[3], "a")
]


def initialize_quiz(questions):
    score = 0
    for ques in questions:
        answer = input(ques.prompt + "\n: ")
        if answer.lower() == ques.ans:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " answer(s) correctly")


initialize_quiz(list_of_questions)

