#!/bin/bash
ip a show wlp7s0 | awk 'NR==7{printf "%s",$2}' | cut -d "/" -f1
