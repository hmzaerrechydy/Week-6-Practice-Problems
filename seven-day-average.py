import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)
    reader = list(reader)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


def calculate(reader): 
    states = {"Alabama": 0, "Alaska": 0, "Arizona": 0, "Arkansas": 0, "California": 0, "Colorado": 0, "Connecticut": 0, "Delaware": 0, "Florida": 0, "Georgia": 0, "Hawaii": 0, "Idaho": 0, "Illinois": 0, "Indiana": 0, "Iowa": 0, "Kansas": 0, "Kentucky": 0, "Louisiana": 0, "Maine": 0, "Maryland": 0, "Massachusetts": 0, "Michigan": 0, "Minnesota": 0, "Mississippi": 0, "Missouri": 0, "Montana": 0, "Nebraska": 0, "Nevada": 0, "New Hampshire": 0, "New Jersey": 0, "New Mexico": 0, "New York": 0, "North Carolina": 0, "North Dakota": 0, "Ohio": 0, "Oklahoma": 0, "Oregon": 0, "Pennsylvania": 0, "Rhode Island": 0, "South Carolina": 0, "South Dakota": 0, "Tennessee": 0, "Texas": 0, "Utah": 0, "Vermont": 0, "Virginia": 0, "Washington": 0, "West Virginia": 0, "Wisconsin": 0, "Wyoming": 0}
     
    for state in states: 
        cases = []
        output = [] 
        count = 0 

        for dict in reversed(reader): 
            if dict["state"] == state: 
                cases.append(int(dict['cases']))  
                count += 1 
            if count == 15:
                previous = 0
                for case in reversed(cases):
                    current = case - previous
                    output.append(current) 
                    previous = case  

                states[state] = output 
                break

    return states

def comparative_averages(new_cases, states):
    for state in states: 
        avg = 0 
        cases = new_cases[state]
        cases.reverse()

        for case in cases[0:7]:
            avg += case
        
        last_week_avg = 0 
        
        for case in cases[7:14]: 
            last_week_avg += case 
        
        last_week_avg /= 7    
        avg /= 7 

        compare = (avg - last_week_avg) / last_week_avg

        development = "" 
        if compare >= 0: 
            development = "increase"
        else:
            development = "decrease"

        print(f"{state} had a 7-day average of {int(avg)} and a {development} of {compare:.2f}%.")
        


main()
