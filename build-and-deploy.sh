#!/usr/bin/env bash
HOME_DIR="/home/brian" && \
ECZ_DIR=$(pwd) && \
RESUME_DIR="$HOME_DIR/Dropbox/resume" && \
RESUME_FILE="resume.html" && \
RESUME_FILE_PATH="$RESUME_DIR/$RESUME_FILE" && \
S3_BUCKET="s3://exitcodezero.io" && \
cd $RESUME_DIR && \
resume export $RESUME_FILE --format=html --theme=elegant && \
cd $ECZ_DIR && \
hugo -t cocoa-eh && \
cp $RESUME_FILE_PATH public/$RESUME_FILE && \
cd public && \
aws s3 sync . $S3_BUCKET --delete
