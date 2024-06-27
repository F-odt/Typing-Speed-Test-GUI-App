# Import the tkinter module and alias it as tk
import tkinter as tk


# Define the ResultManager class
class ResultManager:
    # Initialize the ResultManager object
    def __init__(self, window):
        # Store the main window object
        self.window = window
        # Initialize the best characters per minute (CPM) score
        self.best_cpm = 0
        # Create StringVar objects to store and update results
        self.corrected_cpm = tk.StringVar()  # Corrected CPM
        self.wpm = tk.StringVar()  # Words Per Minute
        self.speed = tk.StringVar()  # Overall speed score

    # Calculate typing speed based on input
    def calculate_speed(self, start_time, end_time, input_text):
        # Calculate the total time taken
        elapsed_time = end_time - start_time
        # Count the number of characters typed
        num_chars = len(input_text)
        # Calculate characters per minute
        cpm = num_chars / elapsed_time * 60
        # Set the corrected CPM
        self.corrected_cpm.set(f"{int(cpm)}")
        # Calculate words per minute (assuming 5 characters per word)
        wpm = num_chars / 5 / elapsed_time * 60
        # Set the WPM
        self.wpm.set(f"{int(wpm)}")
        # Set the overall speed score
        self.speed.set(f"Your score: {int(cpm)} CPM (that is {int(wpm)} WPM)")
        # Update the best CPM if the current score is higher
        if cpm > self.best_cpm:
            self.best_cpm = cpm

    # Display the results on the GUI
    def display_results(self, result_label):
        # Get the current WPM score
        wpm = int(self.wpm.get())
        # Check if the WPM is 40 or higher (considered good)
        if wpm >= 40:
            # Display a congratulatory message
            result_label.config(text=f"Congratulations! Your typing speed is {wpm} WPM, which beats the target!")
        else:
            # Display an encouraging message
            result_label.config(text=f"Your typing speed is {wpm} WPM. Keep practicing to improve your speed!")
