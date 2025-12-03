#!/bin/bash
# Script displays all the methods a server accepts
curl -sI -X -OPTIONS "$1" | grep -oiE "Allow|Public":.* | cut -d ' ' -f2-
