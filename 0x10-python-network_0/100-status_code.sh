#!/usr/bin/env bash
# Display the status of the response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
