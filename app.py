from aws_cdk import (
    aws_s3 as _s3,
    aws_s3_deployment as _deployment,
    aws_cloudfront as _cloudfront,
    aws_cloudfront_origins as _cloudfront_origins,
    core,
)


class Cdkcdns3Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        bucket = _s3.Bucket(
            self, '_s3-site-bucket',
            website_index_document='index.html',
            public_read_access=True,
            removal_policy=core.RemovalPolicy.DESTROY
        )
        
        deployment = _deployment.BucketDeployment(
            self, '_s3-asset',
            destination_bucket=bucket,
            sources=[_deployment.Source.asset('./static/')]
        )
        
        cloudfrontorigin = _cloudfront_origins.S3Origin(
            bucket,
        )
        
        cloudfront = _cloudfront.Distribution(
            self, 'cloudfront_dist',
            default_behavior=cloudfrontorigin
        )
        
        core.CfnOutput(self, 'Cloudfront-DomainName', value=cloudfront.distribution_domain_name)

app = core.App()
Cdkcdns3Stack(app, "cdkcdns3")

app.synth()
