var fv;
var input_isvertical;
var input_action;
var select_type;

document.addEventListener('DOMContentLoaded', function (e) {
    const form = document.getElementById('frmForm');
    fv = FormValidation.formValidation(form, {
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
                url: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                        remote: {
                            url: pathname,
                            data: function () {
                                return {
                                    obj: form.querySelector('[name="url"]').value,
                                    type: 'url',
                                    action: 'validate_data'
                                };
                            },
                            message: 'La dirección url ya se encuentra registrada',
                            method: 'POST'
                        }
                    }
                },
                name: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                    }
                },
                icon: {
                    validators: {}
                },
                description: {
                    validators: {}
                },
                image: {
                    validators: {
                        file: {
                            extension: 'jpeg,jpg,png',
                            type: 'image/jpeg,image/png',
                            maxFiles: 1,
                            message: 'Introduce una imagen válida'
                        }
                    }
                },
                type: {
                    enabled: false,
                    validators: {
                        notEmpty: {},
                    }
                },
                content_type: {
                    validators: {
                        //notEmpty: {},
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
            // $.each($(form).serializeArray(), function () {
            //     result.append(this.name, this.value);
            // });
            // result.forEach(function (key, value) {
            //     console.log(key);
            //     console.log(value);
            // });
            submit_formdata_with_ajax_form(fv);
        });
});

$(function () {

    input_isvertical = $('input[name="is_vertical"]');
    input_action = $('input[name="action"]');
    select_type = $('select[name="type"]');

    $('.select2').select2({
        theme: 'bootstrap4',
        language: "es"
    });

    input_isvertical.on('change', function () {
        select_type.prop('disabled', false);
        var action = this.checked;
        if (!action) {
            fv.disableValidator('type');
            select_type.val('').trigger('change');
        } else {
            fv.enableValidator('type');
        }
        fv.revalidateField('type');
        select_type.prop('disabled', !action).val('');
    });

    select_type.on('change.select2', function () {
        fv.revalidateField('type');
    });
});







