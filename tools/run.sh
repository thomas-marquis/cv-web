#!/bin/bash

set -e

docker run --rm -p "8501:8501" $1/${2:-cv-web}