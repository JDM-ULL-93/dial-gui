# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

import json
import os

from pathlib import Path
from typing import Optional

import pkg_resources
from PySide2.QtCore import QStandardPaths


def version() -> str:
    """Returns the current version of the application."""
    from pkg_resources import DistributionNotFound
    try:
        return pkg_resources.require("dial-gui")[0].version
    except DistributionNotFound:
        return "0.1"


def config_directory() -> str:
    """Returns the configuration directory (This is the root dir for dial)"""
    """
        Changed by JDM. 11/03/2021
        ID:3
        From:
            config_dir = os.path.join(
                QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
                + os.path.sep
                + "dial"
            )
        To:
            config_dir = Path( QStandardPaths.writableLocation(QStandardPaths.ConfigLocation) ) / 'dial'
        Reason:
            Messed slashes in path ('\' first, then '//')
    """
    config_dir = Path( QStandardPaths.writableLocation(QStandardPaths.ConfigLocation) ) #/ 'dial'

    if not os.path.isdir(config_dir):
        os.mkdir(config_dir)

    return config_dir


def plugins_directory() -> str:
    """Returns the root directory for dial plugins (Where the `plugins.json` file is)"""
    """
        Changed by JDM. 11/03/2021
        ID:4
        From:
            plugins_directory = config_directory() + os.path.sep + "plugins"
        To:
            plugins_directory = config_directory() /  "plugins"
        Reason:
            Messed slashes in path ('\' first, then '//')
    """
    plugins_directory = config_directory() /  "plugins"

    if not os.path.isdir(plugins_directory):
        os.mkdir(plugins_directory)

    return plugins_directory


def plugins_install_directory() -> str:
    """Returns the directory where plugins are installed."""
    """
        Changed by JDM. 11/03/2021
        ID:5
        From:
            plugins_install_directory = plugins_directory() + os.path.sep + "site-packages"
        To:
            plugins_install_directory = plugins_directory() / "site-packages"
        Reason:
            Messed slashes in path ('\' first, then '//')
    """
    plugins_install_directory = plugins_directory() / "site-packages"

    if not os.path.isdir(plugins_install_directory):
        os.mkdir(plugins_install_directory)

    return plugins_install_directory


def installed_plugins_file() -> str:
    """Returns the file that contains which plugins are installed and active."""
    """
    Changed by JDM. 11/03/2021
        ID:6
        From:
            plugins_file_path = plugins_directory() + os.path.sep + "plugins.json"
        To:
            plugins_file_path = plugins_directory() / "plugins.json"
        Reason:
            Messed slashes in path ('\' first, then '//')
    """
    plugins_file_path = plugins_directory() / "plugins.json"

    if not os.path.isfile(plugins_file_path):
        with open(plugins_file_path, "w") as json_file:
            json.dump({}, json_file)

    return plugins_file_path


def installed_plugins_file_content() -> Optional[dict]:
    """Returns the content of the `plugins.json` file."""
    with open(installed_plugins_file()) as plugins_file:
        return json.load(plugins_file)

    return None
