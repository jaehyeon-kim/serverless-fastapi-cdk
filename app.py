#!/usr/bin/env python3

from aws_cdk import core

from resources.apig_stack import ApigStack


app = core.App()

ApigStack(app, "serverless-fastapi-cdk")

app.synth()
