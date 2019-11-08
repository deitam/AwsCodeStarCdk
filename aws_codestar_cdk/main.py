from aws_codestar_cdk.cdk_stack.stack import MyStack
from aws_codestar_cdk.cdk_stack.attributes import Attributes
from aws_codestar_cdk.cdk_stack.bucket_stack import MyBucketStack
from typing import List
from aws_cdk import core


class Main:

    def __init__(self, scope: core.Construct, project_name: str, subnet_ids: List[str], security_group_ids: List[str]):
        bucket_stack = MyBucketStack(scope, '{}-bucket-stack'.format(project_name))
        attributes = Attributes(project_name, bucket_stack.get_bucket_name(), subnet_ids, security_group_ids)
        stack_name = '{}-stack'.format(project_name)
        self._stack = MyStack(scope, stack_name, attributes)
        self._stack.add_dependency(bucket_stack)

    def get_stack(self):
        return self._stack
