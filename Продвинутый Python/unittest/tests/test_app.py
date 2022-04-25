import unittest
import app
from unittest.mock import patch


class InitAppTest(unittest.TestCase):

    def test_upload_date(self):
        dirs, docs = {}, []
        self.assertFalse(dirs)
        dirs, docs = app.update_date()
        self.assertTrue(docs)
        self.assertTrue(dirs)
        self.assertIsInstance(dirs, dict)


class AppTest(unittest.TestCase):

    def setUp(self):
        self.dirs, self.docs = app.update_date()
        with patch('app.input', return_value='q'):
            with patch('app.update_date') as mock_ud:
                mock_ud.return_value = self.dirs, self.docs
                app.secretary_program_start()

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf('10006')
        self.assertNotIn('10006', self.dirs['2'])

    def test_add_docs(self):
        before_len = len(self.docs)
        user_input = ['123', 'passport', 'UserName', '111']
        with patch('app.input', side_effect=user_input):
            app.add_new_doc()

        self.assertGreater(len(self.docs), before_len)
        self.assertIn('111', self.dirs)

    def test_check_document_existance(self):
        doc_founded = app.check_document_existance('10006')
        self.assertTrue(doc_founded)

    def test_get_doc_owner_name(self):
        user_input = ['10006']
        with patch('app.input', side_effect=user_input):
            doc_name = app.get_doc_owner_name()

        self.assertEqual(doc_name, "Аристарх Павлов")

    def test_get_all_doc_owners_names(self):
        all_doc_list = app.get_all_doc_owners_names()
        self.assertIsInstance(all_doc_list, set)

    def test_get_doc_shelf(self):
        user_input = ['10006']
        with patch('app.input', side_effect=user_input):
            directory_number = app.get_doc_shelf()

        self.assertEqual(directory_number, '2')

        user_input = ['11111']
        with patch('app.input', side_effect=user_input):
            directory_number = app.get_doc_shelf()

        self.assertFalse(directory_number)

    def test_delete_doc(self):
        user_input = ['10006']
        with patch('app.input', side_effect=user_input):
            doc_number, flag = app.delete_doc()

        self.assertEqual(doc_number, '10006')
        self.assertTrue(flag)

    def test_add_new_shelf(self):
        user_input = ['4']
        with patch('app.input', side_effect=user_input):
            shelf_number, flag = app.add_new_shelf()
        self.assertEqual(shelf_number, '4')
        self.assertTrue(flag)

        user_input = ['2']
        with patch('app.input', side_effect=user_input):
            shelf_number, flag = app.add_new_shelf()
        self.assertEqual(shelf_number, '2')
        self.assertFalse(flag)
