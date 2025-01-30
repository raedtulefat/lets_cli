from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()
                and not line.startswith('#')]


setup(
    name='lets_cli',
    version='0.0.2',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'lets = lets_cli.main:main',
            'lets_setup = lets_cli.setup:interactive_setup',  # Add this line
        ],
    },
)
