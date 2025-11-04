#! /bin/bash

# Ensure ADB is available
# /dev/null is a special filesystem object that discards everything written into it.
# check if the executable "adb" is available in the system's PATH and can be executed.
# command -v adb: locate adb executable.
# if it finds adb executable, it normally prints path to executable and exits with success stat
# exit code 0. if it doesn't find, prints nothing (err msg to stderr) and exit failure nonzero
if ! command -v adb $> /dev/null
# &> /dev/null: redirection that discards both stdout(>) and stderr(&) by sending to 
# /dev/null (black hole of operating systems. ensuring command produces no visible output)
then
    echo "ADB not found. Please ensure Android SDK Platform-Tools are installed"
    exit 1
fi

# check for connected devices
# count # of connected and recognized android devices attached to the compute
# | grep "devices$": takes output of adb devices and passes it to grep command
# | wc - l: passes output from grepp to wc command, count # of lines in its input
DEVICE_COUNT=$(adb devices | grep "device$" | wc -l)
if [ "$DEVICE_COUNT" -eq 0 ]; then
    echo "No Android devices found. Please connect devices or start emulators"
    exit 1
elif [ "$DEVICE_COUNT" -gt 1 ]; then
    echo "Multiple devices found. Please specify a device using 'adb -s <device_id>' or disconnect others."
    exit 1
fi

echo "Starting Android device testing..."

# run the python script
python3 android_test.py

echo "Testing complete. Cleaning up..."
# uninstall after testing
adb uninstall com.example.your_app

