import subprocess
import os

def run_adb_command(command):
    """Executes an ADB command and returns its output"""
    try:
        result = subprocess.run(
            ['adb'] + command.split(),
            capture_output=True, # stdout, stderr captured
            text=True, # stdout, stderr are openend in text mode using encoding
            check=True # process exits with non zero exit code, CalledProcessError exception
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing ADB command: {e}")
        print(f"Stderr: {e.stderr}")
        return None

def install_apk(apk_path):
    """Insatall an APK on the connected device."""
    print(f"Installing {apk_path}...")
    output = run_adb_command(f"install (apk_path}")
    if output and "Success" in output:
        print("APK installed successfully.")
        return True
    else:
        print("APK installation failed.")
        return False


def launch_app(package_name, activity_name):
    """Launches an app on the device"""
    print(f"Launching {package_name} / {activity_name} ...")
    output = run_adb_command(f"shell am start -n {package_name}/{activity_name}")
    if output and "Error" not in output:
        print("App launched successfully.")
        return True
    else:
        print("App launch failed.")
        return False

def pull_logs(device_path, host_path):
    """Pull a file (logs) from the device to the host."""
    print(f"Pulling {device_path} to {host_path}...")
    output = run_adb_command(f"pull {device_path} {host_patah}")
    if output and "pulled" in output:
        print("File pulled successfully.")
        return True
    else:
        print("File pull failed.")
        return False

if __name__ == "__main__":
    apk_to_install = "path/to/your/app.apk"
    app_package = "com.example.your_app"
    app_activity = "com.example.your_app.MainActivity"
    device_log_path = "/sdcard/Android/data/com.example.your_app/files/logs.txt"
    host_log_path = "app_logs.txt"
    
    if install_apk(apk_to_install):
        if launch_app(app_package, app_activity):
            print("App is running. Performing tests...")
            # simulate some test actions
            if pull_logs(device_log_path, host_log_path):
                print(f"Logs saved to {host_log_path}")
            else:
                print("Failed to retrieve logs.")
        else:
            print("Could not launch the app.")
    else:
        print("Could not install the APK.")
        print(
