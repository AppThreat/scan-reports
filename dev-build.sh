#!/usr/bin/env bash

while sleep 1; do
    ag -l | entr -cdrs 'pytest'
done
