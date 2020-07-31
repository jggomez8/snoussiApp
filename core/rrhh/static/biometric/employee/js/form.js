function startTime() {

    function checkTime(i) {
        return (i < 10) ? "0" + i : i;
    }

    var today = new Date(),
        h = checkTime(today.getHours()),
        m = checkTime(today.getMinutes()),
        s = checkTime(today.getSeconds());
    var hour = h + ":" + m + ":" + s;

    $('#time').html(hour);

    t = setTimeout(function () {
        startTime();
    }, 500);
}

$(function () {
    $('.btn-biometric').on('click', function () {
        var dni = $('input[name="dni"]').val();

        var parameters = {
            'dni': dni,
            'action': 'add',
            'horary': $(this).data('id')
        };

        $.ajax({
            url: pathname,
            data: parameters,
            method: 'POST',
            dataType: 'json',
            success: function (request) {
                if (!request.hasOwnProperty('error')) {
                    alert_sweetalert('success', 'Alerta', 'Asistencia registrada correctamente', function () {
                        location.reload();
                    }, 3000, null);

                    return false;
                }
                message_error(request.error);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                message_error(errorThrown + ' ' + textStatus);
            }
        });
    });

    startTime();
});