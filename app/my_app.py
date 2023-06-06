import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a session using any valid AWS credentials
session = boto3.Session(
    aws_access_key_id='test',  # replace with your access key
    aws_secret_access_key='test',  # replace with your secret access key
    region_name='us-east-1'  # replace with your LocalStack region
)

# Create an S3 client pointing to the LocalStack endpoint
s3 = session.client(
    service_name='s3',
    endpoint_url='http://localhost:4566'
)

def read_s3_file(bucket, file_key):
    try:
        # Use the S3 client to get the object
        s3_object = s3.get_object(Bucket=bucket, Key=file_key)
        # Read the file content
        file_content = s3_object['Body'].read().decode('utf-8')

        return file_content

    except Exception as e:
        logging.error(f"Failed to read file {file_key} from S3 bucket {bucket}.")
        logging.error(e)
        return None

def main():
    bucket = 'my-bucket'
    file_key = 'demo.txt'
    file_content = read_s3_file(bucket, file_key)

    if file_content is not None:
        # Log the content of the file
        logging.info(f"Content of {file_key}:\n{file_content}")

if __name__ == "__main__":
    main()

