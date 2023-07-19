import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='custom_annotations_manifold',
    version='0.0.2',
    author='Jyotika Patil',
    author_email='jpatil@identifeye.health',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jyotikahp/custom_annotations_manifold',
    license='MIT',
    packages=['custom_annotations_manifold'],
    install_requires=['boto3', 'requests']
)