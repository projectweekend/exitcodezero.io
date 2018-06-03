+++
title = 'Put Operations on Encrypted S3 Buckets'
date = 2018-05-27
draft = false
tags = ["s3", "aws", "encryption"]
description = "A lesson learned while troubleshooting puts to an encrypted S3 bucket."
+++
Any put operation on an encrypted S3 bucket will fail unless you specify options related to Server Side Encryption. Unfortunately, omitting these options does not result in a message pointing you to the cause of your failure. If you receive denial of access errors, and have already ruled out IAM permissions as the culprit, check out the SSE options.

Here is some helpful documentation for the CLI and Boto3:

* https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html - Note all of the options that begin with `sse`. In the simplest case, all you need to do is set `--sse` to the correct value for your encryption choice.
* http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.put_object - Note all of the parameters that begin with `SSE` and the one named `ServerSideEncryption`. In the simplest case, all you need to do is set `ServerSideEncryption` to the correct value for your encryption choice.
