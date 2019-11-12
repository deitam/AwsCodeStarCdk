import os.path

from aws_cdk import core, aws_s3, aws_s3_deployment


class DeploymentBucketStack(core.Stack):
    """
    This stack is required for the CodeStar project deployment,
    since it requires the source code and toolchain to be located in an S3 bucket.
    """
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '..', 'files')
        deployment_files = aws_s3_deployment.Source.asset(path)

        self.__bucket = aws_s3.Bucket(self, 'DeploymentBucket', access_control=aws_s3.BucketAccessControl.PUBLIC_READ)
        aws_s3_deployment.BucketDeployment(self, 'Deployment', destination_bucket=self.__bucket, sources=[deployment_files])

    def get_bucket_name(self):
        return self.__bucket.bucket_name
