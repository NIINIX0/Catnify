import os, subprocess, shutil, time

shutil.rmtree("build")
time.sleep(1)
os.makedirs("build"); os.chdir("build")
subprocess.run(["cmake", ".."])
subprocess.run(["make"])
