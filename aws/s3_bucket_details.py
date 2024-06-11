"""bucket_info.py"""

import boto3

def list_s3_buckets_with_regions():
    """List buckets and regions."""
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # List all buckets
    buckets = s3_client.list_buckets()
    data = {}

    # Print bucket names and their regions
    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']

        # Get the bucket location
        location = s3_client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']

        # For buckets in us-east-1, LocationConstraint will be None
        if location is None:
            location = 'us-east-1'
        data[bucket_name] = {
            # "name": bucket_name,
            "location": location
        }
    return data
if __name__ == "__main__":
    buckets = list_s3_buckets_with_regions()
    for bkt, deets in buckets.items():
        print(f"{bkt} => {deets['location']}")
