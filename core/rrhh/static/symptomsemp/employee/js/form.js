var tblSymptoms;

function getDataSymptoms(data) {
    tblSymptoms = $('#tblSymptoms').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        data: data,
        columns: [
            {data: "name"},
            {data: "state"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                render: function (data, type, row) {
                    var checked = row.state === 1 ? ' checked' : '';
                    var html = '<div class="checkbox">';
                    html += '<label><input type="checkbox" name="state" value="" ' + checked + '></label></div>';
                    return html;
                }
            },
        ]
    });
}

document.addEventListener('DOMContentLoaded', function (e) {
    const form = document.getElementById('frmForm');
    const fv = FormValidation.formValidation(form, {
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
                temperature: {
                    validators: {
                        notEmpty: {},
                        digits: {}
                    }
                }
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
            var symptoms = tblSymptoms.rows().rows().data().toArray();
            symptoms.push({
                'key': 'temperatura_corporal',
                'name': 'Temperatura corporal',
                'state': 1,
                'cant': $('input[name="temperature"]').val()
            });

            submit_with_ajax('Notificación',
                '¿Estas seguro de realizar la siguiente acción?',
                pathname,
                {
                    'action': $('#action').val(),
                    'symptoms': JSON.stringify(symptoms)
                },
                function () {
                    location.href = form.getAttribute('data-url');
                }
            );
        });
});

$(function () {

    $('input[name="temperature"]').keypress(function (e) {
        return validate_form_text('numbers', e, null);
    });

    $('#tblSymptoms tbody')
        .on('change', 'input[name="state"]', function () {
            var td = tblSymptoms.cell($(this).closest('td, li')).index(),
                row = tblSymptoms.row(td.row).data();
            row.state = this.checked ? 1 : 0;
        })
});