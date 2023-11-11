from __future__ import annotations
from datetime import date
from typing import Any

#from person.persona import Cliente
from product.producto import Curso, Plan, Producto

class PlanCliente(Producto):

    def __init__(self, cliente: "Cliente", plan: "Plan", **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__cliente = cliente
        self.__plan = plan
        self.__cliente.add_plan(self)
        self.__plan.add_plan_cliente(self)

    def get_cliente(self) -> "Cliente":
        return self.__cliente
    
    def get_plan(self) -> "Plan":
        return self.__plan


class ProductoCliente(Producto):

    def __init__(
        self, 
        cliente: "Cliente", 
        curso: "Curso", 
        estado_aprobado: bool = False, 
        nivel_avance: int = 0, 
        **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self.__estado_aprobado = estado_aprobado
        self.__nivel_avance = nivel_avance
        self.__cliente = cliente
        self.__curso = curso
        self.__cliente.add_producto(self)
        self.__curso.add_producto_cliente(self)

    def get_cliente(self) -> "Cliente":
        return self.__cliente
    
    def get_curso(self) -> "Curso":
        return self.__curso