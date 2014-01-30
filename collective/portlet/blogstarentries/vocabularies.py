try:
    from zope.app.schema.vocabulary import IVocabularyFactory
except ImportError:
    from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.i18n import translate
from Acquisition import aq_get
from collective.portlet.blogstarentries import BlogstarLastEntriesMessageFactory as _


class BlogEntryStatesVocabulary(object):
    """
    A simple vocab to translate the discussion states
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        request = aq_get(context, 'REQUEST', None)

        return SimpleVocabulary.fromItems(((translate(_('Draft'), context=request), 'visible'),
                                           (translate(_('Private'), context=request), 'private'),
                                           (translate(_('Published'), context=request), 'published'),))

BlogEntryStatesVocabularyFactory = BlogEntryStatesVocabulary()
