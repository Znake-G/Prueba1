from __future__ import annotations
from abc import ABC
from datetime import date
from typing import Any, List, Optional

#from person.persona import Instructor
#from product.relacion import PlanCliente, ProductoCliente

class Producto(ABC):

    def __init__(
        self, 
        id: int = 0, 
        nombre: str = '', 
        fecha_inicio: Optional[date] = None, 
        fecha_fin: Optional[date] = None, 
        estado_activo: bool = True, 
        valor: float = 0.0
    ) -> None:
        self._id = id
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._estado_activo = estado_activo
        self._valor = valor

    def get_nombre(self) -> str:
        return self._nombre

    def get_fecha_inicio(self) -> Optional[date]:
        return self._fecha_inicio

    def get_estado_activo(self) -> bool:
        return self._estado_activo
    
    def get_valor(self) -> float:
        return self._valor

    def set_estado_activo(self, estado_activo: bool) -> bool:
        self._estado_activo = estado_activo
        return True


class Curso(Producto):

    def __init__(self, instructor: "Instructor", **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__instructores: List["Instructor"] = [instructor]
        self.__productos_cliente: List["ProductoCliente"] = []
        self.__instructores[0].add_curso(self)

    def add_producto_cliente(self, producto_cliente: "ProductoCliente") -> bool:
        self.__productos_cliente.append(producto_cliente)
        return True


class Plan(Producto):

    def __init__(self, valor_maximo_curso: float, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__valor_maximo_curso = valor_maximo_curso
        self.__planes: List["PlanCliente"] = []

    def get_valor_maximo_curso(self) -> float:
        return self.__valor_maximo_curso

    def add_plan_cliente(self, plan: "PlanCliente") -> bool:
        self.__planes.append(plan)
        return True