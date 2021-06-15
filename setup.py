import setuptools

setuptools.setup(
    name="executor-clip",
    version="2.0",
    author='Jina Dev Team',
    author_email='dev-team@jina.ai',
    description="Executors that encode images",
    url="https://github.com/jina-ai/executor-clip-image",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    py_modules=['jinahub.encoder.image.clip'],
    packages=setuptools.find_packages(where='.', include=['jinahub.*']),
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.7",
)


# from jinahub.encoder.image.clip import CLIPImageEncoder
# from jinahub.encoder.text.clip import CLIPTextEncoder