#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98

curl -s -H "X-HolbertonSchool-User-Id: 98" "${1}"
