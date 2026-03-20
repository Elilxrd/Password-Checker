# 🔐 Password Strength Checker + ML

A Python tool that evaluates the strength of a password using **basic rules** and an **optional ML classifier**.  
This project demonstrates Python scripting, cybersecurity concepts, and a simple machine learning workflow.

---

## ⚙️ Features

- **Basic Password Strength Checker**
  - Scores passwords based on length, uppercase, lowercase, numbers, and special characters
  - Classifies as **Weak / Medium / Strong**
- **Optional ML Classifier**
  - Predicts password strength based on patterns in a dataset
  - Uses features like length, digits, uppercase letters, and special characters
  - Built with **scikit-learn Random Forest**

---

## 🚀 Usage

1. Make sure Python 3.x is installed  
2. Install required libraries:
``bash
pip install pandas numpy scikit-learn

3. Run the script:

python password_checker_full.py


4. Input a password when prompted.

5. Optional ML: Include a passwords.csv file in the project folder with the following structure:

password,label
123456,weak
password,weak
Admin123!,strong
My$ecureP@ss,strong
📌 Example Output

Without ML dataset:

=== Password Strength Checker ===
Enter password: MyPass123!
[Basic Checker] Password strength: Strong
ML dataset not found (passwords.csv). Skipping ML prediction.

With ML dataset:

=== Password Strength Checker ===
Enter password: MyPass123!
[Basic Checker] Password strength: Strong
ML model accuracy on test set: 1.0
[ML Prediction] Password strength: strong


🧠 What I Learned

Python scripting: regex, functions, user input

Cybersecurity basics: password strength principles, weak vs strong passwords

Machine Learning: feature extraction, dataset handling, training a Random Forest classifier

Project workflow: combining Python scripts with ML and user-friendly output


🔧 Tools & Technologies

Python 3.x

Libraries: pandas, numpy, scikit-learn

IDE: Visual Studio

Git & GitHub


⚡ Next Steps / Improvements

Build a GUI using Tkinter or PySimpleGUI

Train with larger password datasets for better ML accuracy

Add output logging for analysis

Integrate with network security tools ethically
