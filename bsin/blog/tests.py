from django.test import TestCase
from blog.forms import CadastroUsuarioForm
from django.test import Client, SimpleTestCase

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

    def test_home_view(self):
        client = Client()
        user_login = client.login(username="joseflavio", password="josepassword")
        self.assertTrue(user_login)
        response = client.get("/blog/")
        self.assertEqual(response.status_code, 200)


    def test_usuario_cadastrar(self):
        client = Client()
        url = '/blog/templates/cadastro/cadastro.html'
        response = client.get(url)

        self.assertEqual(200, response.status_code)

    


