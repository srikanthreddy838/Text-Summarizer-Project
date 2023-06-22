import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME ='End to End Text Summarization'
AUTHOR_USER_NAME='Srikanth'
SRC_REPO='textSummarizer'
AUTHOR_EMAIL='singamsrikanthreddy196@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    packages=setuptools.find_packages(where='src')
)