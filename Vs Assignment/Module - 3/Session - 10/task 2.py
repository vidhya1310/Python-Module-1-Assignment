
import tkinter as tk

root = tk.Tk()
root.title("Indian Geography Quiz")
root.geometry("450x350")

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

# Heading
heading = tk.Label(
    root, text="INDIAN GEOGRAPHY QUIZ",
    font=("Arial", 16, "bold")
)
heading.grid(row=0, column=0, columnspan=2, pady=15)

# Question
question_label = tk.Label(
    root, text=questions[0]["question"],
    font=("Arial", 12)
)
question_label.grid(row=1, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(
    root, text="", font=("Arial", 12, "bold")
)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Check answer function
def check(option):
    if option == questions[0]["answer"]:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Wrong!", fg="red")

# Create 4 option Buttons
option_buttons = []

for i, option in enumerate(questions[0]["options"]):
    button = tk.Button(
        root,
        text=option,
        width=20,
        command=lambda option=option: check(option)
    )

    button.grid(
        row=2 + i // 2,
        column=i % 2,
        padx=10,
        pady=5
    )

    option_buttons.append(button)

root.mainloop()
