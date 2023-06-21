# README.md

This repository demonstrates how to use Terraform Local and LocalStack for AWS resource management in a local development environment. 

## Getting Started

### Prerequisites

- LocalStack: You can install it via Homebrew on MacOS with the following command:

```bash
brew install localstack
```

For more installation options, please refer to the [LocalStack installation guide](https://github.com/localstack/localstack#installing).

- Terraform Local: Refer to the [Terraform installation guide](https://learn.hashicorp.com/tutorials/terraform/install-cli) to set it up.

- AWS CLI Local (awslocal): Installation instructions can be found on the [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

- Python 3: Make sure Python 3 is installed on your machine. You can download it from the [official website](https://www.python.org/downloads/).

### Running the demo

1. Start LocalStack:

```bash
localstack start
```

2. Apply your Terraform configuration using the tflocal CLI:

```bash
tflocal apply
```

3. Upload a file to your S3 bucket:

```bash
awslocal s3 cp demo.txt  s3://my-bucket
```

4. List all the buckets to verify the file was uploaded:

```bash
awslocal s3 ls
```

5. Run the Python script to read the file content:

```bash
python3 app/my_app.py
```

## About

LocalStack provides an easy-to-use test/mocking framework for developing Cloud applications. It spins up a testing environment on your local machine that provides the same functionality and APIs as the real AWS cloud environment. 

This demo uses a simple Terraform configuration to create an S3 bucket and a Python script to upload a file and retrieve its content from the bucket.

For more information, visit the [LocalStack Cloud](https://localstack.cloud/).

---