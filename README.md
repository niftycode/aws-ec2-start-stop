# aws-ec2-start-stop

## About

Start your Amazon Web Services EC2 Instance with Python 3.

## Requirements

### Python Modules

If you never used [Amazon Web Services](https://aws.amazon.com/) with Python before, you have to install two additional modules:

    pip install boto3 botocore

or

    pip3 install boto3 botocore

### EC2 Instance ID

Enter your EC2 ID in the *credentials.txt* file. Check your EC2 dashboard for the available IDs.

### AWS Credentials

Save your **AWS Credentials** in your home/users folder:

Linux:

    /home/[username]/.aws

macOS:

    /Users/[username]/.aws

Windows:

    /Users/[username]/.aws

For more information about the content of the *.aws* folder check the AWS documentation: [Configuration and Credential Files](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html).

Instead of creating the *.aws* folder manually you can use the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html):

* [Installer for Windows](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html#install-msi-on-windows)
* [Installer for Linux, macOS, UNIX](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-bundle.html)

After you've installed the AWS CLI open the PowerShell (Windows) or a Shell (UNIX-like systems) and enter:

    aws configure

## Changelog

Empty for now, but this might change in the future.
