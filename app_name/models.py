from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models


class SubjectModel(models.Model):

    # Fields
    name = models.CharField(max_length=20,primary_key=True,verbose_name='Subject Name')
    code = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    units = models.IntegerField()

    # Relationship Fields
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="subjectmodels",
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_name_subjectmodel_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_name_subjectmodel_update', args=(self.pk,))
