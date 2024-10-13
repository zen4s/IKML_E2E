import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "IKML_E2E"
AUTHOR_USER_NAME = "Subhra"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "sj_ghosh@yahoo.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/zen4s/IKML_E2E",
    project_urls={
        "Bug Tracker": f"https://github.com/zen4s/IKML_E2E/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)