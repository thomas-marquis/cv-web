#!/bin/bash

docker build -t $1/${2:-cv-web} .
