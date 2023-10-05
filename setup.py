from setuptools import setup
REQUIRES = [
    'records',
    'structlog',
    'curlify',
    'allure-pytest'
]



setup(
    name='db_client',
    version='0.1',
    packages=['db_client'],
    url='https://github.com/DiLysenk/restclient_dl',
    license='MIT',
    author='lysenkodmitry',
    author_email='-',
    install_requires=REQUIRES,
    description='db_client ohh'
)
