from __future__ import unicode_literals

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .managers import UserManager

import uuid

class User(AbstractBaseUser, PermissionsMixin):
    user_id             = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name          = models.CharField(_('first name'), max_length=150)
    last_name           = models.CharField(_('last name'), max_length=150)
    password            = models.CharField(max_length=128, default=None)
    gender              = models.CharField(max_length=1)
    date_of_birth       = models.DateField(_('DOB'), null=True)
    email               = models.EmailField(_('email address'), max_length=100, unique=True)
    mobile              = models.CharField(_('mobile no'), max_length=15)
    date_joined         = models.DateTimeField(_('date joined'), auto_now=True)
    updated_on          = models.DateTimeField(_('updated'), null=True)
    author              = models.CharField(max_length=100, null=True)
    verification_hash   = models.CharField(max_length=255, null=True)
    verified            = models.BooleanField(default=False)
    last_login          = models.DateTimeField(null=True)
    is_superuser        = models.SmallIntegerField(null=False, default=0)
    is_staff            = models.SmallIntegerField(null=False, default=0)
    is_active           = models.SmallIntegerField(_('active'),null=False, default=0)
    avatar              = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'mobile']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

