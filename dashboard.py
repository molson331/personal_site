"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'personal_site.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.ModelList(
            title=('Event Configuration'),
            column=1,
            collapsible=False,
            models=('personal.models.Event')
        ))

        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('Group: Administration & Applications'),
            column=1,
            collapsible=False,
            children = [
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Applications'),
                    column=1,
                    css_classes=('collapse closed',),
                    exclude=('django.contrib.*',),
                )
            ]
        ))  
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


