#!/bin/bash

gunicorn -w 1 -b 127.0.0.1:8888 shangmen:app --daemon 
