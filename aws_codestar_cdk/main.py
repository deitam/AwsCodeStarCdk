from aws_codestar_cdk.cdk_stack.stack import CodeStarStack
from aws_codestar_cdk.cdk_stack.parameters import CodeStarLambdaParameters
from aws_codestar_cdk.cdk_stack.bucket_stack import DeploymentBucketStack
from typing import List, Optional
from aws_cdk import core


class LambdaCodeStar:

    def __init__(self, scope: core.Construct, project_name: str, subnet_ids: List[str], security_group_ids: List[str], event_type: str = 'None', cron_expression: Optional[str] = None):
        bucket_stack = DeploymentBucketStack(scope, '{}-bucket-stack'.format(project_name))
        parameters = CodeStarLambdaParameters(project_name, bucket_stack.get_bucket_name(), subnet_ids, security_group_ids, event_type, cron_expression)
        self.__stack = CodeStarStack(scope, '{}-stack'.format(project_name), parameters)
        self.__stack.add_dependency(bucket_stack)

    def get_stack(self):
        return self.__stack
