#!/usr/bin/env python3

from aws_cdk import core

from static_website_aws_cdk.static_website_aws_cdk_stack import StaticWebsiteAwsCdkStack
from static_website_aws_cdk.aws_certificate_manager_stack import AWSCertificateManagerStack

app = core.App()
AWSCertificateManagerStack(app, "static-website-cert", env=core.Environment(region="us-east-1"))
StaticWebsiteAwsCdkStack(app, "static-website-aws-cdk", env=core.Environment(region="us-east-1"))

app.synth()
