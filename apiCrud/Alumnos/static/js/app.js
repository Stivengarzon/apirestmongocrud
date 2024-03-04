var alumnoIdModificar;

    function cargarAlumnos() {
        $.ajax({
            url: '/api/alumnos/',
            type: 'GET',
            success: function(data) {
                var html = '';
                $.each(data, function(index, alumno) {
                    html += '<tr>';
                    html += '<td>' + alumno.AlumnoNombre + '</td>';
                    html += '<td>' + alumno.AlumnoPrograma + '</td>';
                    html += '<td>' + alumno.FechaDeIngreso + '</td>';
                    html += '<td><a class="edit cursor-pointer" title="Edit" data-toggle="tooltip" onclick="mostrarFormularioModificar(' + alumno.AlumnoId + ')"><i class="fa fa-pencil"></i></a> <a class="delete cursor-pointer" title="Delete" data-toggle="tooltip" onclick="eliminarAlumno(' + alumno.AlumnoId + ')"><i class="fa fa-trash"></i></a></td>';
                    html += '</tr>';
                });
                $('#alumnos-container').html(html);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    }

    function mostrarFormulario() {
        $('#formulario-modificar').hide();
        $('#formulario-agregar').toggle();
    }

    function agregarAlumno() {
        var nombre = $('#nombre').val();
        var programa = $('#programa').val();
        var fechaIngreso = $('#fecha-ingreso').val();

        $.ajax({
            url: '/api/alumnos/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({AlumnoNombre: nombre, AlumnoPrograma: programa, FechaDeIngreso: fechaIngreso}),
            success: function(response) {
                console.log(response);
                cargarAlumnos();
                $('#nombre').val('');
                $('#programa').val('');
                $('#fecha-ingreso').val('');
                $('#formulario-agregar').hide();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    }

    function eliminarAlumno(id) {
        $.ajax({
            url: '/api/alumnos/' + id + '/',
            type: 'DELETE',
            success: function(response) {
                console.log(response);
                cargarAlumnos();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    }

    function mostrarFormularioModificar(id) {
        // Cerrar el formulario de agregar si está abierto
        $('#formulario-agregar').hide();

        alumnoIdModificar = id;
        // Obtener los datos del alumno y completar el formulario de modificar
        $.ajax({
            url: '/api/alumnos/' + id + '/',
            type: 'GET',
            success: function(alumno) {
                $('#nombre-modificar').val(alumno.AlumnoNombre);
                $('#programa-modificar').val(alumno.AlumnoPrograma);
                $('#fecha-ingreso-modificar').val(alumno.FechaDeIngreso);
                $('#formulario-modificar').show();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    }

    function guardarCambios() {
        var nombre = $('#nombre-modificar').val();
        var programa = $('#programa-modificar').val();
        var fechaIngreso = $('#fecha-ingreso-modificar').val();

        $.ajax({
            url: '/api/alumnos/' + alumnoIdModificar + '/',
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify({AlumnoNombre: nombre, AlumnoPrograma: programa, FechaDeIngreso: fechaIngreso}),
            success: function(response) {
                console.log(response);
                cargarAlumnos();
                $('#formulario-modificar').hide();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    }

    $(document).ready(function() {
        cargarAlumnos();
    });
