from aws_cdk import (
    core,
    aws_certificatemanager as aws_cm,
    aws_ssm as ssm,
)

class AWSCertificateManagerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        cert = aws_cm.Certificate(self, "StaticWebsiteCert", domain_name="static.deepgorthi.com", validation_method=aws_cm.ValidationMethod.DNS)

        ssm.StringParameter(self, "CertificateARNParameter", parameter_name="cert-arn", string_value=cert.certificate_arn)