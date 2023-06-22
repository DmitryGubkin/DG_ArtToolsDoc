import os
import sys
import subprocess

modulesList = ['mkdocs', 'mkdocs-material', 'mkdocs-awesome-pages-plugin', 'mkdocs-video']

for m in modulesList:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', m])
os.system("pause")