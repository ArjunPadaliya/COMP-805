from django.test import TestCase
from .models import Resume, Education, Experience
# Create your tests here.
class ResumeTestCase(TestCase):

    def setUp(self):
        my_resume=Resume(first_name="Arjun", last_name="Padaliya")
        my_resume.save()

    def test_get_full_name(self):
        """
        Testing get_full_name function
        """
        full_name=Resume.objects.first()
        self.assertEqual(full_name.get_full_name(), "Arjun Padaliya")

    def test_last_name_first_name(self):
        """
        testting last_name_first_name function
        """
        last_name_first=Resume.objects.first()
        self.assertEqual(last_name_first.last_name_first_name(), "Padaliya, Arjun")

    def test_get_experience(self):
        """
        testing get_experience function
        """
        edu=Resume.objects.first()
        actual=list(edu.get_education())
        expected=list(edu.education_set.all())
        self.assertEqual(actual, expected)


    def test_get_education(self):
        """
        testing get_education function
        """
        exp=Resume.objects.first()
        actual=list(exp.get_experience())
        expected=list(exp.experience_set.all())
        self.assertEqual(actual, expected)
