1. Crear vista de calendario para turnos
2. Crear vista de calendario para generador de turnos
3. Crear vista calendario para dias no laborales
4. Donde haya fecha desde y hasta, al cambiar la fecha desde, proponer la misma como fecha Hasta
5. Generación de Turnos


1. Recorrer los dias desde la fecha Desde hasta la fecha hasta
    
    2. If
       1. Si el dia es un dia laboral(no esta el registro en un dia no laboral) y 
       2. el dia de la semana esta habilitado:
        
       3. while 
           1. por rango entre 0 y cant de turnos simultaneos de la compania 
           
           4. mientras la hora de inicio sea menos que la hora de finalizacion para la compania:
            
                5. genera un turno
                6. aumenta la hora de inicio segun la duración de la compania
    

a. 1 - 5
b. 1 - 2.2 - 5
c. 1 - 2 - 5 
d. 1 - 2 - 3 - 5
e. 1 - 2 - 3 - 4 - 5 - 6