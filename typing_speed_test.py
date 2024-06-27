import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import messagebox  # Import the messagebox module from tkinter for pop-up messages
import random  # Import the random module for generating random words
from result_manager import ResultManager  # Import the ResultManager class from result_manager module
from timer_manager import TimerManager  # Import the TimerManager class from timer_manager module


class TypingSpeedTest:
    def __init__(self):
        # Initialize the main application window
        self.window = tk.Tk()
        self.window.title("Typing Speed Test")  # Set the title of the window
        self.window.geometry("800x500")  # Set the size of the window

        # Load the words from the text file
        with open("random_words.txt", "r") as file:
            self.words_list = file.read().splitlines()  # Read the words into a list

        self.user_input = tk.StringVar()  # Create a StringVar to hold the user's input
        self.words_per_set = 20  # Number of words to display in each set

        self.result_manager = ResultManager(self.window)  # Initialize the ResultManager
        self.timer_manager = TimerManager(self.window, 60)  # Initialize the TimerManager with a 60-second timer

        self.create_widgets()  # Call the method to create GUI widgets
        self.popup_shown = False  # Flag to track if the popup has been shown

    def create_widgets(self):
        # Create the top frame to hold labels and restart button
        self.top_frame = tk.Frame(self.window, padx=20, pady=10)
        self.top_frame.pack(fill="x")

        # Label to display current best CPM, corrected CPM, WPM, and time left
        self.top_label = tk.Label(self.top_frame, text=f"Your best: 0 CPM, Corrected CPM: 0, WPM: 0, Time left: 60")
        self.top_label.pack(side="left")

        # Button to restart the test
        self.restart_button = tk.Button(self.top_frame, text="Restart", command=self.restart_test)
        self.restart_button.pack(side="right")

        # Frame to display the words to type
        self.words_frame = tk.Frame(self.window, bg="white", padx=20, pady=20)
        self.words_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Generate and display the sample text
        self.sample_text = " ".join(self.generate_sample_text())
        self.text_widget = tk.Text(self.words_frame, bg="white", font=("Helvetica", 18), wrap="word", spacing1=10, padx=10, pady=10, height=5, width=80)
        self.text_widget.pack(padx=10, pady=10)
        self.text_widget.insert("1.0", self.sample_text)
        self.text_widget.config(state=tk.DISABLED)  # Make the text widget read-only

        # Label to prompt the user to type the words
        self.prompt_label = tk.Label(self.window, text="Type the words in the box below:", font=("Helvetica", 14))
        self.prompt_label.pack(pady=10)

        # Entry widget for user input
        self.entry = tk.Entry(self.window, textvariable=self.user_input, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)  # Bind key press event to start the timer
        self.entry.bind("<Return>", self.check_input)  # Bind return key event to check input

        # Label to display the results
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack(pady=10)

        # Labels to display current CPM and WPM
        self.cpm_label = tk.Label(self.top_frame, text="CPM: 0")
        self.cpm_label.pack(side="left")

        self.wpm_label = tk.Label(self.top_frame, text="WPM: 0")
        self.wpm_label.pack(side="left")

    def start_timer(self, event):
        # Start the timer when the user starts typing
        self.timer_manager.start_timer(self.top_label, self.result_manager, self.timer_callback)

    def timer_callback(self):
        # Callback function when the timer ends
        self.result_manager.calculate_speed(self.timer_manager.start_time, self.timer_manager.end_time, self.user_input.get())
        self.result_manager.display_results(self.result_label)
        self.show_popup()

    def check_input(self, event):
        # Check the user input when they press return
        if event.keysym == "Return":
            typed_words = self.user_input.get().strip().split()  # Split the input into words
            expected_words = self.sample_text.split()  # Split the sample text into words

            if typed_words == expected_words:
                # If the typed words match the sample text, load the next set of words
                self.load_next_set()
            else:
                # If the words don't match, end the timer and calculate the speed
                self.timer_manager.end_time = self.timer_manager.time.time()
                self.result_manager.calculate_speed(self.timer_manager.start_time, self.timer_manager.end_time, self.user_input.get())
                self.result_manager.display_results(self.result_label)
        # Update the CPM and WPM labels with the current values
        self.cpm_label.config(text=f"CPM: {int(float(self.result_manager.corrected_cpm.get()))}")
        self.wpm_label.config(text=f"WPM: {int(float(self.result_manager.wpm.get()))}")

    def show_popup(self):
        # Show a popup when the time is up
        if not self.popup_shown:
            self.popup_shown = True
            self.popup = tk.Toplevel(self.window)
            self.popup.title("Time's up!")
            self.popup.geometry("300x100")
            tk.Label(self.popup, text="60 seconds are up. Check your results.").pack(pady=20)

    def restart_test(self):
        # Restart the test and reset all values
        if self.popup_shown:
            self.popup.destroy()  # Close the popup if it was shown
            self.popup_shown = False

        self.sample_text = " ".join(self.generate_sample_text())  # Generate new sample text
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", self.sample_text)
        self.text_widget.config(state=tk.DISABLED)
        self.result_label.config(text="")
        self.user_input.set("")
        self.entry.delete(0, tk.END)
        self.timer_manager.reset_timer()  # Reset the timer
        self.update_labels()

    def generate_sample_text(self):
        # Generate a set of random words from the words list
        random.shuffle(self.words_list)
        return self.words_list[:self.words_per_set]

    def load_next_set(self):
        # Load the next set of words to type
        self.sample_text = " ".join(self.generate_sample_text())
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", self.sample_text)
        self.text_widget.config(state=tk.DISABLED)
        self.user_input.set("")
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def update_labels(self):
        # Update the top label with the current best CPM, corrected CPM, WPM, and time left
        self.top_label.config(
            text=f"Your best: {int(self.result_manager.best_cpm)} CPM, Corrected CPM: {self.result_manager.corrected_cpm.get()}, "
                 f"WPM: {self.result_manager.wpm.get()}, Time left: {self.timer_manager.time_limit}")

    def run(self):
        # Run the main application loop
        self.window.mainloop()


# Initialize and run the Typing Speed Test
typing_test = TypingSpeedTest()
typing_test.run()
