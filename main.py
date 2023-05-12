import tkinter as tk


class TypingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")

        self.label = tk.Label(
            self.root, text="Start typing, if you stop after 5 seconds, your text will dissapear. Press the Save button to save the written text to a file.", wraplength=550)
        self.label.pack(pady=20)

        self.input_box = tk.Entry(self.root, width=100)
        self.input_box.focus_set()
        self.input_box.pack(padx=30)

        self.label = tk.Label(self.root, text="", wraplength=550)
        self.label.pack()

        self.save_button = tk.Button(
            self.root, text="Save!", command=self.save_text)
        self.save_button.pack()

        self.timer = None

        self.input_box.bind('<KeyPress>', self.start_timer)

        self.pass_the_event = ''

    def start_timer(self, event):
        if self.timer is not None:
            self.root.after_cancel(self.timer)
            self.fade_text(4)
            self.pass_the_event = event

        self.timer_count = 5
        self.timer = self.root.after(1000, self.update_timer)

    def update_timer(self):
        self.timer_count -= 1

        if self.timer_count > 0:
            self.timer = self.root.after(1000, self.update_timer)
            self.fade_text(self.timer_count)
        else:
            self.delete_text()

    def delete_text(self):
        self.input_box.delete(0, tk.END)
        self.label.config(text="")

    def fade_text(self, count):
        gray_colors = ['gray0', 'gray40', 'gray60', 'gray80', 'white']
        self.label.config(fg=gray_colors[count])

    def update_label(self, event):
        text = self.input_box.get()
        self.label.config(text=text)

    def save_text(self):
        text = self.input_box.get()
        with open("saved_text.txt", "w") as file:
            file.write(text)
        self.start_timer(self.pass_the_event)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = TypingApp()
    app.input_box.bind('<KeyRelease>', app.update_label)
    app.run()
