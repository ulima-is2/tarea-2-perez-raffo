# Pregunta 1
### Single Responsability

Encontramos que este principio solid no se cumple en el codigo entregado pues existen muchas funciones dentro de las clases **CinePlaneta** y **CineStark** contiene muchas funciones que poseen responsabilidades diferentes, invalidando que las clases de encuentren enfocadas en un solo fin.

### Open - close

Encontramos que el código brindado tampoco cuenta con el principio de Open - Close, pues para agregar una nueva *película*, *cine* o *función* se tendría que modificar varias lineas del código existente, sin la posibilidad de hacer cambios mínimos y mantener la forma inicial del proyecto. Entonces, si bien se cubre la parte **open** (abierto a expanción) del código,pues permite la creación de nuevos objetos, la parte **close** (cerrado al cambio) no se encuentra disponible.


### Interface Segregation

Finalmente podemos observar que el principio de segregación de interfaces no se cumple,pues se tienen clases muy grand.Sería más beneficioso que clases pequeñas hereden de las clases **cine** y cada una implemente sus propios métodos de acuerdo a los requerimientos de las mismas, de esa forma se evitaría que algunas clases pequeñas hereden métodos que no van a emplear.
