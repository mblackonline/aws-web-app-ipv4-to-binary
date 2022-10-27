# aws-web-app-ipv4-to-binary

  

- This is a simple web app that converts an IPv4 address from decimal into binary.

- I used/adapted the following resources for the development of this app:

  - AWS Getting Started Resource Center - https://aws.amazon.com/getting-started/hands-on/build-web-app-s3-lambda-api-gateway-dynamodb/

  - Tiny Technical Tutorials: Architect and Build an End-to-End AWS Web Application from Scratch - https://youtu.be/7m_q1ldzw0U

- I decided to complete this project to gain some hands-on experience with implementing AWS serverless solutions. I enjoyed experimenting with the code in Lambda and I gained a better understanding of how to implement Python within the Lambda function. 
  
- **Note**: I did not want to hard-code the API Gateway endpoint directly into the index.html file, so I made a separate .js file and created a variable within it to store the URL for the API Gateway endpoint. That file name can be added to the .gitignore file to prevent the file from being included in the GitHub repo. However, I have included the file (named apiCallExample.js) with this repo to provide an example of how I implemented it in the working application. If you want to use this method, you will need to zip the .js file up with the index.html file before deploying it to Amplify.

### The web application architecture uses the following AWS resources:  
- <a href="https://aws.amazon.com/amplify/console/">AWS Amplify Console</a>. 
- <a href="https://aws.amazon.com/api-gateway/">Amazon API Gateway</a>
- <a href="https://aws.amazon.com/lambda/">AWS Lambda</a>
- <a href="https://aws.amazon.com/iam/">AWS Identity and Access Management (IAM)</a>
- <a href="https://aws.amazon.com/dynamodb/">Amazon DynamoDB</a>

### Below is an example of the web app in action:

![AWS-Web-App](https://github.com/mblackonline/aws-web-app-ipv4-to-binary/blob/f9a429333b214a9be5d093abda1a18b99de72de2/AWS-Web-App.gif)