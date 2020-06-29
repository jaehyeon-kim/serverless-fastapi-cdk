#!/usr/bin/env python3

from aws_cdk import core

from serverless_fastapi_cdk.serverless_fastapi_cdk_stack import ServerlessFastapiCdkStack


app = core.App()
ServerlessFastapiCdkStack(app, "serverless-fastapi-cdk")

app.synth()
