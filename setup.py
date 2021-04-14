from setuptools import setup, find_packages

setup(name="snakemake_utils",
      version="0.0.1",
      author="erjel",
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      )