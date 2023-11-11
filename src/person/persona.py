from __future__ import annotations
from abc import ABC
from typing import List, Optional, Tuple

from product.producto import Curso
from product.relacion import PlanCliente, ProductoCliente

class Persona(ABC):

    def __init__(self, nombre: str, cedula: str, telefono: str, email: str) -> None:
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        self._email = email

    def get_nombre(self) -> str:
        return self._nombre


class Cliente(Persona):

    def __init__(self, nombre: str, cedula: str, telefono: str, email: str) -> None:
        super().__init__(nombre, cedula, telefono, email)
        self.__planes: List["PlanCliente"] = []
        self.__productos: List["ProductoCliente"] = []

    def get_planes(self) -> List["PlanCliente"]:
        return self.__planes
    
    def get_productos(self) -> List["ProductoCliente"]:
        return self.__productos

    def add_plan(self, plan: "PlanCliente") -> bool:
        self.__planes.append(plan)
        return True
    
    def add_producto(self, producto: "ProductoCliente") -> bool:
        self.__productos.append(producto)
        return True

    def get_plan(self, index: int) -> "PlanCliente":
        return self.__planes[index]
    
    def get_plan_activo(self) -> Optional["PlanCliente"]:
        for plan in self.__planes:
            if plan.get_estado_activo():
                return plan
        return None
    
    def get_ingreso(self) -> float:
        ingresos = 0
        for producto in self.__productos:
            ingresos += producto.get_valor()
        return ingresos
    
    def has_plan_activo(self) -> bool:
        for plan in self.__planes:
            if plan.get_estado_activo():
                return True
        return False
    
    def has_curso_comprado_registrado(self, curso: "Curso") -> Tuple[bool, Optional[str]]:
        for producto in self.__productos:
            if producto.get_curso() == curso:
                return (True, 'registrado') if producto.get_valor() == 0 else (True, 'comprado')
        return False, None


class Instructor(Persona):

    def __init__(self, nombre: str, cedula: str, telefono: str, email: str) -> None:
        super().__init__(nombre, cedula, telefono, email)
        self.__cursos: List["Curso"] = []

    def add_curso(self, curso: "Curso") -> bool:
        self.__cursos.append(curso)
        return True