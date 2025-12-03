#!/bin/bash
# Script displays response after sending a variable to header
curl -s -H "X-School-User-Id: 98" "$1"