
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Indian Geography Quiz")
root.geometry("450x350")

# Store 5 questions
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "2. Which is the longest river in India?",
        "options": ["Yamuna", "Ganga", "Narmada", "Godavari"],
        "answer": "Ganga"
    },
    {
        "question": "3. Which is the highest mountain peak in India?",
        "options": ["Nanda Devi", "Kanchenjunga", "Anamudi", "Everest"],
        "answer": "Kanchenjunga"
    },
    {
        "question": "4. Which is the largest Indian state by area?",
        "options": ["Gujarat", "Rajasthan", "Maharashtra", "Punjab"],
        "answer": "Rajasthan"
    },
    {
        "question": "5. Which ocean is south of India?",
        "options": ["Pacific", "Indian", "Atlantic", "Arctic"],
        "answer": "Indian"
    }
]

# Heading Label
heading = tk.Label(
    root,
    text="INDIAN GEOGRAPHY QUIZ",
    font=("Arial", 16, "bold")
)
heading.grid(row=0, column=0, columnspan=2, pady=20)

# First question Label
question_label = tk.Label(
    root,
    text=questions[0]["question"],
    font=("Arial", 12)
)
question_label.grid(row=1, column=0, columnspan=2, pady=20)

# Run window
root.mainloop()
