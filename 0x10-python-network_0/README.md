# Python Networking

## Introduction

This folder is an interaction with the `curl` command used for manipulating urls.

- Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
    - The size must be displayed in bytes
    - Used `curl`

- Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
    - Display only body of a 200 status code response
    - Used `curl`

- Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
    - Used `curl`

- Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
    - A header variable `X-School-User-Id` must be sent with the value `98`
    - Used `curl`