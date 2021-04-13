from setuptools import setup

setup(
    name="dokkasaurus",
    version="0.2.0",
    py_modules=["dokkasaurus"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        dokkasaurus=dokkasaurus:cli
    """,
)
