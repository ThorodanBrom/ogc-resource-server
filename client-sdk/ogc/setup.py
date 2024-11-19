# coding: utf-8

"""
    OGC Compliant DX Resource Server

    OGC compliant Features and Common API definitions. Includes Schema and Response Objects.   <a href='/stac/api'>STAC API Documentation</a>    <a href='/metering/api'>DX Metering API Documentation</a>

    The version of the OpenAPI document: 1.0.1
    Contact: info@iudx.org.in
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "openapi-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="OGC Compliant DX Resource Server",
    author="Geospatial Data eXchange (GSX)",
    author_email="info@iudx.org.in",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "OGC Compliant DX Resource Server"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    OGC compliant Features and Common API definitions. Includes Schema and Response Objects.   &lt;a href&#x3D;&#39;/stac/api&#39;&gt;STAC API Documentation&lt;/a&gt;    &lt;a href&#x3D;&#39;/metering/api&#39;&gt;DX Metering API Documentation&lt;/a&gt;
    """,  # noqa: E501
    package_data={"openapi_client": ["py.typed"]},
)
