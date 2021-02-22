# Autofill Google Form

import requests
import datetime
import time
import sys

# URL to the form you want to fill. formResponse should be used instead of viewform
url = 'https://docs.google.com/forms/d/e/1FAIpQLSex4USg0XegW7hpBce_mr8sicNvoxiLxND9QDDPYXVWWo9a1w/formResponse'


def get_values():
    """It returns a list of different form data to be submitted by send_attendance method.
    subjects_time is a dictionary with Day as keys and time and subjects in a list as values.
    value_list is a list of lectures' subject and time of current_day."""
	
    values_list = []

    values_list.append({
  	# Email Address
        "emailAddress": str(sys.argv[1]),
        "entry.947480993": "aaa",
        "entry.1512509175": "Option 2",
        "entry.996134388": "test2",
    })

    #values_list.append(values)

    return values_list


def send_attendance(url, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    for d in data:
        try:
            requests.post(url, data=d)
            print("Form Submitted.")
            time.sleep(10)
        except:
            print("Error Occured!")


final_data = get_values()

send_attendance(url, final_data)
