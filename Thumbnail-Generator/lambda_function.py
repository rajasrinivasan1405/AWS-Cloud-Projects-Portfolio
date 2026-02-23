import json
import boto3
import urllib.parse

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            source_bucket = record['s3']['bucket']['name']
       file_key = urllib.parse.unquote_plus(record['s3']['object']['key'])
             destination_bucket = "image-copy-14"
            copy_source = {
                'Bucket': source_bucket,
                'Key': file_key
            }
   s3.meta.client.copy(copy_source, destination_bucket, file_key)
            print(f"Success! Copied {file_key} from {source_bucket} to {destination_bucket}")

        return {
            'statusCode': 200,
            'body': json.dumps('Copy process completed successfully!')
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
