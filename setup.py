from setuptools import setup, find_packages

setup(
    name="kanvas",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'transformers',
        'opencv-python',
        'pillow',
        'flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'kanvas=src.main:main',
        ],
    },
    description="Kanvas: A universal platform for AI-powered media generation",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your-email@example.com",
    url="https://github.com/your-username/kanvas",
    license="MIT",
)
