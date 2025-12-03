#!/bin/bash
# Script sends a GET to a server and displays repsonse
curl -s -L -w "%{http_code}" "$1" -o response_body > status_code; cat response_body
