# nw_test.py

import subprocess
import time

def install_app(apk_path):
    print(f"Installing {apk_path}...")
    subprocess.run(["adb", "install", apk_path], check=True)
    print("App installed successfully.")

def launch_app(package_name, activity_name):
    print(f"Launching {package_name} / {activity_name}...")
    subprocess.run(["adb", "shell", "am", "start", "-n", f"{package_name}/{activity_name}"], check=True)
    print("App launched.")

def run_simple_test():
    package = "com.example.myapp"
    activity = "com.example.myapp.MainActivity"
    apk = "path/to/your/app.apk"
    
    try:
        install_app(apk)
        launch_app(package, activity)
        time.sleep(5) #simulate interaction
        print("Simple test passed")
    except subprocess.CalledProcessError as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    run_simple_test()
