import boto3

# cmlproject?region=us-east-1
class S3:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id="ASIAUPVRYDAMF6THIUHE",
            aws_secret_access_key="Hi/pubqsXF9IsFtubqYCs2jrYdJ4Q0Rt9syUrEE0",
            region_name="us-east-1",
        )
        # self.bucket = s3.Bucket("cmlproject")

    def get_list(self):
        for bucket_object in self.s3_client.list_buckets():
            print(bucket_object["Name"])


s3_instance = S3()
s3_instance.get_list()
