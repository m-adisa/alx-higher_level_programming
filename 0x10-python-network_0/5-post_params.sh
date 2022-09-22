#!/bin/bash
# Display the body after sent a header variable and GET request
curl -s -X POST -L "$1" -d 'email=test@gmail.com&subject=I will always be here for PLD'
