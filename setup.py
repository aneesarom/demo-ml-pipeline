from setuptools import setup, find_packages

setup(name = "census income",
      version = "0.0.1",
      author = "anees_aro",
      author_email = "anees@g.com",
      packages = find_packages(),
      install_requires = ["pandas", "numpy", "flask"]
)