import datetime
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
import uuid

class InviteRequest(models.Model):
    email = models.EmailField(_('Email address'), unique=True)
    created = models.DateTimeField(_('Created'), default=datetime.datetime.now)
    invited = models.BooleanField(_('Invited'), default=False)
    invitation_code = models.CharField(max_length = 10, blank=True,
                                       unique=True, null=True)
    invited_date = models.DateTimeField(_('Invited Date'),
                                        null=True, blank=True)
    used_invitation = models.BooleanField(_('Used invitation'),
                                          default=False)
    used_invitation_date = models.DateTimeField(_('Used invitation date'),
                                                null=True, blank=True)

    def __unicode__(self):
        return _('Invite for %(email)s') % {'email': self.email}

    def send_invite(self):
        '''Method to send email with invite and update model information
        according to that'''
        self.invited_date = datetime.datetime.now()
        self.invitation_code =  str(uuid.uuid1()).split('-')[0]
        self.invited = True
        data = {
                'code': reverse('privatebeta_activate_invite',
                                args=[self.invitation_code]),
                'site': Site.objects.get_current()
               }
        context = Context(data)
        email_template = get_template('privatebeta/invitation_email.html')
        email_message = email_template.render(context)
        send_mail('Your invitation for askbot.com',
                email_message, 'admin@askbot.com', [self.email])
        self.save()

    def invite_used(self):
        self.used_invitation = True
        self.used_invitation_date = datetime.datetime.now()
        self.save()
