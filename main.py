import subprocess
import sys
import pkg_resources

with open('requirements.txt', 'r') as f:
    packages = f.readlines()

for package in packages:
    try:
        pkg_resources.require(package.strip())
    except pkg_resources.DistributionNotFound:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package.strip()])

from customer import *