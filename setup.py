from setuptools import setup
from setuptools import find_packages

version = '1'

# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.
install_requires = [
    'acme>0.24.0',
    'certbot>=0.21.1',
    'boto3',
    'mock',
    'setuptools',
    'zope.interface',
]

setup(
    name='certbot-dns-nsof',
    version=version,
    description="Meta networks route53 DNS Authenticator plugin for Certbot",
    url="https://www.metanetworks.com",
    author="Yuval Mishan",
    author_email='yuval@metanetworks.com',
    license='Apache License 2.0',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    keywords=['certbot', 'route53', 'aws', 'nsof'],
    entry_points={
        'certbot.plugins': [
            'nsof = certbot_dns_nsof.nsof_dns_route53:Authenticator',
        ],
    },
)
