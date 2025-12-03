#!/bin/bash
# Displays the size of the response body from a url
if [[ -z "$1" ]]; then
    echo "Usage $0 url"
    exit 1
fi

url="$1"

size=$(curl -s -w "%(size_download)" -o /dev/null "$url")
echo "$size"
