from django.test import TestCase
from blog.forms import CadastroUsuarioForm

class UserViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(UserViewTests, cls).setUpClass()
        print('\nUserViewTests')
        
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


    def test_UserForm_valid(self):
        form = CadastroUsuarioForm(data={'username': "joseflavio",
                                        'password1': "josepassword",
                                        'password2': "josepassword",
                                        'email': "jose@gmail.com",
                                        'foto': ""})
        self.assertTrue(form.is_valid())


    def test_UserForm_invalid(self):
        form = CadastroUsuarioForm(data={'username': "joseflavio",
                                        'password1': "josepassword",
                                        'password2': "josepassword",
                                        'email': "john@thebest.com",
                                        'foto': ""})
        self.assertTrue(form.is_valid())


