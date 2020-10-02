import unittest
from django.urls import reverse
from django.test import Client
from .models import SubjectModel
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_subjectmodel(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["code"] = "code"
    defaults["branch"] = "branch"
    defaults["units"] = "units"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return SubjectModel.objects.create(**defaults)


class SubjectModelViewTest(unittest.TestCase):
    '''
    Tests for SubjectModel
    '''
    def setUp(self):
        self.client = Client()

    def test_list_subjectmodel(self):
        url = reverse('app_name_subjectmodel_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_subjectmodel(self):
        url = reverse('app_name_subjectmodel_create')
        data = {
            "name": "name",
            "code": "code",
            "branch": "branch",
            "units": "units",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_subjectmodel(self):
        subjectmodel = create_subjectmodel()
        url = reverse('app_name_subjectmodel_detail', args=[subjectmodel.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_subjectmodel(self):
        subjectmodel = create_subjectmodel()
        data = {
            "name": "name",
            "code": "code",
            "branch": "branch",
            "units": "units",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('app_name_subjectmodel_update', args=[subjectmodel.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


