import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="appthreat-scan-reports",
    version="1.0.1",
    author="Team AppThreat",
    author_email="cloud@appthreat.com",
    description="Library for producing gorgeous html reports from AppThreat scan results. Compatible with SARIF and grafeas format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/appthreat/scan-reports",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["Jinja2"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
        "Topic :: Security",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
