#!/usr/bin/env python3

from aws_cdk import core

from static_website_aws_cdk.static_website_aws_cdk_stack import StaticWebsiteAwsCdkStack


app = core.App()
StaticWebsiteAwsCdkStack(app, "static-website-aws-cdk")

app.synth()
