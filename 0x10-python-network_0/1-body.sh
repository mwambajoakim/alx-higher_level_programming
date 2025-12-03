#!/bin/bash
# Script sends a GET to a server and displays responses for 200 status code
curl -s -L -w "%{http_code}" "$1" -o response_body > status_code; cat response_body
