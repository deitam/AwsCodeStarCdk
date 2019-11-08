## AWS CodeStar CDK
A package used to deploy a lambda function into AWS CodeStar via CDK.

### How to use
Install the package by pip using 
```pip install aws-codestar-cdk```
Afterwards, import the main file into your project and call the Main classes constructor.
The arguments for the constructor are the scope, your project name, list of subnet IDs where the function should be deployed and list of security group IDs for the function.
It should look something like this:
```from aws_cdk import core
from aws_codestar_cdk.main import Main

app = core.App()

main = Main(app, 'project-name', ['subnet-1', 'subnet-2'], ['sg-1', 'sg-2'])

app.synth()
```
