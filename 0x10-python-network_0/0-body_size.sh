#!/bin/bash
# Displays the size of the response body from a url
curl -s -w "%{size_download}" -o /dev/null "$1"
