# AWS-Cloud-Projects-Portfolio
"A collection of 4 AWS projects: EC2 Auto Scaling, AI Image Recognition, S3 Security Auditor, and Serverless Thumbnail Generator."

 ## 1.Automated Scalable Web Infrastructure
- **Objective:** Deploy a self-healing, high-availability web server.
- **Services Used:** EC2, Launch Templates, Auto Scaling Groups (ASG), VPC, Bash Scripting.
- **Key Features:** - Automated Apache installation using
- **User Data scripts**.- Configured
- **Security Groups** for HTTP (80) and SSH (22) traffic.
- **Challenges Overcome:** - Resolved
- **RDP connectivity errors** by identifying that Linux instances require SSH/Instance Connect rather than Remote Desktop.- Fixed
- **Bash script execution errors** related to shell special characters.

- ## 2. Serverless AI Image Intelligence
- **Objective:** Automatically detect objects in images uploaded to S3 and notify via email.
- **Services Used:** Amazon S3, AWS Lambda, Amazon Rekognition, Amazon SNS.
- **Key Outcome:** Created a pipeline where S3 triggers a Python Lambda function to analyze images using AI.
- **Challenges Overcome:** Resolved `InvalidS3ObjectException` by auditing S3 bucket naming and metadata permissions.

## 3. Automated S3 Security Auditor
- **Objective:** Monitor and alert on unauthorized S3 bucket creations using **EventBridge** and **SNS**.
- **Impact:** Ensures 24/7 security monitoring without manual auditing.

## 4. Serverless Thumbnail Generator
- **Objective:** Automate image processing using S3 event triggers and Lambda to save storage costs.

- ## 5. Serverless Visitor Counter 📈
- **Objective:** Build a dynamic visitor counter for a website using a serverless backend.
- **Services Used:** AWS Lambda, Amazon DynamoDB, API Gateway, S3 (Static Website Hosting).
- **How it works:** - The frontend (JavaScript) calls an **API Gateway** endpoint.
    - API Gateway triggers a **Lambda function**.
    - Lambda updates the visitor count in a **DynamoDB table** and returns the new value.
- **Key Skill:** Demonstrated "Full Stack" cloud integration by connecting a frontend UI to a NoSQL database.
-

- ### Project Screenshots
![Web Server Working](<img width="1919" height="1079" alt="Screenshot 2026-02-23 194839" src="https://github.com/user-attachments/assets/27b00f35-ae58-4d21-879a-a819315da508" />


### Project Screenshots
![S3 triggers a Python Lambda function to analyze images using AI](<img width="1919" height="1071" alt="Screenshot 2026-02-23 195448" src="https://github.com/user-attachments/assets/58f8ad20-6140-4b48-9a1d-7c4b457e0b60" />


### Project Screenshots
![AWS Security Alert](<img width="1919" height="1079" alt="Screenshot 2026-02-23 211412" src="https://github.com/user-attachments/assets/186c1eac-be6f-4868-9f71-c4f9fbd5b76e" />


