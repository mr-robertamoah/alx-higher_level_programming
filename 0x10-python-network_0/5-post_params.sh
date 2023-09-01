#!/bin/bash
# variables email and subject and their values must be sent with response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
