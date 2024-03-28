#!/bin/bash
# Sends a DELETE request to the URL passed, and displays the body
curl -s "$1" -X DELETE
