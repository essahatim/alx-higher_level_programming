#!/bin/bash
# Takes a URL as argument and displays all HTTP methods accepted by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
