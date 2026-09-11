#!/bin/bash

URL="https://qvmsmbng2blemd57npzaobceju0behjp.lambda-url.eu-west-1.on.aws/"

# Require a question as the first argument
if [ -z "$1" ]; then
  echo "Usage: ./query.sh \"your question here\""
  exit 1
fi

QUESTION="$1"

PAYLOAD=$(jq -n --arg q "$QUESTION" '{query: $q}')

RESPONSE=$(curl -s -X POST "$URL" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

# Print just the answer text, cleanly
echo "$RESPONSE" | jq -r '.response'