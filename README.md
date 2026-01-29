Image Analysis Using AWS Rekognition
-> Project Overview

This project implements an end-to-end image recognition system using AWS cloud services. Users upload
images, which are securely stored and analyzed using Amazon Rekognition to automatically detect
objects, scenes, and labels. The results are then displayed to the user.

The system is designed to be secure, scalable, and serverless, leveraging AWS-managed services.

->Technologies Used

1.Amazon S3 – Image storage
2.Amazon Rekognition – Image analysis and label detection
3.AWS IAM – Authentication and access control
4.AWS CLI – Service access and management
5.Python – Backend processing and API calls

-> Workflow

1.User uploads an image to the application
2.Image is stored securely in Amazon S3
3.IAM manages authentication and access permissions
4.Python script accesses AWS services using AWS CLI
5.Image is retrieved from S3 for processing
6.Amazon Rekognition analyzes the image
7.Detected labels and metadata are generated
8.Results are displayed on the output screen
