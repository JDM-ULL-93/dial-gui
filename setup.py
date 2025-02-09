# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="dial-gui",
    version="0.11a0",
    description="A node-based GUI for Deep Learning tasks",
    python_requires="<=3.8.3,>=3.6.0",
    project_urls={
        "homepage": "https://github.com/JDM-ULL-93/dial-gui",
        "repository": "https://github.com/JDM-ULL-93/dial-gui",
    },
    author="David Afonso",
    author_email="davafons@gmail.com",
    license="GPL-3.0-only",
    keywords="deep-learning",
    packages=[
        "dial_gui",
        "dial_gui.event_filters",
        "dial_gui.main_window",
        "dial_gui.node_editor",
        "dial_gui.project",
        "dial_gui.utils",
        "dial_gui.widgets",
        "dial_gui.widgets.editor_tabwidget",
        "dial_gui.widgets.log",
        "dial_gui.widgets.menus",
        "dial_gui.widgets.node_editor",
        "dial_gui.widgets.plugin",
        "dial_gui.widgets.plugin.plugins_table",
    ],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        "PySide2==5.*,>=5.12.6",
        "qimage2ndarray==1.*,>=1.8.3",
        "dependency-injector==3.*,>=3.15.6",
        "nbconvert==5.*,>=5.6.1"
    ],
    extras_require={
        "dev": [
            "black==19.*,>=19.10.0.b0",
            "docstr-coverage==1.*,>=1.0.5",
            "flake8==3.*,>=3.7.9",
            "isort==4.*,>=4.3.21",
            "mypy==0.*,>=0.761.0",
            "pre-commit==2.*,>=2.1.1",
            "pylint==2.*,>=2.4.4",
            "pytest==5.*,>=5.2.0",
            "pytest-cov==2.*,>=2.4.0",
            "pytest-qt==3.*,>=3.3.0",
            "mkdocs==1.*>=1.1",
            "taskipy==1.*,>=1.1.3",
            "tox==3.*,>=3.14.5",
        ]
    },
)
