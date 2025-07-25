import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auditory_cortex",
    version="1.0",
    author="Bilal Ahmed",
    author_email="ahmedb@purdue.edu",
    description="Deep neural networks as models of the auditory cortex using ECoG data in PyTorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bilalhsp/deep-auditory-spikes",
    packages=setuptools.find_packages(),
    package_data={
        'auditory_cortex': ['config.yml']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'importlib', 'numpy', 'scipy',
        'matplotlib', 'pandas', 'omegaconf', 
        'memory-profiler',
        'sentencepiece', 'transformers',
        'cupy', 'seaborn', 'plotly', 'naplib', 'scikit-learn',
        'torch>=2.0', 'torchaudio>=2.0',
    ],
)