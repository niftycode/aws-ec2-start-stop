#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
start_stop_ec2.py
Python 3.6
version: 1.1
author: Bodo Schonfeld
last edited: 29/07/2017
"""

import sys
import os
import argparse
import boto3.ec2
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

# Global Class Pattern
class Mem:
    # Declare globals here...
    instance_id = ""

# Read credentials from credentials.txt
def readCredentials():
    try:
        with open('credentials.txt', 'r') as f:
            credentials = [line.strip() for line in f]
            return credentials
    except FileNotFoundError:
        return None

# Evaluate the arguments
def evaluate(args):
    operation = args.o
    if operation == "start":
        start_ec2()
    elif operation == "stop":
        stop_ec2()
    else:
        print("")
        print("You can >start< or >stop< your EC2 instance.")
        print("")

# Start the instance
def start_ec2():
    # This code is from Amazon's EC2 example
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[Mem.instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[Mem.instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

# Stop the instance
def stop_ec2():
    # This code is from Amazon's EC2 example
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[Mem.instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances witout dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[Mem.instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

# Parse input arguments (start / stop)
def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--o', type=str, default="nothing",
                        help='You can >start< or >stop< your EC2 instance.')
    args = parser.parse_args()
    sys.stdout.write(str(evaluate(args)))

def main():
    credentials = readCredentials()
    Mem.instance_id = credentials[0]
    parseArguments()
    print("")

if __name__ == '__main__':
    main()
