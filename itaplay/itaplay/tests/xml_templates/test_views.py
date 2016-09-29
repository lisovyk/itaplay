import json

from django.test import TestCase, Client
from xml_templates.models import XmlTemplate
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse


class XmlTemplateViewTests(TestCase):

    def setUp(self):
        XmlTemplate.objects.create(
            id=1,
            template_name='template1',
            template_content='''<?xml ><name="template1"></project>''',
        )

        XmlTemplate.objects.create(
            id=2,
            template_name='template2',
            template_content='''<?xml ><name="template2"></project> ''',
        )

        User.objects.create(
            id=1,
            username="superuser@user.com",
            email="super@user.com",
            password="password1",
            is_superuser=True,
        )

        self.client = Client()

    def test_get_list_xml_templates_loads(self):
        self.client.login(username="superuser@user.com",
                          password="password1")
        url = reverse('templates_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_list_xml_templates(self):
        self.client.login(username="superuser@user.com",
                          password="password1")
        url = reverse('templates_list')
        response = self.client.get(url)
        self.assertContains(response, "template1")
        self.assertContains(response, "template2")

    def test_get_detail_xml_templates_loads(self):
        self.client.login(username="superuser@user.com",
                          password="password1")
        url = reverse("template_current", args=[1, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_detail_xml_templates(self):
        self.client.login(username="superuser@user.com",
                          password="password1")
        url = reverse("template_current", args=[1, ])
        response = self.client.get(url)
        data = json.loads(response.content)
        content = {'template_content': '<?xml ><name="template1"></project>',
                   'template_name': 'template1', 'id': 1}
        self.assertEqual(data, content)

    def test_add_xml_templates_loads(self):
        self.client.login(username="superuser@user.com",
                          password="password1")
        url = reverse("template_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_xml_template(self):
        self.client.login(username="superuser@user.com",
                          password="password1")
        url = reverse("template_delete", args=[1, ])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(XmlTemplate.objects.count(), 1)
