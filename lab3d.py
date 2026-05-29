#!/usr/bin/env python3

import subprocess

def free_space():

    process = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        shell=True,
        stdout=subprocess.PIPE
    )

    stdout, stderr = process.communicate()

    return stdout.decode('utf-8').strip()
