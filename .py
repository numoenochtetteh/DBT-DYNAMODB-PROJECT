# to start the project you need to install and configure AWS CLI (AMAZON WEB SERVICES COMMAND LINE INTERFACE)
# To confirm the installation, use the 
aws --version #command at a command prompt 

#REASON FOR AWS Command Line Interface
#The AWS CLI allows you to interact with AWS services (like DynamoDB, S3, or EC2) directly from your terminal
#Configuring the CLI links your local machine to your AWS account. It ensures that your credentials (like Access Key ID and Secret Access Key) are properly set up to authenticate your action

#After that create your access key and secret key in IAM to help you interact with AWS in AWS CLI
#Open a terminal on your local machine and enter
aws configure. #Enter the access key and secret access key and  Choose a default region name

#Loading data to DynamoDB table from a .csv file can only be done using python
# Import necessary libraries
import boto3  # This library lets us connect and interact with AWS services like DynamoDB
import csv    # This library helps us read data from CSV files

# Connect to DynamoDB service in AWS (use the appropriate region)
dynamodb = boto3.resource('dynamodb', 'us-east-1')  # This line connects us to DynamoDB in the "us-east-1" region

# Function to write data to DynamoDB in batches (faster way to insert multiple items)
def batch_write(table_name, rows):
    table = dynamodb.Table(table_name)  # We choose the DynamoDB table where we want to save the data

    with table.batch_writer() as batch:  # This starts the batch writing process (in bulk)
        for row in rows:  # For each row (or record) in the list of data
            batch.put_item(Item=row)  # This adds the row to the DynamoDB table

    return True  # If everything worked, we return True to show it's successful

# Function to read data from a CSV file and convert it into a list of dictionaries
def read_csv(csv_file, list):
    rows = csv.DictReader(open(csv_file, encoding="utf8"))  # This opens the CSV file and reads it row by row

    for row in rows:  # For each row in the CSV file
        list.append(row)  # Add the row as a dictionary to the list (this is our data to insert into DynamoDB)

# Main program starts here
if __name__ == '__main__':
    table_name = 'USINDSSP2020'  # Name of the DynamoDB table where we want to save the data
    file_name = 'USINDSSP2020.csv'  # The CSV file that has the data we want to upload

    items = []  # Create an empty list where we will store the data from the CSV file

    # Read the data from the CSV file
    read_csv(file_name, items)

    # Upload the data to DynamoDB using the batch_write function
    status = batch_write(table_name, items)

    # If the upload was successful, print "Data is saved", else print an error message
    if(status):
        print('Data is saved')  # Success message
    else:
        print('Error while loading data...')  # Error message









