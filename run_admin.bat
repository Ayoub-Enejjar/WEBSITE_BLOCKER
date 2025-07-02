@echo off
:: Run the app with admin privileges
powershell -Command "Start-Process cmd -ArgumentList '/c python app.py' -Verb RunAs"
:: Wait for the app to start
