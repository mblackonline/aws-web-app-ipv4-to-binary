# import the JSON utility package
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('IPv4ConverterDB')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

# extract the ipv4 address as a string from the Lambda service's event object
    ipv4addr = (event["ipv4"])
    
    ipv4_split = ipv4addr.split('.')  # This creates a comma separated list of the 4 octets saved as strings
    binary = []  # This creates an empty list to store the binary conversions

    # Use a for loop to iterate through the "ipv4_split" list and convert each octet into binary
    for octet in ipv4_split:
        binary.append(''.join(f'{int(octet):08b}'))  # creates a comma separated list of the binary converted numbers

    # For the sake of clarity, I created the below variables to store each converted octet
    octet1 = binary[0]
    octet2 = binary[1]
    octet3 = binary[2]
    octet4 = binary[3]

    final = f"The binary equivalent of {ipv4addr} is: {octet1}.{octet2}.{octet3}.{octet4}"

# write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': (final),
            'LatestGreetingTime':now
            })

# return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps(final)
    }