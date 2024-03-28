#!/bin/bash
# Sends a request to the URL, and displays the bytes size.
curl -s "$1" | wc -c
