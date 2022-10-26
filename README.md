# aws-web-app-ipv4-to-binary

  

- This is a simple web app that converts an IPv4 address into its binary equivalent.

  

- Note: I did not want to hard-code the API Gateway Endpoint directly into the index.html file, so I made a separate .js file and created a variable within it to store the URL for the API Gateway Endpoint. That file name can be added to your .gitignore file to prevent it from being included in the repo. However, I have included the file (apiCallExample.js) with this repo to provide an example of how I implemented it in the working application. If you want to use this method, you will need to zip the .js file up with the index.html file before deploying it to Amplify.

  

- I used/adapted the following resources for the development of this app:

  - AWS Getting Started Resource Center - https://aws.amazon.com/getting-started/hands-on/build-web-app-s3-lambda-api-gateway-dynamodb/

  - Tiny Technical Tutorials: Architect and Build an End-to-End AWS Web Application from Scratch - https://youtu.be/7m_q1ldzw0U

## Below is an example of the web app in action:

![AWS-Web-App](https://github.com/mblackonline/aws-web-app-ipv4-to-binary/blob/f9a429333b214a9be5d093abda1a18b99de72de2/AWS-Web-App.gif)