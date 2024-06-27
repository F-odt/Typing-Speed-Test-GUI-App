# Import the time module for time-related functions
import time
# Import the tkinter module and alias it as tk
import tkinter as tk


# Define the TimerManager class
class TimerManager:
    # Initialize the TimerManager object
    def __init__(self, window, time_limit):
        self.window = window  # Store the main window object
        self.time_limit = time_limit  # Set the time limit for the timer
        self.time_left = tk.StringVar()  # Create a StringVar to store and update time left
        self.timer_started = False  # Flag to check if timer has started
        self.start_time = None  # Variable to store start time
        self.end_time = None  # Variable to store end time
        self.top_label = None  # Reference to the top label in the GUI
        self.result_manager = None  # Reference to the ResultManager object
        self.callback = None  # Callback function to be called when timer ends

    # Method to start the timer
    def start_timer(self, top_label, result_manager, callback):
        if not self.timer_started:
            self.start_time = time.time()  # Set the start time
            self.timer_started = True  # Set timer started flag to True
            self.top_label = top_label  # Store reference to top label
            self.result_manager = result_manager  # Store reference to ResultManager
            self.callback = callback  # Store the callback function
            self.update_timer()  # Start updating the timer

    # Method to update the timer
    def update_timer(self):
        elapsed_time = time.time() - self.start_time  # Calculate elapsed time
        time_remaining = self.time_limit - elapsed_time  # Calculate remaining time
        self.time_left.set(f"Time left: {int(time_remaining)}s")  # Update time left StringVar

        if time_remaining > 0:
            # Update the top label with current stats
            self.top_label.config(
                text=f"Your best: {int(self.result_manager.best_cpm)} CPM, Corrected CPM: {self.result_manager.corrected_cpm.get()}, "
                     f"WPM: {self.result_manager.wpm.get()}, {self.time_left.get()}")
            # Schedule next update in 1000ms (1 second)
            self.window.after(1000, self.update_timer)
        else:
            self.end_time = time.time()  # Set the end time
            self.callback()  # Call the callback function when time is up

    # Method to reset the timer
    def reset_timer(self):
        self.timer_started = False  # Reset timer started flag
        self.time_limit = 60  # Reset time limit to 60 seconds
        self.top_label = None  # Clear top label reference
        self.result_manager = None  # Clear ResultManager reference
        self.callback = None  # Clear callback function reference
