import pandas as pd
import random

class QUIZ():
    def __init__(self, ):
        print("📘 Welcome to the Word Meaning Quiz!\n")
        self.type = int(input("Choose Game Type:\n 1.Practice\n 2.Test \nEnter your choice: "))
        self.num_of_ques = int(input("\nHow many words would you like to be tested on: "))
        self.file_name = 'words.csv'
        self.row_range_start = 1
        self.row_range_end = 1
        self.last_question_asked = None
        self.incorrect = []
        self.load_game()

        if self.type == 1:
            self.play_game_practice()
        else: 
            self.play_game_test()
    
    def load_game(self):
        df = pd.read_csv(self.file_name)

        words = []
        for _, row in df.iterrows():
            words.append({
                "word": row["Words"].strip(),
                "definition": row["Definition"].strip()
            })
        
        self.words = words
        words_ranged = words[self.row_range_start-1 : self.row_range_end]
        self.words_to_ask =  random.sample(words_ranged, min(self.num_of_ques, len(words_ranged)))
    
    def question(self):
        word_entry = random.choice(self.words_to_ask)

        word = word_entry["word"]
        definition = word_entry["definition"]
        choices = [definition]
        while len(choices) < 5:
            cand = random.choice(list(self.words))
            if cand["definition"] not in choices:
                choices.append(cand["definition"])
            if len(choices) == len(self.words):
                break
        random.shuffle(choices)
        ques = {"word": word, "answer": definition, "choices": choices}

        return ques
    
    def play_game_practice(self):
        count = 0
        correct_count = 0

        while len(self.words_to_ask)+len(self.incorrect) > correct_count:
            ques = self.question()
            if self.last_question_asked == ques["word"] and len(self.words_to_ask) != 1:
                continue
            self.last_question_asked = ques["word"]

            print(f"QUESTIONS: {correct_count}/{len(self.words_to_ask)+len(self.incorrect)}\n")
            print("🔤 What is the meaning of the word:", ques["word"])
            for idx, opt in enumerate(ques["choices"], 1):
                print(f"{idx}. {opt}")

            try:
                choice = int(input("Choose the correct option (1-5): "))
                if ques["choices"][choice - 1] == ques["answer"]:
                    print("✅ Correct!\n\n")
                    correct_count += 1

                else:
                    print(f"❌ Incorrect! Correct definition: {ques['answer']}\n\n")

                    if all(ques["word"] != item["word"] for item in self.incorrect):
                        self.incorrect.append({"word": ques["word"], "definition": ques["answer"]})
                
                count += 1
                
            except (ValueError, IndexError):
                print("⚠️ Invalid input. Try again.")
        
        self.results(correct_count,count)
    
    def play_game_test(self):
        count = 0
        correct_count = 0

        while self.words_to_ask:
            ques = self.question()
            if self.last_question_asked == ques["word"] and len(self.words_to_ask) != 1:
                continue
            self.last_question_asked = ques["word"]

            print(f"QUESTIONS: {count}/{self.num_of_ques}\n")
            print("🔤 What is the meaning of the word:", ques["word"])
            for idx, opt in enumerate(ques["choices"], 1):
                print(f"{idx}. {opt}")

            try:
                choice = int(input("Choose the correct option (1-5): "))
                if ques["choices"][choice - 1] == ques["answer"]:
                    print("✅ Correct!\n\n")
                    correct_count += 1

                else:
                    print(f"❌ Incorrect! Correct definition: {ques['answer']}\n\n")

                    if all(ques["word"] != item["word"] for item in self.incorrect):
                        self.incorrect.append({"word": ques["word"], "definition": ques["answer"]})
                
                count += 1
                self.words_to_ask = [d for d in self.words_to_ask if d.get("word") != ques["word"]]
                
            except (ValueError, IndexError):
                print("⚠️ Invalid input. Try again.")
        
        self.results(correct_count,count)
    
    def results(self, correct, count):
        print("\n🎉 Quiz Complete!")
        print(f"✅ Total correctly identifed words: {correct}")
        if count-correct != 0:
            print("\n❌ Words you got wrong:", count-correct)
            for incorrects in self.incorrect:
                print(f"\n- {incorrects['word']} : {incorrects['definition']}")
        else:
            print("🥳 Perfect score! No incorrect answers.")

QUIZ()

        