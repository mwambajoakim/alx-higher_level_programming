#!/bin/bash
# Scipt sends a DELETE request to url and displays the response
curl -s --request "DELETE" "$1" -o response_body; cat response_body
