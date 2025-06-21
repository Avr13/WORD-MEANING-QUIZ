# 📘 GRE Word Meaning Quiz

An interactive terminal-based quiz game to master **English Vocabulary**. This tool helps you **practice** or **test** your vocabulary knowledge in a fun and engaging way using multiple-choice questions.

---

## ✨ Features

* ✅ Uses **Barron's 800** word list in CSV for high-quality GRE preparation.
* 🧠 **Two game modes**:

  * **Practice Mode**: Learn at your own pace with unlimited retries.
  * **Test Mode**: Challenge yourself with a fixed number of questions.
* 🎯 Randomized multiple-choice questions to simulate real GRE-style tests.
* 📊 Instant feedback with scoring and detailed result summaries.
* ♻️ Reinforces learning by repeating incorrect words in practice mode.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gre-word-quiz.git
cd gre-word-quiz
```

### 2. Prepare the Data

Ensure your CSV file named `words.csv` is in the following format:

| Words    | Definition                     |
| -------- | ------------------------------ |
| Aberrant | deviating from the normal      |
| Zealot   | one who is fanatically devoted |
| ...      | ...                            |

**Note**: No headers with extra spaces; both columns must be present and correctly named.

### 3. Install Requirements

```bash
pip install pandas
```

### 4. Run the Quiz

```bash
python quiz.py
```

You'll be prompted to:

* Select a game mode (Practice or Test)
* Enter how many questions you want
* Start answering questions 🎉

---

## 🧑‍🏫 Use Cases

This quiz can be used in various contexts:

| Use Case                     | Description                                                                |
| ---------------------------- | -------------------------------------------------------------------------- |
| 🧪 **GRE Preparation**       | Ideal for revising Barron's 800 words with focused testing.                |
| 🎓 **Classroom Engagement**  | Teachers can use it as a fun vocabulary drill for students.                |
| 📈 **Personal Growth**       | Anyone interested in expanding their English vocabulary can benefit.       |
| 🛠️ **CLI Project Showcase** | A great beginner-friendly example of CLI apps using `pandas` and `random`. |

---

## 🛠️ Customization

You can modify:

* The word list by editing the `words.csv` file.
* The number of multiple-choice options.
* The quiz style (e.g., timed questions, hint mode) — great for future enhancements!

---

## 📂 Project Structure

```
gre-word-quiz/
│
├── quiz.py          # Main Python script
├── words.csv        # CSV file containing words and definitions
└── README.md        # Project documentation
```

---

## 🧩 Future Improvements

* Add difficulty levels (easy, medium, hard)
* Enable loading custom word lists
* Create a GUI version using Tkinter or PyQt
* Add spaced repetition support for smarter learning

---

## 🤝 Contributing

Have a cool idea? Found a bug? Contributions are welcome!

```bash
# Fork the repo, make changes, and submit a pull request
```

## 🙋‍♀️ Made for Learners, by a Learner

Whether you're preparing for the GRE or just love challenging your vocabulary, this quiz is for you. Happy learning! 💪

---

