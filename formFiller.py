# formFiller.py - Automatically fills in the Google Form.

import pyautogui, webbrowser, time

# Open Google Form
webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSeMKGambgeWtXVKbRJl0gn-b81dhBX8TTn1O_lcQwrQmXzpWw/viewform?usp=header")

# Wait for the form to load
time.sleep(3)

# Form data (Update with your actual values)
formData = [
    {'id':'1','email': 'mani@gmail.com', 'name': 'Manish', 'college': 'NMAMT, Nitte University', 'team': 'Controller', 'role': 'SWE Intern'},
]

pyautogui.PAUSE = 1.0  # Increase pause time for more reliable operation

for i, person in enumerate(formData):
    print(f"Filling form for {person['name']} (Record {i+1}/{len(formData)})...")
    
    # If this is not the first record, click "Submit another response"
    if i > 0:
        print("Clicking 'Submit another response'...")
        # Coordinates for "Submit another response" button - adjust these for your screen
        pyautogui.click(490, 1070)  
        time.sleep(3)  # Wait for the form to reload
    
    # First, click anywhere in the form to ensure it's active
    pyautogui.click(600, 400)
    time.sleep(1)
    
    # Now fill each field and use tab to navigate
    
    # Fill ID
    pyautogui.typewrite(person['id'])
    pyautogui.press('tab')
    
    # Fill Email
    pyautogui.typewrite(person['email'])
    pyautogui.press('tab') 
    
    # Fill Name
    pyautogui.typewrite(person['name'])
    pyautogui.press('tab')
    
    # Fill College
    pyautogui.typewrite(person['college'])
    pyautogui.press('tab')
    
    # Fill Team
    pyautogui.typewrite(person['team'])
    pyautogui.press('tab')
    
    # Fill Role
    pyautogui.typewrite(person['role'])
    
    # Submit Form (uses tab to get to the submit button, then presses enter)
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    print(f"Form submitted for {person['name']}.")
    
    # Wait for the submission confirmation page to load
    time.sleep(5)
    
    # If this is the last record, we're done
    if i == len(formData) - 1:
        print("Last record processed. Ending script.")
        break

print("Form filling completed. Processed", len(formData), "records.")