from aws_cdk import core, aws_iam
from aws_cdk.custom_resources import AwsCustomResource
from aws_codestar_cdk.cdk_stack.attributes import Attributes


class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, atts: Attributes) -> None:
        super().__init__(scope, id)

        policy = aws_iam.PolicyStatement(
            actions=[
                "iam:PassRole",
                "codestar:CreateProject",
                "codestar:UpdateProject",
                "codestar:DeleteProject",
                "s3:GetObject"
            ]
        )
        policy.add_all_resources()

        project_name = atts.project_name
        code_bucket_key = 'source.zip'
        toolchain_bucket_key = 'toolchain.yml'
        bucket_name = atts.bucket_name
        subnet_ids = atts.subnet_ids
        security_group_ids = atts.security_group_ids

        project = AwsCustomResource(self, "CreateProject",
                                    on_create={
                                        "service": "CodeStar",
                                        "action": "createProject",
                                        "parameters": {
                                            'id': project_name,
                                            'name': project_name,
                                            'sourceCode': [
                                                {
                                                    'destination': {
                                                        'codeCommit': {
                                                            'name': project_name
                                                        },
                                                    },
                                                    'source': {
                                                        's3': {
                                                            'bucketKey': code_bucket_key,
                                                            'bucketName': bucket_name
                                                        }
                                                    }
                                                },
                                            ],
                                            'toolchain': {
                                                'source': {
                                                    's3': {
                                                        'bucketKey': toolchain_bucket_key,
                                                        'bucketName': bucket_name
                                                    }
                                                },
                                                'roleArn': 'arn:aws:iam::770536902058:role/service-role/aws-codestar-service-role',
                                                'stackParameters': {
                                                    "ProjectId": project_name,
                                                    "MySubnetIds": subnet_ids,
                                                    "MySecurityGroupIds": security_group_ids
                                                }
                                            }
                                        },
                                        "physicalResourceId": '123'
                                    },
                                    on_update={
                                        "service": "CodeStar",
                                        "action": "updateProject",
                                        "parameters": {
                                            'id': project_name,
                                            "description": "dummy description",
                                        },
                                        "physicalResourceId": '123'
                                    },
                                    on_delete={
                                        "service": "CodeStar",
                                        "action": "deleteProject",
                                        "parameters": {
                                            'id': project_name,
                                            "deleteStack": True,
                                        },
                                        "physicalResourceId": '123'
                                    },
                                    policy_statements=[policy]
                                    )
