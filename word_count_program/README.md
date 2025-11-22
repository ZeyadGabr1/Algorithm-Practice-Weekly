# 📝 Word Counter Program

A simple yet effective program that counts **alphabetical words only** in a given text. It ignores numbers, punctuation marks, and extra spaces, ensuring accurate word counting using a custom algorithm — not built‑in split methods.

---

## 🔧 **Tools & Technologies Used**

* **Python 3**
* **Object-Oriented Programming (OOP)**
* Custom text‑parsing algorithm
* Terminal input/output (CLI)

---

## 🌟 **Project Features**

* Counts words using a manual algorithm.
* Ignores commas, periods, numbers, and special characters.
* Detects the start and end of words through character inspection.
* Clean OOP structure for easier maintenance and extension.
* Beginner-friendly and great for learning logical thinking.

---

## 🚀 **How the Program Works**

The program follows a clear algorithm:

### **Step 1 — Input & Preprocessing**

* The program asks the user to enter a text.
* The text is cleaned by converting it to lowercase and stripping extra spaces.

### **Step 2 — Iterating Through Each Character**

* A loop checks each character in the text.
* A flag (`in_word`) is used to track whether the loop is currently inside a word.

### **Step 3 — Detecting Word Boundaries**

* If the character is alphabetical and `in_word` is False → a new word starts.
* If the character is not alphabetical → the word ends.
* Numbers, spaces, and punctuation are completely ignored.

### **Step 4 — Output**

* The final word count is printed to the user.

---

## 📂 **Project Structure**

```
📁 word_counter
│
├── main.py        # The program logic (WordCounter class)
└── README.md      # Project documentation
```

---

## ▶️ **How to Run the Program**

### **1. Clone the Repository**

```bash
git clone https://github.com/ZeyadGabr1/Algorithm-Practice-Weekly.git
cd Algorithm-Practice-Weekly/word_count_program
python3 main.py
```

### **2. Run the Program**

```bash
python3 main.py
```

---

## 💻 **Program Preview (How It Looks When Running)**

```
 ****************************** 
 Welcome In Word Counter Program 
 ****************************** 

Please enter the full text my dear : Learning algorithms improves your logical thinking and problem solving skills.

 ------------------------------ 
 I'm finished! The number of words in the text is : 10 
 ------------------------------
```

---

The program will ask you to enter a text, then it will display the total number of alphabetical words.
---

## 📘 Example

**Input:**

```
Hello, my friend! I have 2 cats and 1 dog.
```

**Output:**

```
I'm finished! The number of words in the text is: 8
```

---

## 💡 Future Improvements

* Add GUI version.
* Add support for multiple languages.
* Add unit tests (pytest).
* Add option to count numbers separately.

---

## 👨‍💻 Author

Created by **Zeyad** as part of algorithmic thinking training.

Feel free to use, modify, or contribute!
