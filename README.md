Conversor pasa archivos xlxs a csv. Esto es de gran ayuda para futuras operaciones con csv y agiliza manejo de operaciones en excel.

Detalles:

*Elimina filas y columnas vacias.
*En carpeta archivos excel se pone los archivos xlxs a convertir
*En carpeta archivos csv apareceran los convertidos de xlxs a csv

Este proyecto estará en GitHub y se agregará funcionalidades de ser necesario en el tiempo.

----------------------
Posibles implementaciones según necesidades
----------------------

Si queremos seleccionar columnas especificas 
(Se pondria antes de la conversión de línea /*Línea 28*/)
datos = datos.loc[:, ["NombreColumnaA", "NombreColumnaB"]]

----------------------
