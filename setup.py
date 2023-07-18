# from setuptools import setup
#
# setup(
#     name='custom_module',
#     version='1.0.0',
#     description='A module to add custom annotations',
#     author='Jyotika Patil',
#     author_email='jpatil@identifeye.health',
#     # url='https://github.com/yourusername/custom_module',custom_module
#     packages=['custom_module'],
# )
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='custom_module',
    version='0.0.1',
    author='Jyotika Patil',
    author_email='jpatil@identifeye.health',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jyotikahp/custom_annotations_manifold',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    # },
    license='MIT',
    packages=['custom_module'],
    install_requires=['boto3'],
)