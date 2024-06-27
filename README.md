# Typing Speed Test Application

This application is a typing speed test that measures a user's 
typing speed in Characters Per Minute (CPM) and Words Per Minute (WPM). 
It consists of three main modules:

## Modules

### 1. main.py

This is the entry point of the application.

**Key Features:**
- Imports the TypingSpeedTest class from the typing_speed_test module
- Creates an instance of TypingSpeedTest
- Runs the typing speed test application

**Usage:**
```python
python main.py

### 2. result_manager.py
This module manages the calculation and display of typing speed results.
Key Features:

Calculates typing speed (CPM and WPM) Note: CPM - Characters Per Minute, WPM - Words Per Minute
Tracks the best CPM score
Displays results on the GUI

Main Class: ResultManager
Key Methods:

calculate_speed(): Calculates typing speed based on input
display_results(): Shows the results on the GUI

### 3. timer_manager.py
This module handles the timer functionality for the typing test.
Key Features:

Manages a countdown timer
Updates the GUI with remaining time
Triggers callback when time is up

Main Class: TimerManager
Key Methods:

start_timer(): Initiates the timer
update_timer(): Updates the timer every second
reset_timer(): Resets the timer for a new test

The repo contains the text file called "random_words.txt" that contains all the
words used in the app operation.
