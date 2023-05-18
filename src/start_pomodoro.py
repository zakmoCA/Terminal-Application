import pomodoro_length
import datetime
import run_pomodoro
import csv
import os


pomodoros = []
tasks = []


def start():
    try:
        task_name = input('Enter the name of the task this pomodoro is for: ')
        work_time, break_time = pomodoro_length.pomodoro_length()  # my pomodoro as defined by pomodoro_length()

        pomodoro = {
            'start_time': datetime.datetime.now(),
            'end_time': datetime.datetime.now() + datetime.timedelta(minutes=work_time),
            'duration': work_time,
            'task': task_name,
        }
        pomodoros.append(pomodoro)

        # Check if the task already exists
        task_exists = False
        for task in tasks:
            if task['name'] == task_name:
                task['pomodoros'].append(pomodoro)
                task_exists = True
                break

        # If the task doesn't exist, create a new one
        if not task_exists:
            task = {
                'name': task_name,
                'pomodoros': [pomodoro],
            }
            tasks.append(task)
        
        # WRITING TO CSV
        headers = ['Task Name', 'Start Time', 'End Time', 'Duration']

        # Check if the CSV file already exists
        file_exists = os.path.isfile('pomodoros.csv')

        # Now, write the pomodoro to a CSV file
        with open('pomodoros.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            
            # Write headers only if the file doesn't exist yet
            if not file_exists:
                writer.writerow(headers)
            
            # Else write the pomodoro data
            writer.writerow([task_name, pomodoro['start_time'], pomodoro['end_time'], pomodoro['duration']])

        # Now start the timer
        run_pomodoro.run_pomodoro(work_time, break_time)

        
    
    except KeyboardInterrupt:
        print("\nInterrupted. Writing current pomodoro to file...")
        # Now, write the pomodoro to a CSV file
        headers = ['Task Name', 'Start Time', 'End Time', 'Duration']

        # Check if the CSV file already exists
        file_exists = os.path.isfile('pomodoros.csv')

        # Now, write the pomodoro to a CSV file
        with open('pomodoros.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            
            # Write headers only if the file doesn't exist yet
            if not file_exists:
                writer.writerow(headers)
            
            # Else write the pomodoro data
            writer.writerow([task_name, pomodoro['start_time'], pomodoro['end_time'], pomodoro['duration']])
        
        

