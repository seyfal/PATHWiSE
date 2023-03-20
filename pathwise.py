# openai.organization = "org-tUKmFHP7000FSOLkMus2M2B3"

import openai
import tkinter as tk
from tkinter import ttk

openai.api_key = "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"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def on_submit():
    prompt = user_input.get()
    response = generate_text(prompt)
    response_label.config(text=response)

root = tk.Tk()
root.title("OpenAI Python App")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

user_input = tk.StringVar()
input_label = ttk.Label(frame, text="Enter your input:")
input_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
input_entry = ttk.Entry(frame, textvariable=user_input, width=40)
input_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=1, column=1, sticky=(tk.W, tk.E))

response_label = ttk.Label(frame, text="", wraplength=300)
response_label.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))

root.mainloop()
