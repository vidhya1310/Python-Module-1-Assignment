
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Indian Geography Quiz")
root.geometry("450x350")
root.resizable(False, False)

# Store questions
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

# Store quiz state
state = {
    "index": 0,
    "score": 0
}

# Heading Label
heading = tk.Label(
    root,
    text="INDIAN GEOGRAPHY QUIZ",
    font=("Arial", 16, "bold")
)
heading.grid(row=0, column=0, columnspan=2, pady=12)

# Question Label
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    wraplength=420
)
question_label.grid(row=1, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold")
)
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Score Label
score_label = tk.Label(
    root,
    text="Score: 0/5",
    font=("Arial", 11, "bold")
)
score_label.grid(row=5, column=0, columnspan=2, pady=5)

# Check answer function
def check(option):
    if option == questions[state["index"]]["answer"]:
        result_label.config(text="Correct!", fg="green")
        state["score"] += 1
    else:
        result_label.config(text="Wrong!", fg="red")

    score_label.config(text=f"Score: {state['score']}/5")

    # Disable buttons after one answer
    for button in option_buttons:
        button.config(state="disabled")

# Load question function
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
    score_label.config(text=f"Score: {state['score']}/5")

# Create 4 option buttons
option_buttons = []

for i in range(4):
    button = tk.Button(
        root,
        text="",
        width=20,
        font=("Arial", 10)
    )

    button.grid(
        row=2 + i // 2,
        column=i % 2,
        padx=8,
        pady=5
    )

    option_buttons.append(button)

# Show final result
def show_result():
    question_label.config(text="Quiz Completed!")

    # Hide option buttons
    for button in option_buttons:
        button.grid_remove()

    next_button.grid_remove()

    # Display final score
    result_label.config(
        text=f"Your score: {state['score']}/5",
        fg="blue",
        font=("Arial", 16, "bold")
    )

    restart_button.grid(
        row=6, column=0, columnspan=2, pady=15
    )

# Next question function
def next_question():
    if state["index"] < 4:
        state["index"] += 1
        load_question()
    else:
        show_result()

# Next Button
next_button = tk.Button(
    root,
    text="Next",
    width=15,
    command=next_question
)
next_button.grid(row=6, column=0, columnspan=2, pady=10)

# Restart function
def restart_quiz():
    state["index"] = 0
    state["score"] = 0

    restart_button.grid_remove()

    # Show option buttons again
    for button in option_buttons:
        button.grid()

    next_button.grid(
        row=6, column=0, columnspan=2, pady=10
    )

    load_question()

# Restart Button
restart_button = tk.Button(
    root,
    text="Restart Quiz",
    width=15,
    command=restart_quiz
)

# Load first question
load_question()

# Run application
root.mainloop()
