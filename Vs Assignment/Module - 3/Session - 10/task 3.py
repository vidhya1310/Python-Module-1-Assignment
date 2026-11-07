
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

# Store index and score
state = {
    "index": 0,
    "score": 0
}

# Heading
heading = tk.Label(
    root, text="INDIAN GEOGRAPHY QUIZ",
    font=("Arial", 16, "bold")
)
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Question Label
question_label = tk.Label(root, text="", font=("Arial", 12))
question_label.grid(row=1, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Score Label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 11))
score_label.grid(row=5, column=0, columnspan=2, pady=5)

option_buttons = []

# Check answer
def check(option):
    if option == questions[state["index"]]["answer"]:
        result_label.config(text="Correct!", fg="green")
        state["score"] += 1
        score_label.config(text=f"Score: {state['score']}")
    else:
        result_label.config(text="Wrong!", fg="red")

    for button in option_buttons:
        button.config(state="disabled")

# Load question
def load_question():
    index = state["index"]

    question_label.config(text=questions[index]["question"])

    for i, option in enumerate(questions[index]["options"]):
        option_buttons[i].config(
            text=option,
            state="normal",
            command=lambda option=option: check(option)
        )

    result_label.config(text="")
    score_label.config(text=f"Score: {state['score']}")

# Create option buttons
for i in range(4):
    button = tk.Button(root, text="", width=20)
    button.grid(
        row=2 + i // 2,
        column=i % 2,
        padx=10,
        pady=5
    )
    option_buttons.append(button)

# Next button function
def next_question():
    if state["index"] < 4:
        state["index"] += 1
        load_question()
    else:
        question_label.config(text="All questions completed!")

# Next Button
next_button = tk.Button(
    root, text="Next", width=15,
    command=next_question
)
next_button.grid(row=6, column=0, columnspan=2, pady=10)

load_question()

root.mainloop()
