
#1 Crear un estudiante:
curl -X POST -H "Content-Type: application/json" \
-d '{"nombre_estudiante":"Dylan Rodriguez","horario_clase":"8:00-10:00","nombre_clase":"Desarrollo web","docente_clase":"Profe Andres Miranda"}' \
http://127.0.0.1:5000/estudiantes

#2 listar estudiantes 
curl http://127.0.0.1:5000/estudiantes

#3 buscar estudiantes 
curl http://127.0.0.1:5000/estudiantes/1



