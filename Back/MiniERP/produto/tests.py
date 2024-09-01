from django.test import TestCase
from .models import Produto

class ProtutoModelTests(TestCase):
    
    def setUp(self):
        Produto(nome="produto 1", preco= 10.0, quantidade=5)
        Produto(nome="produto 2", preco= 20.0, quantidade=4)

    def test_obter_todos(self):
        produtos = Produto.obter_todos()
        self.assertEqual(len(produtos), 2)

        self.assertEqual(produtos[0].nome, "produto 1")
        self.assertEqual(produtos[0].preco, 10)
        self.assertEqual(produtos[0].quantidade, 5)

        self.assertEqual(produtos[1].nome, "produto 2")
        self.assertEqual(produtos[1].preco, 20)
        self.assertEqual(produtos[1].quantidade, 4)