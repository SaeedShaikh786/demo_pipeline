from setuptools import setup,find_packages

setup(name="censos-income",
        version="0.0.1",
        author="saeed",
        author_email="saidshaikh.nagar@gmail.com",
        packages=find_packages(),
        install_requirements=["pandas","flask"]
        )

