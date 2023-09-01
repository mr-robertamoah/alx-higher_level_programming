#!/bin/bash
# A header variable X-School-User-Id must be sent with the value 98
curl -s -H "X-School-User-Id: 98" "${1}"
