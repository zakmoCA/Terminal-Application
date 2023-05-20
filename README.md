# [My App Repo (GitHub)]()
# [My Project Management (Trello)](https://trello.com/invite/b/0EUM1gBZ/ATTIe34c9fe163d3046c50de67b75f7ade7735039F3D/t1a3)

# Table of Contents

1. [Sources](#sources)
2. [Style Guide](#style-guide)
3. [Purpose](#purpose)
4. [Target Audience](#target-audience)
5. [Implementation Plan](#implementation-plan)
    1. [Outline](#outline)
    2. [Project Management](#project-management)
    3. [Priorities and Deadlines](#priorities-and-deadlines)
6. [App Features](#app-features) 
    1. [Feature 1](#feature1)
    2. [Feature 2](#feature2)
    3. [Feature 3](#feature3)
    4. [Feature 4](#feature4)
    5. [Feature 5](#feature5)
7. [Help Documentation](#help-documentation)
    1. [Installaiton Steps](#installation-steps)
    2. [Dependencies](#dependencies)
    3. [System And Hardware Requirements](#system-and-hardware-requirements)


# Sources



# Style Guide

The style guide I will be following for this project is PEP 8.

# Purpose

# Target Audience

# Implementation Plan

## Outline

My Pomodoro applicaiton should perform the basic functions of a pomodoro timer albeit in the command line, the user should be able to:
- Enter a task name for each pomodoro
- Set work and break time durations
- Provide a timer countdown of the pomodoro work/break periods
- Give an alert when work and break periods are over

## Project Management
### Initial Outline
My Initial project outline was done on Asana but I then transitioned to Trello. Below you will see a high level overview of the key components of involved in completing the command line application and assignment. 

![Initial Outline in Asana](/docs/Day1-Asana.png)

### End of First Day
Once starting the assignment, I transitioned to Trello and developed a more granular implementation plan, complete with checklists for the appropriate items (features/tests), along with deadlines for the key deliverables. By the end of day 1, all the core functionality and testing of the application was complete, although I was yet to expand upon the core functionality to the extent I would want the finished product to have. I believed some of this would come to me as I worked on the application, and indeed feature 4 did as a result.
### Day 1 Trello Board
![Project Board end of Day 1](/docs/end-of-day-1.png)

### End of Second Day
My initial projections for deadlines were not met, as I was running a little late with some features after my second day of working on the assignment. This was somewhat expected as I was already running behind due to extenuating circumstances and I expected timelines to be dynamic as a result. However, because of the prioritisation of the key features, and having already implemented the aspects of the assignment which required greater amounts of reading/learning/cognitive overhead, this could be made up for by end of day 3.
### Day 2 Trello Board
![Project Board end of Day 2](/docs/end-of-day2.png)

### End of Third Day

### Day 3 Trello Board


## Priorities and Deadlines
In terms of deadlines and priorities, my highest priority tasks were in order;
1. Develop Implementation Plan
2. Write first feature
3. Test first feature
4. Write second and third features/tests

Doing the above things allows me to complete the core functionality of my command-line app, and meet the minimum requirements for the assignment. There would be space after which to decide if I wanted to implement further features and tests. It also involved the most technical and cognitive overhead out of all the deliverables, which is why I prioritised their completion, before the rest of the application and documentation requirements.

# App Features

## Choose Pomodoro work/break times for timer

The Pomodoro technique is a popular time management technique. It involves picking a task, and setting a 'pomodoro' timer and working on the task, the timer is traditionally for 25 minutes, followed by a 5 minute break. The end of the work and break periods are signified by a sound as is the case with timers, and pomodoro applications typically also provide alerts. My application prompts the user to enter their desired work time and break time in minutes, and then starts the timer.

## Assign Pomodoro's to specific 'tasks'

The application prompts the user to enter a 'task' for their pomodoro. This task name can then be used for statistics purposes in the data visualisation aspect of the application ie. how many pomodoros did I complete for task x this week?

## Write Pomodoro data to file

The pomodoro's task name, start time, end time, and duration are written to a CSV file, along with the respective headers.

## Alert when work/break times are over



## Data Visualisation




## Features & Checklist Items
### Feature 1: Set Work and Break Times
![Feature 1 - Set Timer](/docs/set-pomodoro-timer-plan.png)

The first feature was the timer functionality. It would involve:
- Getting user input for determining the length of the work and break times
- Displaying the timer 
- Handling exceptions

The design of this feature involved a high level overview of what processes would be needed, and then a step by step;
- User input 
- Way to display user input as a countdown timer

Step by step this would require:
1. Getting appropriate user input, by ensuring the user entered only digits
2. Converting this user input to integer type
3. Using either control flow or exception handling to ensure the program (feature) runs until appropriate input has been attained

The functionality for this feature is provided by the run_pomodoro.py and pomodoro_length.py modules, although it is executed by the start function in start_pomodoro.py. Code below.
![pomodoro_length.py]()
![run_pomodoro.py]()
![start_pomodoro.py]()

### Feature 2: Set Task
![Feature 2 - Set Task](/docs/set-task-plan.png)

The second feature allows the user to allocate the pomodoro to a 'task'. This is achieved by getting user input for the task name. 
Potential inappropriate user input is handled using a while loop:
- User is asked to enter task name
- Program exits while loop and asks user for timer settings
- If no user input is recorded the program continues running and user is told that they they must enter a task name, and prompted again

The 'task' is then appended to the 'tasks' list as a dictionary, which holds the task name (string) and pomodoro data (list of dictionaries) with the keys 'name' and 'pomodoros' respectively. If the task name entered for a pomodoro already exists in our list, the pomodoro data is appended to that task's list of 'pomodoros', else a new task dictionary is created with the current tasks name and pomodoro data.


### Feature 3: Write To CSV
![Feature 3 - Write To CSV](/docs/write-csv-plan.png)

The third feature of this application involves writing the data for each pomodoro to a CSV file, allowing this information to be stored and accessed later, or manipulated using data visualisation tools. This feature required:
- Access to the file system to check for the existence of the data file, and also create the file if it doesn't already exist
- Ability to append new data to the file, without erasing or modifying the existing data
- Handling exceptions, Python's built-in 'csv' and 'open' libraries were used to achieve this

A high level overview of the steps this would require:
1. Checking (once pomodoro finishes) if the CSV file ('pomodoros.csv') already exists in the current directory using os.path.isfile() function
2. Opening the file in append mode if it doesn't exist vs creating it if it does exist
3. If file is new, writing the headers 'Task Name', 'Start Time', 'End Time', and 'Duration'
4. Writing the pomodoro data corresponding to the above headers to the file
5. Close the file once finished 

Like other command-line programs, the user can also abort this program using 'Ctrl/Cmd' + 'C'. We still want to record the pomodoro data should this occur, so the start function which executes the application is wrapped in a try/except block, with the exception being a KeyboardInterrupt.
- When the start function first runs the user is asked to enter timer settings
- It then enters a 'try' block where the pomodoro cycle commences, continuously monitoring for a KeyboardInterrupt exception
- Should the user enter 'Ctrl/Cmd' + 'C', the program enters the 'except' block which handles our file writing before the program ends

This allows us to integrate the KeyboardInterrupt into our application by ensuring the pomodoro data is still recorded should the user want to abort the program.

### First Test: Timer Functionality
![Test 1: Timer Funcitonality](/docs/first-test.png)


### Second Test: Writing To CSV
![Test 2: File Writing](/docs/second-test.png)





## Project Management Workflow


# Help Documentation

## Installation Steps



## Dependencies



## System And Hardware Requirements
