import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="static_website_aws_cdk",
    version="0.0.1",

    description="CDK Python app for AWS S3 Static Website",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "static_website_aws_cdk"},
    packages=setuptools.find_packages(where="static_website_aws_cdk"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-s3",
        "aws-cdk.aws-certificatemanager",
        "aws-cdk.aws-ssm",
        "aws-cdk.aws-cloudfront",
        "aws-cdk.custom-resources"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
