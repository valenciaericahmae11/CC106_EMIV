from django.test import TestCase

from django.urls import reverse

from .models import Student


class StudentManagementTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            student_id='SRCC-TEST-001',
            first_name='Alex',
            last_name='Santos',
            gender='Male',
            date_of_birth='2004-02-15',
            contact_number='09170000001',
        )

    def student_data(self, **overrides):
        data = {
            'student_id': 'SRCC-TEST-002',
            'first_name': 'Jamie',
            'last_name': 'Reyes',
            'gender': 'Female',
            'date_of_birth': '2003-11-08',
            'contact_number': '09170000002',
        }
        data.update(overrides)
        return data

    def test_registration_creates_student_and_redirects(self):
        response = self.client.post(
            reverse('student_registration'),
            self.student_data(),
        )

        self.assertRedirects(response, reverse('registration_success'))
        self.assertTrue(
            Student.objects.filter(student_id='SRCC-TEST-002').exists()
        )

    def test_student_list_search_and_create_link(self):
        response = self.client.get(
            reverse('student_list'),
            {'q': 'Alex'},
        )

        self.assertContains(response, 'Alex')
        self.assertNotContains(response, 'Jamie')
        self.assertContains(response, reverse('student_create'))

    def test_create_form_rejects_missing_required_field(self):
        response = self.client.post(
            reverse('student_create'),
            self.student_data(first_name=''),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.assertEqual(Student.objects.count(), 1)

    def test_update_changes_existing_student(self):
        response = self.client.post(
            reverse('student_update', args=[self.student.pk]),
            self.student_data(student_id=self.student.student_id),
        )

        self.student.refresh_from_db()
        self.assertRedirects(
            response,
            reverse('student_detail', args=[self.student.pk]),
        )
        self.assertEqual(self.student.first_name, 'Jamie')

    def test_delete_requires_post(self):
        delete_url = reverse('student_delete', args=[self.student.pk])

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Student.objects.filter(pk=self.student.pk).exists())
        self.assertContains(response, 'Confirm Student Deletion')

        response = self.client.post(delete_url)
        self.assertRedirects(response, reverse('student_list'))
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
