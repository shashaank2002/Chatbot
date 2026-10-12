import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

messages = [
    "hello",
    "hi",
    "hey",

    "what is your name",
    "your name",
    "tell me your name",
]

intents = [
    "greeting",
    "greeting",
    "greeting",

    "name",
    "name",
    "name",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(messages)

model = LogisticRegression()
model.fit(X,intents)

def send_message():
    user_message = user_input.get()

    if user_message.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_message + "\n")

    user_message_vector = vectorizer.transform([user_message])

    prediction = model.predict(user_message_vector)
    intent = prediction[0]

    if intent == "greeting":
        reply = "Hello! How are you?"
    elif intent == "name":
        reply = "My name is AI Chatbot."

    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")

window = tk.Tk()
window.title("AI Chatbot")
window.geometry("500x500")

title = tk.Label(window, text="AI Chatbot",font=("Arial",20))
title.pack(pady=20)

chat_area = tk.Text(window, width=20,height=20)
chat_area.pack(pady=10)

user_input = tk.Entry(window, width=40)
user_input.pack(pady=10)

send_button = tk.Button(window,text="Send", command=send_message)
send_button.pack(pady=10)

window.mainloop()