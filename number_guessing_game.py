import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.master.geometry("400x300")
        self.master.configure(bg="#2E4053")  # Background color
        
        # Game settings
        self.random_number = random.randint(1, 100)  # Random number between 1 and 100
        self.attempts = 10
        
        # Title label with color
        self.title_label = tk.Label(master, text="Guess the Number!", font=("Helvetica", 18, "bold"), fg="#F4D03F", bg="#2E4053")
        self.title_label.pack(pady=10)
        
        # Instructions label with color
        self.instructions_label = tk.Label(master, text="Guess a number between 1 and 100:", font=("Helvetica", 12), fg="#D5DBDB", bg="#2E4053")
        self.instructions_label.pack(pady=5)
        
        # Entry field for user input
        self.entry = tk.Entry(master, font=("Helvetica", 14), bg="#1C2833", fg="#F4D03F", insertbackground="#F4D03F")
        self.entry.pack(pady=5)
        
        # Submit button with styles
        self.submit_button = tk.Button(master, text="Submit Guess", font=("Helvetica", 12, "bold"), bg="#1ABC9C", fg="white", command=self.check_guess)
        self.submit_button.pack(pady=10)
        
        # Attempts label with color (showing attempts)
        self.attempts_label = tk.Label(master, text=f"Attempts left: {self.attempts}", font=("Helvetica", 12), fg="#F4D03F", bg="#2E4053")
        self.attempts_label.pack(pady=5)
        
        # Welcome message on the next line
        self.welcome_label = tk.Label(master, text="Welcome to Rn's Guessing Number Game!", font=("Helvetica", 12), fg="#F4D03F", bg="#2E4053")
        self.welcome_label.pack(pady=5)
        
        # Result message label
        self.result_label = tk.Label(master, text="", font=("Helvetica", 12), fg="#EC7063", bg="#2E4053")
        self.result_label.pack(pady=10)
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100!")
                return
            
            self.attempts -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")
            
            if guess < self.random_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.random_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text="Congratulations! You guessed it!")
                self.end_game()
            
            if self.attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you're out of attempts. The number was {self.random_number}.")
                self.end_game()
                
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
    
    def end_game(self):
        self.entry.config(state="disabled")
        self.submit_button.config(state="disabled")

# Running the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
