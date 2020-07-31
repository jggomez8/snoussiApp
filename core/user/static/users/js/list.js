var form;
var fv;

document.addEventListener('DOMContentLoaded', function (e) {
    form = document.getElementById('frmChangePasswordByUser');
    fv = FormValidation.formValidation(form, {
            locale: 'es_ES',
            localization: FormValidation.locales.es_ES,
            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                submitButton: new FormValidation.plugins.SubmitButton(),
                bootstrap: new FormValidation.plugins.Bootstrap(),
                icon: new FormValidation.plugins.Icon({
                    valid: 'fa fa-check',
                    invalid: 'fa fa-times',
                    validating: 'fa fa-refresh',
                }),
            },
            fields: {
                password: {
                    validators: {
                        notEmpty: {
                            message: 'El password es requerido'
                        },
                    }
                },
            },
        }
    )
        .on('core.element.validated', function (e) {
            if (e.valid) {
                const groupEle = FormValidation.utils.closest(e.element, '.form-group');
                if (groupEle) {
                    FormValidation.utils.classSet(groupEle, {
                        'has-success': false,
                    });
                }
                FormValidation.utils.classSet(e.element, {
                    'is-valid': false,
                });
            }
            const iconPlugin = fv.getPlugin('icon');
            const iconElement = iconPlugin && iconPlugin.icons.has(e.element) ? iconPlugin.icons.get(e.element) : null;
            iconElement && (iconElement.style.display = 'none');
        })
        .on('core.validator.validated', function (e) {
            if (!e.result.valid) {
                const messages = [].slice.call(form.querySelectorAll('[data-field="' + e.field + '"][data-validator]'));
                messages.forEach((messageEle) => {
                    const validator = messageEle.getAttribute('data-validator');
                    messageEle.style.display = validator === e.validator ? 'block' : 'none';
                });
            }
        })
        .on('core.form.valid', function () {
            submit_with_ajax('Notificación',
                '¿Estas seguro de cambiar la clave?',
                pathname,
                {
                    'id': $('#id_pass').val(),
                    'action': 'change_password',
                    'password': $('input[name="password"]').val()
                },
                function () {
                    location.href = pathname;
                });
        });
});

$(function () {

    $('#data tbody').on('click', 'a[rel]', function () {
        var td = table.cell($(this).closest('td, li')).index(),
            rows = table.row(td.row).data(),
            rel = $(this).attr('rel'),
            id = rows[0];

        switch (rel) {
            case 'reset_password':
                submit_with_ajax('Notificación',
                    '¿Estas seguro de resetear la clave?',
                    pathname, {id: id, action: rel},
                    function () {
                        location.reload();
                    }
                );
                break;
            case 'login_with_user':
                submit_with_ajax('Notificación',
                    '¿Estas seguro de iniciar sesión con este usuario?',
                    pathname, {id: id, action: rel},
                    function () {
                        location.href = '/';
                    },
                );
                break;
            case 'search_access':
                $('#tblAccessUsers').DataTable({
                    destroy: true,
                    responsive: true,
                    autoWidth: false,
                    ajax: {
                        url: pathname,
                        type: 'POST',
                        data: {
                            action: rel, id: id
                        },
                        dataSrc: ""
                    },
                    columns: [
                        {"data": "id"},
                        {"data": "date_joined"},
                        {"data": "hour"},
                        {"data": "localhost"},
                        {"data": "hostname"},
                    ],
                    columnDefs: [
                        {orderable: false, targets: ['_all']}
                    ]
                });
                $('#myModalAccessUsers').modal('show');
                break;
            case 'search_groups':
                $('#tblProfiles').DataTable({
                    destroy: true,
                    responsive: true,
                    autoWidth: false,
                    ajax: {
                        url: pathname,
                        type: 'POST',
                        data: {
                            action: rel, id: id
                        },
                        dataSrc: ""
                    },
                    columns: [
                        {"data": "id"},
                        {"data": "name"},
                    ]
                });
                $('#myModalProfile').modal('show');
                break;
            case 'change_password':
                $('#id_pass').val(id);
                $('#myModalChangePasswordByUser').modal('show');
                break;
        }
    });

    /*Validate Form */

    $('#myModalChangePasswordByUser').on('hidden.bs.modal', function () {
        fv.resetForm(true);
    });
});

