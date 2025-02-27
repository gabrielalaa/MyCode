import json
with open ("Quiz/questions.json", encoding="utf-8") as file:
    data = json.load(file)
    score = 0
    for i in data:
        print(f"Question: {i['question']}")
        print(f"A: {i['question']}")
        print(f"B: {i['question']}")
        print(f"C: {i['question']}")
        print(f"D: {i['question']}")
        a = input("Your answer is:")
        if a == i["answer"]:
            score += 1
        else:
            print(f"The correct answer is {i['answer']}")
print(score)