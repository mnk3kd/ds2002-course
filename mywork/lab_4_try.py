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

#Here is URL here, too: Presigned URL: https://ds2002-mnk3kd.s3.amazonaws.com/kelp.jpeg?AWSAccessKeyId=ASIA5FTZEJ2LDOE77V5M&Signature=Z2Ph%2FKz2Mk%2BT3JwGSVrqjECAri8%3D&x-amz-security-token=FwoGZXIvYXdzEEoaDFS0z3GUPFwe7NvWmiLEAbHTKSc2uUUP%2F0BlPmh1V8DTtogilTy1SJ%2BQ6Nq9lv9JzNmSdJ8d4GA6AhmTeVQPR12WyLCCQy8LBOB%2FsfXhIHEWeDvk9riX7eCyaiSwssopp%2BYQGNTmgmzleYiClT%2F7Hq6U9zsrBoR4gT27gVd%2Bu3EHxYchn1WnTQQEiO%2FUwqdiQNcEMPNPgn2sPhGzAIYD%2Flq1V4Uv8KAd%2FwoUHvxfLOPOUZ1X9NNYjMD8YoBnXhT0we1phn7c%2B3tXAepnW4IZvodCBJQo7734rwYyLajz%2Fj%2FgMpI4xFaaHhrdv5b0mBsqz7M4XHms7c4EIK3p%2B6%2FxNjtQpNqT3VjMHA%3D%3D&Expires=1711758082
