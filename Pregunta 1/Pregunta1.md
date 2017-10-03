# Pregunta 1
### Single Responsability

Encontramos que este principio solid no se cumple en el codigo entregado pues existen muchas funciones dentro de las clases **CinePlaneta** y **CineStark** contiene muchas funciones que poseen responsabilidades diferentes, invalidando que las clases de encuentren enfocadas en un solo fin.

### Open - close

Encontramos que el c�digo brindado tampoco cuenta con el principio de Open - Close, pues para agregar una nueva *pel�cula*, *cine* o *funci�n* se tendr�a que modificar varias lineas del c�digo existente, sin la posibilidad de hacer cambios m�nimos y mantener la forma inicial del proyecto. Entonces, si bien se cubre la parte **open** (abierto a expanci�n) del c�digo,pues permite la creaci�n de nuevos objetos, la parte **close** (cerrado al cambio) no se encuentra disponible.


### Interface Segregation

Finalmente podemos observar que el principio de segregaci�n de interfaces no se cumple,pues se tienen clases muy grand.Ser�a m�s beneficioso que clases peque�as hereden de las clases **cine** y cada una implemente sus propios m�todos de acuerdo a los requerimientos de las mismas, de esa forma se evitar�a que algunas clases peque�as hereden m�todos que no van a emplear.
