import unittest

from config import FIELDS
from db.config import START, STOP
from user import User


class VKUserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User('1')
        self.user_data = self.user.get_user_data()

    def test_user_id_isdigit(self):
        value = self.user.user_id.isdigit()
        self.assertTrue(value)

    def test_user_data_is_dict(self):
        self.assertIsInstance(self.user_data, dict)

    def test_get_groups_is_list(self):
        value = self.user.get_groups()
        self.assertIsInstance(value, list)

    def test_get_photos_is_list(self):
        value = self.user.get_photos()
        self.assertIsInstance(value, list)

    def test_search_results_is_list(self):
        value = self.user.search_users(1, 25, 30, 0)
        self.assertIsInstance(value[1], list)

    def test_search_results_are_instances(self):
        value = self.user.search_users(1, 25, 30, 0)
        self.assertIsInstance(value[1][0], User)


class ParamsTestCase(unittest.TestCase):
    def test_sex_in_fields(self):
        self.assertIn('sex', FIELDS.split(', '))

    def test_city_in_fields(self):
        self.assertIn('city', FIELDS.split(', '))

    def test_country_in_fields(self):
        self.assertIn('country', FIELDS.split(', '))

    def test_interests_in_fields(self):
        self.assertIn('interests', FIELDS.split(', '))

    def test_music_in_fields(self):
        self.assertIn('music', FIELDS.split(', '))

    def test_movies_in_fields(self):
        self.assertIn('movies', FIELDS.split(', '))

    def test_tv_in_fields(self):
        self.assertIn('tv', FIELDS.split(', '))

    def test_books_in_fields(self):
        self.assertIn('books', FIELDS.split(', '))

    def test_stop_gt_start(self):
        self.assertGreater(STOP, START)
