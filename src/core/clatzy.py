from datetime import date, timedelta
from typing import List

from person.persona import Cliente, Instructor
from product.producto import Curso, Plan
from product.relacion import PlanCliente, ProductoCliente

class Clatzy:
    
    def __init__(self) -> None:
        self.__clientes: List["Cliente"] = []
        self.__cursos: List["Curso"] = []
        self.__instructores: List["Instructor"] = []
        self.__planes: List["Plan"] = []

    def add_cliente(self, nombre: str, cedula: str, telefono: str, email: str) -> bool:
        self.__clientes.append(Cliente(nombre, cedula, telefono, email))
        return True

    def add_curso(self, id: int, nombre: str, fecha_inicio: date, valor: float, instructor: "Instructor") -> bool:
        self.__cursos.append(Curso(
            id = id,
            nombre = nombre,
            fecha_inicio = fecha_inicio,
            valor = valor,
            instructor = instructor
        ))
        return True

    def add_instructor(self, nombre: str, cedula: str, telefono: str, email: str) -> bool:
        self.__instructores.append(Instructor(nombre, cedula, telefono, email))
        return True

    def add_plan(self, nombre: str, fecha_inicio: date, valor: float, valor_maximo_curso: float) -> bool:
        self.__planes.append(Plan(
            nombre = nombre, 
            fecha_inicio = fecha_inicio,
            valor = valor,
            valor_maximo_curso = valor_maximo_curso
        ))
        return True
    
    def get_cliente(self, index: int) -> "Cliente":
        return self.__clientes[index]

    def get_curso(self, index: int) -> "Curso":
        return self.__cursos[index]

    def get_instructor(self, index: int) -> "Instructor":
        return self.__instructores[index]

    def get_plan(self, index: int) -> "Plan":
        return self.__planes[index]

    def comprar_curso(self, cliente: "Cliente", curso: "Curso", fecha: date, valor: float = 0) -> bool:
        has_curso, obtencion = cliente.has_curso_comprado_registrado(curso)
        if has_curso:
            print(f'El cliente {cliente.get_nombre()} ya habia {obtencion} el curso {curso.get_nombre()}')
            return False
        else:
            if cliente.has_plan_activo():
                plan_cliente = cliente.get_plan_activo()
                if curso.get_valor() <= plan_cliente.get_plan().get_valor_maximo_curso():
                    if valor == 0:
                        producto_cliente = ProductoCliente(
                            fecha_inicio = fecha,
                            valor = valor,
                            cliente = cliente,
                            curso = curso
                        )
                        
                        print(
                            f'El cliente {producto_cliente.get_cliente().get_nombre()}',
                            f'registro exitosamente el curso {producto_cliente.get_curso().get_nombre()}'
                        )
                    else:
                        producto_cliente = ProductoCliente(
                            fecha_inicio = fecha,
                            valor = 0,
                            cliente = cliente,
                            curso = curso
                        )
                        
                        print(
                            f'El curso está incluido en el plan del cliente {producto_cliente.get_cliente().get_nombre()},',
                            f'por lo tanto no debe pagar. Se procede a registrar el curso {producto_cliente.get_curso().get_nombre()}',
                            f'con costo $0'
                        )
                    return True
                else:
                    if valor == 0:
                        print(
                            f'El plan del cliente {cliente.get_nombre()}',
                            f'no cubre el curso {curso.get_nombre()}'
                        )
                        return False
                    else:
                        if valor == curso.get_valor():
                            producto_cliente = ProductoCliente(
                                fecha_inicio = fecha,
                                valor = valor,
                                cliente = cliente,
                                curso = curso
                            )

                            print(
                                f'El cliente {producto_cliente.get_cliente().get_nombre()}',
                                f'compro exitosamente el curso {producto_cliente.get_curso().get_nombre()}'
                            )
                            return True
                        else:
                            print(
                                f'El cliente {cliente.get_nombre()} no pago el valor correcto',
                                f'por el curso {curso.get_nombre()}'
                            )
                            return False
            else:
                if valor == curso.get_valor():
                    producto_cliente = ProductoCliente(
                        fecha_inicio = fecha,
                        valor = valor,
                        cliente = cliente,
                        curso = curso
                    )

                    print(
                        f'El cliente {producto_cliente.get_cliente().get_nombre()}',
                        f'compro exitosamente el curso {producto_cliente.get_curso().get_nombre()}'
                    )
                    return True
                else:
                    print(
                        f'El cliente {cliente.get_nombre()} no pago el valor correcto',
                        f'por el curso {curso.get_nombre()}'
                    )
                    return False
    
    def comprar_plan(self, cliente: "Cliente", plan: "Plan", fecha: date) -> bool:
        if cliente.has_plan_activo():
            print(f'El cliente {cliente.get_nombre()} ya tiene un plan activo')
            return False
        
        plan_cliente = PlanCliente(
            fecha_inicio = fecha,
            fecha_fin = (fecha + timedelta(days = 365)),
            valor = plan.get_valor(),
            cliente = cliente,
            plan = plan
        )

        print(
            f'El cliente {plan_cliente.get_cliente().get_nombre()}',
            f'compro exitosamente un plan {plan_cliente.get_plan().get_nombre()}'
        )
        return True

    def get_cliente_mayor_ingreso(self) -> str:
        ingresos = {}
        for cliente in self.__clientes:
            ingresos[cliente.get_nombre()] = cliente.get_ingreso()

        return max(ingresos, key = ingresos.get)

    def list_all(self) -> None:
        print('Lista de clientes con sus compras:')
        for cliente in self.__clientes:
            print('----------------------------------------')
            print(cliente.get_nombre())
            print('Planes:')
            for plan in cliente.get_planes():
                print(
                    f'{plan.get_plan().get_nombre()}',
                    f'{plan.get_fecha_inicio()}',
                    f'{plan.get_valor():.1f}',
                    f'{plan.get_estado_activo()}'
                )

            print('\nCursos:')
            for producto in cliente.get_productos():
                print(
                    f'{producto.get_curso().get_nombre()}',
                    f'{producto.get_fecha_inicio()}',
                    f'{producto.get_valor():.1f}',
                    f'{producto.get_estado_activo()}'
                )