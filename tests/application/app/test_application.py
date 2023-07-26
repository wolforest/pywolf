import pytest
import asyncio

from pywolf.utils import pathutils
from pywolf.application.application import Application
from pywolf.application.context import context


async def main():
    print('test application start ...')
    await asyncio.sleep(1)
    print('test application stoped')


def test_app_flow():
    app_path = pathutils.dirname(__file__)
    Application(app_path)
    # .run(main())

    conf = context.get_config()
    assert 'name_in_test_env' == conf.get('wolf.name')
