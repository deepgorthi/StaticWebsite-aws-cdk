from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_cloudfront as cf,
    custom_resources as cr
)

class StaticWebsiteAwsCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "static-website", access_control=s3.BucketAccessControl.PUBLIC_READ, website_index_document="index.html")
        bucket.grant_public_access()

        parameter = cr.AwsCustomResource(self,"GetCertArn", on_update=cr.AwsSdkCall(service="SSM",action="getParameter",parameters={"Name": "cert-arn"}, region="us-east-1", physical_resource_id=str(time.time)))

        cf.CloudFrontWebDistribution(self, "CDN", price_class=cf.PriceClass.PRICE_CLASS_100, alias_configuration=cf.AliasConfiguration(names=["static.deepgorthi.com"],acm_cert_ref=parameter.get_data_string("Parameter.Value"),ssl_method=cf.SSLMethod.SNI,security_policy=cf.SecurityPolicyProtocol.TLS_V1_1_2016),origin_configs=[cf.SourceConfiguration(behaviors=[cf.Behavior(is_default_behavior=True)],s3_origin_source=cf.S3OriginConfig(s3_bucket_source=bucket))])