#!/bin/bash
# Script displays all the methods a server accepts
curl -sI -X -HEAD "$1" | grep -i "Allow:" | cut -d ' ' -f2-
