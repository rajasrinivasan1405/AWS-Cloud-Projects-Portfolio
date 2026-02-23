import boto3
import json
import urllib.parse

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
sns = boto3.client('sns')

def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    raw_key = event['Records'][0]['s3']['object']['key']
    key = urllib.parse.unquote_plus(raw_key, encoding='utf-8')
    
    print(f"Bucket: {bucket}")
    print(f"Key: {key}")

    try:
        
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=5
        )
        
        labels = [label['Name'] for label in response['Labels']]
        message = f"AI Analysis Result for {key}:\n\nI found: {', '.join(labels)}"
        
       
        sns.publish(
            TopicArn="arn:aws:sns:ap-south-1:775296258395:AI-Image--Alerts", 
            Subject="AI Image Analysis Report",
            Message=message
        )
        
        return {'statusCode': 200, 'body': 'AI Processed Successfully!'}
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': str(e)}
