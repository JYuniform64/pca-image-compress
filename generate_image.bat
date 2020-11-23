@echo off
del image\*.png /q /f /s
FOR /L %%a IN (1,1,%2) DO python compress.py %1 -n %%a -s png -q