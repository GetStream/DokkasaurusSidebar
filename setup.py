from setuptools import setup

setup(
    name="dokkasauros",
    version="0.1.3",
    py_modules=["dokkasauros"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        dokkasauros=dokkasauros:cli
    """,
)
