import os
import boto3
from botocore.exceptions import NoCredentialsError

# AWS S3 Configuration
BUCKET_NAME = "symptom-checker-raw-data"  # Your bucket name
FOLDER_PATH = "data/raw/"  # Path to the raw data folder

# Use IAM Role for Authentication (no need for access keys if properly configured)
s3 = boto3.client("s3")

def upload_files_to_s3(folder_path, bucket_name):
    """Upload all files from a folder to an S3 bucket."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_file_path, folder_path)  # Key in S3
            try:
                print(f"Uploading {local_file_path} to s3://{bucket_name}/{s3_key}")
                s3.upload_file(local_file_path, bucket_name, s3_key)
                print(f"Uploaded {file} successfully.")
            except NoCredentialsError:
                print("IAM Role or credentials not available.")

# Run the upload
if __name__ == "__main__":
    upload_files_to_s3(FOLDER_PATH, BUCKET_NAME)
