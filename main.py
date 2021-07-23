import tkinter as tk
import random
from writing_window import WritingWindow

prompts = ["When she woke up one morning ...", "He simply couldn't think about anything else than ...", "Once upon a "
                                                                                                        "time...", "Far far away from here ..."]
random_string = random.choice(prompts)

end_timer=0

app = tk.Tk()

app.title("Time Writing Motivator")
app.config(height=850, width=900, bg="#C9D8B6")

create_window=False
end_timer=60
string=random_string

def destroy():
    app.withdraw()

def set_1min():
    button_1.config(bg = "#515E63", fg = "#ffffff")
    button_2.config(bg="#D6B0B1", fg="#000000")
    button_3.config(bg="#D6B0B1", fg="#000000")
    global end_timer
    end_timer=60

def set_2min():

    button_2.config(bg = "#515E63", fg = "#ffffff")
    button_1.config(bg="#D6B0B1", fg="#000000")
    button_3.config(bg="#D6B0B1", fg="#000000")
    global end_timer
    end_timer=120

def set_5min():
    button_3.config(bg = "#515E63", fg = "#ffffff")
    button_1.config(bg="#D6B0B1", fg="#000000")
    button_2.config(bg="#D6B0B1", fg="#000000")
    global end_timer
    end_timer=300


def prompt_accepted():
    global string
    button_prompt1.config(bg = "#515E63", fg = "#ffffff")
    button_prompt2.config(bg="#D6B0B1", fg="#000000")
    button_prompt3.config(bg="#D6B0B1", fg="#000000")
    string=string

def new_prompt():
    global string
    button_prompt2.config(bg = "#515E63", fg = "#ffffff")
    button_prompt3.config(bg="#D6B0B1", fg="#000000")
    button_prompt1.config(bg="#D6B0B1", fg="#000000")
    random_string = random.choice(prompts)
    var.set(random_string)
    string=random_string



def no_prompt():
    global string
    button_prompt3.config(bg = "#515E63", fg = "#ffffff")
    button_prompt2.config(bg="#D6B0B1", fg="#000000")
    button_prompt1.config(bg="#D6B0B1", fg="#000000")
    var.set(" ")
    string=""



def writing():
    window = WritingWindow(app, end_timer, string)
    window.user_text.insert("1.0", string)
    window.iconbitmap('icon1.ico')

app.iconbitmap('icon1.ico')


img_logo = tk.PhotoImage(file="logo.png")
label_logo = tk.Label(image=img_logo, width=660, height=150, background=("#C9D8B6"))
label_logo.config(highlightthickness=0)
label_logo.grid(column=0, row=0, columnspan=5)

intro_text = "Challenge and train yourself to come up with new stories faster.\n The Time Writing Motivator makes your text " \
             "disappear\n if you don't write anything for a few moments\n and ... you have to start from the beginning"
introduction_label = tk.Label(app, text=intro_text, pady=10, padx=20, font=("Sans Serif", 16, "normal"), bg="#C9D8B6")
introduction_label.place(relx=0.5, rely=0.5, anchor="center")
introduction_label.grid(column=0, row=1, columnspan=5)

label_logo1 = tk.Label(app, pady=20, text="How long do you want to write your story?", font=("Sans Serif", 16, "normal"),
                      background=("#C9D8B6"))
label_logo1.grid(column=0, row=2, columnspan=5)

button_1 = tk.Button(text="1 minute", padx=30, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
                           bg="#515E63", fg="#ffffff", activebackground="#515E63", activeforeground="#ffffff",
                           highlightcolor="#57837B", bd=2, command=set_1min)
button_1.focus_set()
button_1.grid(column=1, row=3)
button_2 = tk.Button(text="2 minutes", padx=30, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
                           bg="#D6B0B1", activebackground="#515E63", activeforeground="#ffffff",
                           highlightcolor="#57837B", bd=2, command=set_2min)
button_2.grid(column=2, row=3)
button_3 = tk.Button(text="5 minutes", padx=30, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
                           bg="#D6B0B1", activebackground="#515E63", activeforeground="#ffffff",
                           highlightcolor="#57837B", bd=2, command=set_5min)
button_3.grid(column=3, row=3)

label_prompt = tk.Label(text="Random prompt:", font=("Sans Serif", 16, "normal"), pady=20, background=("#C9D8B6"))
label_prompt.grid(column=2, row=4)

var=tk.StringVar()
prompt_text = tk.Label(height=1, width=50, padx=20, pady=20, bg="white", textvariable=var)
prompt_text.config(font=("Serif", 14, 'normal'), relief="flat", highlightthickness=0)
var.set(random_string)
prompt_text.grid(column=1, row=5, columnspan=3)


empty_label = tk.Label(text="\n", background="#C9D8B6")
empty_label.grid(column=1, row=6)

button_prompt1 = tk.Button(text="Accept prompt", padx=20, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
                           bg="#515E63", activebackground="#515E63", activeforeground="#ffffff",
                           highlightcolor="#57837B", bd=2, fg="#ffffff", command=prompt_accepted)
button_prompt1.focus_set()
button_prompt1.grid(column=1, row=7)
button_prompt2 = tk.Button(text="Other prompt", padx=20, pady=5,relief="raised", font=("Sans Serif", 12, "normal"),
                           bg="#D6B0B1", activebackground="#515E63", activeforeground="#ffffff",
                           highlightcolor="#57837B", bd=2, command=new_prompt)
button_prompt2.grid(column=2, row=7)
button_prompt3 = tk.Button(text="No prompt", padx=20, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
                           bg="#D6B0B1", activebackground="#515E63", activeforeground="#ffffff",
                           highlightcolor="#57837B", bd=2, command=no_prompt)
button_prompt3.grid(column=3, row=7)

empty_label2 = tk.Label(text="\n", background="#C9D8B6")
empty_label2.grid(column=1, row=8)

button_go = tk.Button(text="Start writing", bg="#8B5E83", fg="#ffffff",padx=100, pady=5, relief="raised", font=("Sans Serif", 14, "bold"), command=lambda: [destroy(), writing()])
button_go.grid(column=1, row=9, columnspan=3)

empty_label3 = tk.Label(text="\n", background="#C9D8B6")
empty_label3.grid(column=1, row=10)



app.mainloop()
