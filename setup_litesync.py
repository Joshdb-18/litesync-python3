import os
import subprocess
from setuptools import setup

# Download and extract litesync
subprocess.run(["curl", "-O", "https://litesync.io/download/litesync-free-windows-x86_64.tar.gz"])
subprocess.run(["tar", "-xzvf", "litesync-free-windows-x86_64.tar.gz"])
subprocess.run(["install.bat"])

# Define setup function
def run_setup():
    setup(
        name='litesync',
        version='1.0',
        packages=['litesync'],
        package_data={'': ['*.h']},
        include_package_data=True,
        data_files=[('C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.22621.0\\ucrt', ['sqlite3.h', 'sqlite3ext.h'])],
    )

# Run setup
run_setup()
