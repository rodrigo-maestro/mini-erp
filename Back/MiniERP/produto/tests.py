from django.test import TestCase
from .models import Produto

class ProtutoModelTests(TestCase):
    
    def setUp(self):
        Produto.id_counter = 0
        Produto.produto_list = []
        Produto(nome="produto 1", preco= 10.0, quantidade=5)
        Produto(nome="produto 2", preco= 20.0, quantidade=4)

    def test_obter_todos(self):
        produtos = Produto.obter_todos()
        self.assertEqual(len(produtos), 2)

        self.assertEqual(produtos[0].id, 1)
        self.assertEqual(produtos[0].nome, "produto 1")
        self.assertEqual(produtos[0].preco, 10)
        self.assertEqual(produtos[0].quantidade, 5)

        self.assertEqual(produtos[1].id, 2)
        self.assertEqual(produtos[1].nome, "produto 2")
        self.assertEqual(produtos[1].preco, 20)
        self.assertEqual(produtos[1].quantidade, 4)

    def test_obter_por_id(self):
        produto1 = Produto.obter_por_id(1)
        produto2 = Produto.obter_por_id(2)

        self.assertEqual(produto1.id, 1)
        self.assertEqual(produto1.nome, "produto 1")
        self.assertEqual(produto1.preco, 10)
        self.assertEqual(produto1.quantidade, 5)

        self.assertEqual(produto2.id, 2)
        self.assertEqual(produto2.nome, "produto 2")
        self.assertEqual(produto2.preco, 20)
        self.assertEqual(produto2.quantidade, 4)

    def test_alterar(self):
        Produto.alterar(1, "produto alterado", 30, 3)

        produtos = Produto.obter_todos()

        self.assertEqual(len(produtos), 2)

        self.assertEqual(produtos[0].id, 1)
        self.assertEqual(produtos[0].nome, "produto alterado")
        self.assertEqual(produtos[0].preco, 30)
        self.assertEqual(produtos[0].quantidade, 3)

        self.assertEqual(produtos[1].id, 2)
        self.assertEqual(produtos[1].nome, "produto 2")
        self.assertEqual(produtos[1].preco, 20)
        self.assertEqual(produtos[1].quantidade, 4)

    def test_remover(self):
        Produto.remover(1)

        produtos = Produto.obter_todos()

        self.assertEqual(len(produtos), 1)

        self.assertEqual(produtos[0].id, 2)
        self.assertEqual(produtos[0].nome, "produto 2")
        self.assertEqual(produtos[0].preco, 20)
        self.assertEqual(produtos[0].quantidade, 4)