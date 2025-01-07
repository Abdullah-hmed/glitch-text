from setuptools import setup

setup(
    name="glitch-text",
    version="1.0.0",
    py_modules=["glitch"],
    entry_points={
        "console_scripts": [
            "glitch=glitch:main",
        ],
    },
    author="Abdullah Ahmed",
    description="A glitchy text effect tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/abdullah-hmed/glitch-text',
    license='MIT',
    python_requires=">=3.6",
    install_requires=[],
)
