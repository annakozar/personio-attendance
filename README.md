To create an AWS Lambda function that goes to Personio and fills in the working hours from 8:00 till 17:00 with a break from 12:00-13:00 and runs as a cron job every day at 8:00, you can follow these steps:

First, you'll need to create an AWS Lambda function. Go to the AWS Management Console and select Lambda from the list of services.

Click on the Create function button and choose Author from scratch. Give your function a name and select the runtime as Python.

In the Function code section, you'll need to past the code from personio.py that will interact with the Personio API to fill in the working hours. 

Replace 'YOUR_API_KEY' with your actual Personio API key. You can find your API key in your Personio account under Settings > API Credentials.

[getting started with the personio api](https://developer.personio.de/docs/getting-started-with-the-personio-api)

Test your code by clicking on the Test button in the top right corner of the Lambda console. You can use a test event with an empty JSON object.

Once your code is working correctly, you can set up a cron job to run your Lambda function every day at 8:00. To do this, go to the CloudWatch service in the AWS Management Console.

Click on the Rules option in the left-hand menu and then click on the Create rule button.

In the Create Rule page, configure the following settings:

Event Source: Schedule
Cron expression: 0 8 * * ? *
Target: Lambda function
Function: Choose your Lambda function from the dropdown menu
Click on the Create button to save your cron job.
Your Lambda function will now run every day at 8:00 and fill in the working hours in Personio from 8:00 till 17:00 with a break from 12:00-13:00.