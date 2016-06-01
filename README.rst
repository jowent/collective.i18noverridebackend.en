.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.i18noverridebackend.en
==============================================================================

This product was built to provide a "best efforts" translations override for 
backend editors who only speak English, yet have to maintain multilingual Plone
sites.  It will override as many translations as possible without being seen by
public users.



Translations
------------

Translations of this product are welcome, but will need to actually be 
different products, e.g. for French `collective.i18noverridebackend.fr`.
Any known translations are shown below. If you create one please raise
a Pull Request so we can provide a link here,

- 


Installation
------------

Install collective.i18noverridebackend.en by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.i18noverridebackend.en

    zcml =
        collective.i18noverridebackend.en

and then running ``bin/buildout``

Note: the zcml part is important otherwise translations wont be overridden


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.i18noverridebackend.en/issues
- Source Code: https://github.com/collective/collective.i18noverridebackend.en
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know through the issue tracker above


License
-------

The project is licensed under the GPLv2.
