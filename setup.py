from setuptools import setup

setup(
    name='dyao',
    version='0.1.0',
    author = "Daryl Joe Yao",
    author_email = "djy@sourcepad.com",
    description = "Python Skeleton",
    entry_points={
        'console_scripts': [
            'dyao=setup_protocol:run'
        ]
    }
)
