from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in contract/__init__.py
from contract import __version__ as version

setup(
	name="contract",
	version=version,
	description="trilogy",
	author="ezzat",
	author_email="E.Azab@trilogy.com.sa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
