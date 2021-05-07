from setuptools import setup, find_packages

setup(
    name="dokkasaurus",
    version="0.3.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        dokkasaurus=sidebar.dokkasaurus:cli
    """,
)
