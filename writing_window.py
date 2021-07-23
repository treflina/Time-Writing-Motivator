import tkinter as tk
import time
from tkinter import filedialog

class WritingWindow(tk.Toplevel):

    def __init__(self, parent,end_timer, string):
        super().__init__(parent)

        self.title("Time Writing Motivator")
        self.config(height=850, width=900, bg="#C9D8B6")

        self.img_logo = tk.PhotoImage(file="logo.png")
        self.label_logo = tk.Label(self, image=self.img_logo, width=660, height=150, background=("#C9D8B6"))
        self.label_logo.config(highlightthickness=0)
        self.label_logo.grid(column=0, row=0, columnspan=5)

        self.empty_label4 = tk.Label(self,bg="#C9D8B6")
        self.empty_label4.grid(column=0, row=1)

        self.user_text = tk.Text(self, font=("Verdana", 12, "normal"))
        self.user_text.focus_set()
        self.user_text.grid(column=1, row=1, columnspan=4)

        self.scrollbar = tk.Scrollbar(self)

        self.user_text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.user_text.yview)
        self.scrollbar.grid(column=5, row=1, sticky="ns")

        self.empty_label5 = tk.Label(self,bg="#C9D8B6", pady=15)
        self.empty_label5.grid(column=0, row=2, columnspan=5)
        self.empty_label6 = tk.Label(self,bg="#C9D8B6", padx=10)
        self.empty_label6.grid(column=6, row=1)

        # self.button_restart = tk.Button(text="1 minute", padx=30, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
        #                      bg="#515E63", fg="#ffffff", activebackground="#515E63", activeforeground="#ffffff",
        #                      highlightcolor="#57837B", bd=2, command=restart)
        # self.button_restart.focus_set()
        # self.button_restart.grid(column=1, row=3)
        self.button_save = tk.Button(self,text="Save", padx=30, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
                             bg="#ffffff", activebackground="#515E63", activeforeground="#ffffff",
                             highlightcolor="#57837B", state="disabled",bd=2, command=self.save)
        self.button_save.grid(column=2, row=3)
        self.button_exit = tk.Button(self,text="Exit", padx=30, pady=5, relief="raised", font=("Sans Serif", 12, "normal"),
                             bg="#D6B0B1", activebackground="#515E63", activeforeground="#ffffff",
                             highlightcolor="#57837B", bd=2, command=exit)
        self.button_exit.grid(column=3, row=3)

        self.empty_label7 = tk.Label(self,bg="#C9D8B6", padx=10)
        self.empty_label7.grid(column=0, row=4)

        self.end_timer=end_timer
        self.start_time=time.time()
        self.string=string
        self.bind("<KeyRelease>", self.start)


    def rgb_to_hex(self):
        print(f"r: {self.r}")
        self.r = self.r + 25
        self.g = self.g + 25
        self.b = self.b + 25
        color = f'#{self.r:02x}{self.g:02x}{self.b:02x}'
        self.user_text.config(foreground=color)

    def start(self, event):
        self.count = 0
        self.cancel_id = None
        self.r = 0
        self.g = 0
        self.b = 0
        self.text_disappear()
        self.current_time=time.time()


    def text_disappear(self):
        self.user_text.config(foreground="black")
        if self.count < 10:
            self.count += 1
            self.cancel_id = self.user_text.after(2500, self.text_disappear)
            self.rgb_to_hex()
            self.unbind("<KeyRelease>")
            self.bind("<Key>", self.stop)

        if self.count == 10:
            self.user_text.delete("1.0", "end")
            self.cancel_id = None
            self.bind("<KeyRelease>", self.start)

        elapsed_time=time.time()-self.start_time
        if elapsed_time>self.end_timer:
            self.user_text.insert("end", "\n\n                                              -----THE END-----                       ")
            self.user_text.config(state="disabled", fg="black")
            self.empty_label5.config(text='Your time is up. You can save your story.', font=("Sans Serif", 20, "normal"))
            self.user_text.after_cancel(self.cancel_id)
            self.cancel_id=None
            self.count=0
            self.button_save.config(state="normal", bg="#D6B0B1")


    def stop(self, event):
        if self.cancel_id is not None:
            self.user_text.after_cancel(self.cancel_id)
            self.cancel_id = None
            self.count = 0
            self.unbind("<Key")
            self.bind("<KeyRelease>", self.start)


    def save(self):
        data=[('txt','*.txt'), ('docx','*.docx'),('doc','*.doc')]
        f = filedialog.asksaveasfile(mode='w',filetypes=data, defaultextension=".txt", initialfile="mystory")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        story_to_save = str(self.user_text.get(1.0, "end-1c"))
        f.write(story_to_save)
        f.close()

    def exit(self):
        exit()


















