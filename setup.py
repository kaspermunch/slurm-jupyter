import setuptools, os, sys

# if sys.platform == 'win32':
#     # make an .exe file beside the actual script
#     os.environ['SETUPTOOLS_LAUNCHER'] = "executable"

setuptools.setup(
    name="slurm_jupyter",
    version="1.0",
    author="Kasper Munch",
    author_email="kaspermunch@birc.au.dk",
    description="Utility running jupyter on a slurm cluster.",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaspermunch/slurm_jupyter",
    packages=setuptools.find_packages(),
    scripts=['slurm-jupyter.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# python3 setup.py sdist bdist_wheel