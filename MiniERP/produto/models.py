from django.db import models

class Produto:
    id_counter = 1
    produto_list = []

    def __init__(self, nome, preco, quantidade):
        self.id = Produto.id_counter
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto.id_counter += 1
        Produto.produto_list.append(self)

    @classmethod
    def obter_todos(cls):
        return cls.produto_list
    
    @classmethod
    def obter_por_id(cls, produto_id):
        return next((p for p in cls.produto_list if p.id == produto_id), None)
    
    @classmethod
    def alterar(cls, produto_id, nome, preco, quatidade):
        produto = cls.obter_por_id(produto_id)
        if produto:
            produto.nome = nome
            produto.preco = preco
            produto.quantidade = quatidade
    
    @classmethod
    def remover(cls, produto_id):
        produto = cls.obter_por_id(produto_id)
        if produto:
            cls.produto_list.remove(produto)