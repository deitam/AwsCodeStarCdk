import os.path

from aws_cdk import core, aws_s3, aws_s3_deployment


class MyBucketStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '..', 'files')
        source1 = aws_s3_deployment.Source.asset(path)

        bucket = aws_s3.Bucket(self, 'MyBucket', access_control=aws_s3.BucketAccessControl.PUBLIC_READ)
        self._bucket_name = bucket.bucket_name
        files = aws_s3_deployment.BucketDeployment(self, 'MyDeployment', destination_bucket=bucket, sources=[source1])

    def get_bucket_name(self):
        return self._bucket_name
