#!/bin/bash

LAST=$(git describe --abbrev=0)
NEXT=$((LAST+1))

echo "Previous version: ${LAST}"
echo "New version:      ${NEXT}"

echo "Creating tag..."
echo "git tag -a ${NEXT} -m \"Version ${NEXT}\""

echo "Pushing tag..."
echo "git push origin ${NEXT}"
