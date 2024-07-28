import json
import boto3
import email
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')



def lambda_handler(event, context):
    for record in event['Records']:
        # Extract necessary information from the event
        print(event['Records'])
        ses_message = json.loads(record['body'])
        message_id = ses_message['mail']['messageId']
        receipt = ses_message['receipt']
        
        # Retrieve email content from S3
        bucket_name = 'bank-tim-atkins-co-za'
        object_key = f'{message_id}.eml'
        email_obj = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        email_data = email_obj['Body'].read()

        # Parse email content
        msg = email.message_from_bytes(email_data)
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            # Extract attachment
            attachment_data = part.get_payload(decode=True)
            attachment_name = part.get_filename()

            # Save the attachment to S3
            try:
                s3_client.put_object(Bucket=bucket_name, Key=f'attachments/{attachment_name}', Body=attachment_data)
            except ClientError as e:
                print(f"Error saving attachment '{attachment_name}' to S3: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Attachment extraction successful!')
    }