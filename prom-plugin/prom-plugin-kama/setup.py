import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="kama-sdk-py",
  version="0.0.1",
  author="NMachine",
  author_email="xavier@nmachine.io",
  description="Prometheus plugin for KAMA",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/nectar-cs/kama-sdk-py",
  packages=setuptools.find_packages(exclude=[]),
  package_data={
    'prom_kaml': [
      'assets/*.*',
      'model/**/yamls/**'
    ]
  },
  include_package_data=True,
  install_requires=[
    'kama-sdk-py',
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.8'
)
