## Deploy static website to AWS S3 and CloudFront with AWS CDK (Python)

A standard S3 bucket is created to store the static files stored in a folder (/static). The bucket is marked as private and is accessed via a CloudFront distribution.

#### How to run the example

1. Install the required dependencies

   `$ pip install -r requirements.txt`

2. Synthesize (cdk synth) and/or deploy (cdk deploy)

   `$ cdk deploy`
