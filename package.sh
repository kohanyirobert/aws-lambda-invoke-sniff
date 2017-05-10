#! /bin/sh
rm -vf package-*.zip
zip -r package-$(basename $(pwd))-$(cat VERSION).zip VERSION handler.py
