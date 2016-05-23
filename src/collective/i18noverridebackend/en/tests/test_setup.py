# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.i18noverridebackend.en.testing import COLLECTIVE_I18NOVERRIDEBACKEND_EN_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.i18noverridebackend.en is properly installed."""

    layer = COLLECTIVE_I18NOVERRIDEBACKEND_EN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.i18noverridebackend.en is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.i18noverridebackend.en'))

    def test_browserlayer(self):
        """Test that ICollectiveI18NoverridebackendEnLayer is registered."""
        from collective.i18noverridebackend.en.interfaces import (
            ICollectiveI18NoverridebackendEnLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveI18NoverridebackendEnLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_I18NOVERRIDEBACKEND_EN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.i18noverridebackend.en'])

    def test_product_uninstalled(self):
        """Test if collective.i18noverridebackend.en is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.i18noverridebackend.en'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveI18NoverridebackendEnLayer is removed."""
        from collective.i18noverridebackend.en.interfaces import ICollectiveI18NoverridebackendEnLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveI18NoverridebackendEnLayer, utils.registered_layers())
