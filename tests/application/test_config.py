import pytest
import os

from pywolf.lang import pathutils
from pywolf.application.config import Config


def test_config_load():
    config_path = pathutils.current(__file__) + 'config/style1/'
    conf = Config(config_path).load()

    assert 'name_in_test_env' == conf.get('wolf.name')

