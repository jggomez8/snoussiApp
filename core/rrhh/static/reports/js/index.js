var tblEmployee;

function format(symptoms) {
    var html = '<b>Ficha de ' + symptoms.user.full_name + '</b>';
    html += '<hr>';
    html += '<p><b>Estado: </b><span class="text-danger">Inactivo por contagio</span></p>';
    html += '<hr>';
    html += '<h5>Datos Personales</h5>';
    html += '<p><b>Genero: </b>' + symptoms.gender.name + '<br>';
    html += '<b>Edad: </b>' + symptoms.age + '<br>';
    html += '<b>Dependencia: </b>' + symptoms.dependence.name + '<br></p>';
    html += '<hr>';
    html += '<h5>Detención</h5>';

    $.each(symptoms.infections, function (key, value) {
        html += '<p><b>Detención caso sospechoso:</b> ' + value.date_joined + '<br>';
        html += '<p><b>Pruebas: </b><br>';
        html += '<b>Temperatura corporal: </b> ' + value.body_temperature + '<br>';
        html += '<b>Falta de aire: </b> ' + (value.air_death === 1 ? 'Si' : 'No') + '<br>';
        html += '<b>Tos seca: </b> ' + (value.dry_cough === 1 ? 'Si' : 'No') + '<br>';
        html += '<b>Malestar intestinal: </b> ' + (value.intestinal_discomfort === 1 ? 'Si' : 'No') + '<br>';
        html += '<b>Dolor de cabeza: </b> ' + (value.headache === 1 ? 'Si' : 'No') + '<br>';
        html += '<b>Perdida de gusto: </b> ' + (value.lost_taste === 1 ? 'Si' : 'No') + '<br>';
        html += '<b>Perdida de olfato: </b> ' + (value.lost_olfato === 1 ? 'Si' : 'No') + '<br></p>';
    });

    html += '<h5>Cerco Epidemiológico</h5>';
    html += '<p><b>Dependencia restringida: </b> ' + symptoms.dependence.name + '<br>';
    html += '<b>Cantidad de empleados aislados: </b> ' + symptoms.isolated_employees + '<br>';
    html += '<b>Núcleo Familiar aislado: </b> ' + symptoms.cant_familiar + '<br>';
    html += '<b>Total:</b> ' + symptoms.cant_total + ' personas contagiadas que mantienen vinculo con el contagiado<br></p>';
    return html;
}

function getData() {
    $.ajax({
        url: pathname,
        data: {
            'action': 'personal_infected'
        },
        method: 'POST',
        dataType: 'json',
        success: function (request) {
            if (!request.hasOwnProperty('error')) {
                console.log(request);
                $('.infected').html(request.infected);
                $('.epidemiological_fence').html(request.epidemiological_fence);
                setTableInfected(request.table);
                setTableNotInfected(request.notInfected);
                return false;
            }
            message_error(request.error);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            message_error(errorThrown + ' ' + textStatus);
        }
    });

    function setTableInfected(data) {
        tblEmployee = $('#tblEmployee').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: data,
            columns: [
                {data: "user.full_name"},
                {data: "gender.name"},
                {data: "age"},
                {data: "dependence.name"},
                {data: "id"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    render: function (data, type, row) {
                        var buttons = '<a class="btn btn-secondary btn-xs btn-flat" rel="det"><i class="fas fa-bars"></i> Ver más</a>';
                        buttons += ' <a class="btn btn-success btn-xs btn-flat" rel="reintegrate"><i class="fas fa-user-check"></i> Reintegrar empleado</a>';
                        return buttons;
                    }
                },
            ]
        });
    }

    function setTableNotInfected(data) {
        $('#tblNotInfected').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: data,
            columns: [
                {data: "user.full_name"},
                {data: "gender.name"},
                {data: "age"},
                {data: "dependence.name"},
            ],
            columnDefs: []
        });
    }
}

function getData2() {
    $('#tblEmployeeNotInfected').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,

        columns: [
            {data: "user.full_name"},
            {data: "gender.name"},
            {data: "age"},
            {data: "dependence.name"},
        ],
        columnDefs: [
        ]
    });
}

$(function () {

    getData();

    $('#tblEmployee tbody')
        .on('click', 'a[rel="det"]', function () {
            var cell = tblEmployee.cell($(this).closest('td, li')).index();
            var data = tblEmployee.row(cell.row).data();

            var tr = $(this).closest('tr');
            var row = tblEmployee.row(tr);

            if (row.child.isShown()) {
                row.child.hide();
                tr.removeClass('shown');
            } else {
                row.child(format(data)).show();
                tr.addClass('shown');
            }

        })
        .on('click', 'a[rel="reintegrate"]', function () {
            var cell = tblEmployee.cell($(this).closest('td, li')).index();
            var data = tblEmployee.row(cell.row).data();
            submit_with_ajax('Alerta', '¿Estas seguro de reintegrar al empleado?', pathname, {
                'action': 'reintegrate',
                'id': data.id,
            }, function () {
                alert_sweetalert('success', 'Alerta', 'Empleado reintegrado correctamente', function () {
                    location.reload();
                })
            }, 10000, null);

        })
});
