#! /bin/bash

# define variables
# OR leave empty for single connected device
DEVICE_SERIAL="emulator-5554"
TEST_SCRIPT="nw_test.py"
REPORT_DIR="test_reports"

# Ensure ADB is available
# if adb is not found
if ! command -v adb &> /dev/null
then 
    echo "ADB not found. Please ensure Android SDK Platorm-Tools are installed and in your PATH."
    exit 1
fi

# connect to device (if specific device is provided)
# a unary conditional operator, returns True (exit status 0) if the following string is NOT empty
if [ -n "$DEVICE_SERIAL" ]; then
    echo "Connecting to device: $DEVICE_SERIAL"
    # || logical OR operator. Right command will only execute if left command fails
    adb connect "$DEVICE_SERIAL" || { echo "Failed to connect to device."; exit 1; }# exit 1: error
fi

# create report directory
mkdir -p "$REPORT_DIR"

echo "Running Android tests..."
# > redirect operator. Send stdout to a file
# 2>&1: std shell redirection trick
# 2: stderr file descriptor
# > redirect
# &1: stdout file descriptor (was already redirected to test_output.log)
# 0: stdin file descriptor
# &: specific syntax for duplicating or merging file descriptors during redirection. "Do not treat this number as a filename; treat it as a reference to an already open I/O stream" 
python "$Test_SCRIPT" > "$REPORT_DIR/test_output.log" 2>&1

# $?: shell parameter that hold exit status (return code) of recently executed foreground command
# 0: exit status, successfuly completed w/o errors
if [ $? -eq 0 ]; then
    echo "Tests completed successfully. See $REPORT_DIR/test_output.log for details."
else
    echo "Tests failed. Check $REPORT_DIR/test_output.log for errors."
fi

# disconnect from device
# shell variable: "$DEVICE_SERIAL"
adg disconnect "$DEVICE_SERIAL"
