from __future__ import annotations
from datetime import date

from core.clatzy import Clatzy

def main():
    clatzy = Clatzy()

    clatzy.add_instructor('Pedro Wightman', '123456789', '3000000001', 'pwightman@uninorte.edu.co')
    clatzy.add_instructor('Miguel Jimeno', '123456780', '3000000002', 'majimeno@uninorte.edu.co')
    clatzy.add_instructor('Augusto Salazar', '123456781', '3000000003', 'augustosalazar@uninorte.edu.co')
    clatzy.add_instructor('Marlene Duarte', '123456782', '3000000004', 'mduarte@uninorte.edu.co')
    clatzy.add_instructor('Gustavo Morales', '123456783', '3000000005', 'gmorales@uninorte.edu.co')
    clatzy.add_instructor('Maria Barrios', '123456784', '3000000006', 'mbarrios@uninorte.edu.co')
    clatzy.add_instructor('Carolina Alvarado', '123456785', '3000000007', 'calvarado@uninorte.edu.co')

    local_date = date(2023, 4, 22)
    
    clatzy.add_curso(0,'Introduccion a Python', local_date, 100_000, clatzy.get_instructor(2))
    clatzy.add_curso(1,'Introduccion a Bases de datos', local_date, 100_000, clatzy.get_instructor(1))
    clatzy.add_curso(2,'Programacion Optima', local_date, 100_000, clatzy.get_instructor(3))
    clatzy.add_curso(3,'Introduccion a GIS con PosGIS', local_date, 100_000, clatzy.get_instructor(0))
    clatzy.add_curso(4,'Introduccion a programacion web', local_date, 150_000, clatzy.get_instructor(2))
    clatzy.add_curso(5,'Introduccion a programacion movil', local_date, 150_000, clatzy.get_instructor(5))
    clatzy.add_curso(6,'Gerencia de proyectos', local_date, 150_000, clatzy.get_instructor(6))

    clatzy.add_plan('Plan ilimitado anual', local_date, 2_000_000, (1 << 31) - 1)
    clatzy.add_plan('Plan anual igual o menor a 100.000', local_date, 500_000, 100_000)

    clatzy.add_cliente('Pedro Perez', '223456789', '3000000001', 'pwightman@uninorte.edu.co')
    clatzy.add_cliente('Miguel Jimenez', '223456780', '3000000002', 'majimeno@uninorte.edu.co')
    clatzy.add_cliente('Augusto Belalcazar', '223456781', '3000000003', 'augustosalazar@uninorte.edu.co')
    clatzy.add_cliente('Jose Camacho', '223456782', '3000000004', 'jcapacho@uninorte.edu.co')
    clatzy.add_cliente('Gustavo Moradas', '223456783', '3000000005', 'gmorales@uninorte.edu.co')
    
    clatzy.comprar_plan(clatzy.get_cliente(0), clatzy.get_plan(1), local_date) # El valor del plancliente es el valor actual del plan
    clatzy.comprar_plan(clatzy.get_cliente(0), clatzy.get_plan(0), local_date) # Cliente ya tiene plan, debe fallar
    
    clatzy.get_cliente(0).get_plan(0).set_estado_activo(False) # El cliente desactiva su plan actual.
    
    clatzy.comprar_plan(clatzy.get_cliente(0), clatzy.get_plan(0), local_date) # El cliente ha adquirido un plan nuevo y no tiene planes activos
    clatzy.comprar_plan(clatzy.get_cliente(1), clatzy.get_plan(1), local_date)
    clatzy.comprar_plan(clatzy.get_cliente(4), clatzy.get_plan(0), local_date)
    
    # Si el cliente tiene plan, se almacena el valor de ProductoCliente como $0 pues no pago en efectivo por ese curso
    clatzy.comprar_curso(clatzy.get_cliente(0), clatzy.get_curso(3), local_date)
    clatzy.comprar_curso(clatzy.get_cliente(1), clatzy.get_curso(5), local_date) # Cliente tiene plan, pero no cubre esa clase
    clatzy.comprar_curso(clatzy.get_cliente(1), clatzy.get_curso(5), local_date, 150_000)
    clatzy.comprar_curso(clatzy.get_cliente(2), clatzy.get_curso(5), local_date, 149_000) # El cliente no pago lo suficiente
    clatzy.comprar_curso(clatzy.get_cliente(2), clatzy.get_curso(5), local_date, 150_000)
    clatzy.comprar_curso(clatzy.get_cliente(3), clatzy.get_curso(2), local_date, 150_000) # El valor es mayor al del curso
    clatzy.comprar_curso(clatzy.get_cliente(3), clatzy.get_curso(2), local_date, 100_000)
    clatzy.comprar_curso(clatzy.get_cliente(4), clatzy.get_curso(0), local_date)
    clatzy.comprar_curso(clatzy.get_cliente(4), clatzy.get_curso(1), local_date)
    clatzy.comprar_curso(clatzy.get_cliente(4), clatzy.get_curso(2), local_date)
    clatzy.comprar_curso(clatzy.get_cliente(2), clatzy.get_curso(0), local_date, 100_000)
    clatzy.comprar_curso(clatzy.get_cliente(0), clatzy.get_curso(3), local_date) # Debe fallar pues el cliente ya tiene el curso
    
    # Dado que el usuario tiene plan y este incluye el curso, se debe comprar sin colocar costo y mostrar mensaje de informacion
    clatzy.comprar_curso(clatzy.get_cliente(0), clatzy.get_curso(2), local_date, 100_000)
    clatzy.comprar_curso(clatzy.get_cliente(1), clatzy.get_curso(5), local_date, 150_000) # Como su plan no cubre ese curso, puede comprar la clase
    clatzy.comprar_curso(clatzy.get_cliente(2), clatzy.get_curso(1), local_date, 100_000)
    clatzy.comprar_curso(clatzy.get_cliente(3), clatzy.get_curso(1), local_date, 100_000)
    clatzy.comprar_curso(clatzy.get_cliente(3), clatzy.get_curso(1), local_date, 100_000) # Debe fallar pues el cliente ya tiene el curso

    # Dado que el usuario tiene plan y este incluye el curso, se debe comprar sin colocar costo y mostrar mensaje de informacion
    clatzy.comprar_curso(clatzy.get_cliente(4), clatzy.get_curso(6), local_date, 150_000)
    clatzy.comprar_curso(clatzy.get_cliente(1), clatzy.get_curso(2), local_date)
    clatzy.comprar_curso(clatzy.get_cliente(1), clatzy.get_curso(4), local_date, 150_000)
    clatzy.comprar_curso(clatzy.get_cliente(1), clatzy.get_curso(6), local_date, 150_000)
    
    print('\n----------------------------------------')
    print(f'El cliente que más ha pagado en efectivo por cursos es {clatzy.get_cliente_mayor_ingreso()}')
    print('----------------------------------------\n')
    
    print('------------- BONIFICACION -------------')
    clatzy.list_all()


if __name__ == '__main__':
    main()
