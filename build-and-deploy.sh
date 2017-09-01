#!/usr/bin/env bash
hugo && \
cp /home/brian/Dropbox/resume/resume.html public/resume.html && \
cd public && \
aws s3 sync . s3://exitcodezero.io
