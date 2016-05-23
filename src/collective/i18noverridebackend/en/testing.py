# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.i18noverridebackend.en


class CollectiveI18NoverridebackendEnLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.i18noverridebackend.en)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.i18noverridebackend.en:default')


COLLECTIVE_I18NOVERRIDEBACKEND_EN_FIXTURE = CollectiveI18NoverridebackendEnLayer()


COLLECTIVE_I18NOVERRIDEBACKEND_EN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_I18NOVERRIDEBACKEND_EN_FIXTURE,),
    name='CollectiveI18NoverridebackendEnLayer:IntegrationTesting'
)


COLLECTIVE_I18NOVERRIDEBACKEND_EN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_I18NOVERRIDEBACKEND_EN_FIXTURE,),
    name='CollectiveI18NoverridebackendEnLayer:FunctionalTesting'
)


COLLECTIVE_I18NOVERRIDEBACKEND_EN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_I18NOVERRIDEBACKEND_EN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveI18NoverridebackendEnLayer:AcceptanceTesting'
)
