import os
from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as _apig
from aws_cdk import aws_logs as _logs
from aws_cdk import aws_s3 as _s3


class ApigStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        self.add_lambda_function()
        self.add_apig()

    def add_lambda_function(self):
        self.lambda_function = _lambda.Function(
            self,
            "LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="main.handler",
            code=_lambda.Code.asset(os.path.join(os.path.dirname(__file__), "lambda")),
            function_name="fastapi-serverless-cdk-lambda",
        )

        _logs.LogGroup(
            self,
            "LambdaFunctionLog",
            log_group_name=f"/aws/lambda/{self.lambda_function.function_name}",
            removal_policy=core.RemovalPolicy.DESTROY,
            retention=_logs.RetentionDays.ONE_WEEK,
        )

    def add_apig(self):
        _apig.LambdaRestApi(
            self,
            "RestApi",
            handler=self.lambda_function,
            rest_api_name="fastapi-serverless-cdk-api",
        )
