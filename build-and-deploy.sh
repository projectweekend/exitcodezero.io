#!/usr/bin/env bash
hugo
cd public
aws s3 sync . s3://exitcodezero.io
