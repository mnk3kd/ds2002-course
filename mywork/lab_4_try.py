#!/usr/bin/python3


import boto3
import requests

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            print("Image downloaded successfully.")
    else:
        print("Failed to download image.")

# Initialize S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# Download image
download_image('https://news.virginia.edu/sites/default/files/article_image/kelp_forest_douglas_klug_photo_lgdr.jpeg', 'kelp.jpeg')

# Define S3 bucket and local file
bucket_name = 'ds2002-mnk3kd'
local_file = 'kelp.jpeg'

# Upload image to S3
with open(local_file, 'rb') as f:
    s3.upload_fileobj(f, bucket_name, local_file, ExtraArgs={'ACL': 'public-read'})

# Generate presigned URL
object_name = 'kelp.jpeg'
expires_in = 604800

presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print("Presigned URL:", presigned_url)

#I have no idea why the importing requests is not working - couold be an issue with my python, as I have that package installed. The rest of the script should be correct.

