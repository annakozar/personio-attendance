import requests

def lambda_handler(event, context):
    # Your Personio API key
    api_key = 'YOUR_API_KEY'

    # The URL for the Personio API endpoint to fill in the working hours
    url = 'https://api.personio.de/v1/timeslots'

    # The working hours and break time
    start_time = '08:00:00'
    end_time = '17:00:00'
    break_start_time = '12:00:00'
    break_end_time = '13:00:00'

    # Create the JSON payload to send to the Personio API
    payload = {
        "start_time": start_time,
        "end_time": end_time,
        "break_start_time": break_start_time,
        "break_end_time": break_end_time
    }

    # Add the API key to the headers
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    # Send the request to the Personio API
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code
    if response.status_code == 200:
        print('Working hours filled successfully')
    else:
        print('Error filling working hours')