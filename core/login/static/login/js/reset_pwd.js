document.addEventListener('DOMContentLoaded', function (e) {
    const form = document.getElementById('frmResetPassword');
    const fv = FormValidation.formValidation(form, {
            locale: 'es_ES',
            localization: FormValidation.locales.es_ES,
            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                submitButton: new FormValidation.plugins.SubmitButton(),
                bootstrap: new FormValidation.plugins.Bootstrap(),
                excluded: new FormValidation.plugins.Excluded(),
                icon: new FormValidation.plugins.Icon({
                    valid: 'fa fa-check',
                    invalid: 'fa fa-times',
                    validating: 'fa fa-refresh',
                }),
            },
            fields: {
                username: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2
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
            var submitButton = fv.form.querySelector('[type="submit"]');
            var parameters = $(fv.form).serializeArray();
            $.confirm({
                theme: 'material',
                title: 'Confirmación',
                icon: 'fas fa-envelope',
                content: '¿Esta seguro de resetear tu contraseña?',
                columnClass: 'small',
                typeAnimated: true,
                cancelButtonClass: 'btn-primary',
                draggable: true,
                dragWindowBorder: false,
                buttons: {
                    info: {
                        text: "Si",
                        btnClass: 'btn-primary',
                        action: function () {
                            $.ajax({
                                url: pathname,
                                data: parameters,
                                method: 'POST',
                                dataType: 'json',
                                beforeSend: function () {
                                    loading_message('Enviando correo...');
                                },
                                success: function (request) {
                                    if (!request.hasOwnProperty('error')) {
                                        location.href = fv.form.getAttribute('data-url');
                                        return false;
                                    }
                                    message_error(request.error);
                                },
                                error: function (jqXHR, textStatus, errorThrown) {
                                    message_error(errorThrown + ' ' + textStatus);
                                },
                                complete: function () {
                                    $.LoadingOverlay('hide');
                                }
                            });
                        }
                    },
                    danger: {
                        text: "No",
                        btnClass: 'btn-red',
                        action: function () {
                            submitButton.removeAttribute('disabled');
                        }
                    },
                }
            });
        });
});

