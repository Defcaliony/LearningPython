import random

WORDS = {
    "plural_fruits": ["apples", "bananas", "oranges", "kiwis"],
    "uncountable_drink": ["water", "tea", "coffee", "juice", "whiskey"],
    "uncountable_thing": ["money", "time", "help", "information"],
    "place": ["park", "store", "city centre", "zoo"],
}

TEMPLATES = [
    {
        "template": "Can I have {some_any} {uncountable_drink}?",
        "answer": "some",
        "rule": "Це прохання (Request) -> використовуємо 'some' ",
    },
    {   "template": "There isn't {some_any} {uncountable_thing} left.",
        "answer": "any",
        "rule": "Заперечне речення (isn't) -> використовуємо 'any' ",
    },
]

def generate_sentence():
    # 1. Chose a random template from the TEMPLATES list
    item = random.choice(TEMPLATES)

    # 2.Create vocabulary for formating sentence
    # {some_any} -> "____"
    formatted_dict = {"some_any": "____"}

    # 3.
    for key, words_list in WORDS.items():
        if key in item["template"]:
            formatted_dict[key] = random.choice(words_list)

    # 4.
    sentence = item["template"].format(**formatted_dict)

    # Return clear sentence
    return sentence, item["answer"], item["rule"]

#print(generate_sentence()) = chek for work

def run_quize():
    print("=== Trainer: SOME vs ANY ===")
    print("Input 'some' or 'any'. For exit input 'exit'.\n")

    score = 0
    total = 0

    while True:
        #Take new generate sentece
        sentence, correct_answer, rule = generate_sentence()

        print(f"Sentence: {sentence}")
        user_input = input("Your answer (some/any): ").strip().lower()

        #exit for game
        if user_input == "exit":
            print(f"\nTraining complate! Your result: {score}/{total} ")
            break


        # Chek answer for clear
        if user_input == correct_answer:
            print("Correct!✅\n")
            score += 1
        else:
            print(f"Incorrect ❌. Correct answer: {correct_answer}")
            print(f" Explain: {rule}\n")

        total +=1

    # Main point for enter (to start program)
if __name__ == "__main__":
    run_quize()



