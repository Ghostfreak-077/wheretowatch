#!/bin/bash

while getopts ":t:h" opt; do
  case $opt in
    h)
      echo "Usage: $0 [-title title_of_the_movie] [-h for help]"
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    t)
      title=$OPTARG
      ;;
  esac
done

shift $((OPTIND - 1))

API_URL="http://localhost:5001"

response=$(curl $API_URL/search/?title=$title)

echo $response