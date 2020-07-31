var fv;

document.addEventListener('DOMContentLoaded', function (e) {
    const form = document.getElementById('frmForm');
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
                name: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                    }
                },
                system_name: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                    }
                },
                icon: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 4,
                        },
                    }
                },
                image: {
                    notEmpty: {},
                    validators: {
                        file: {
                            extension: 'jpeg,jpg,png',
                            type: 'image/jpeg,image/png',
                            maxFiles: 1,
                            message: 'Introduce una imagen válida'
                        }
                    }
                },
                proprietor: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                    }
                },
                email: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 5
                        },
                        regexp: {
                            regexp: /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/i,
                            message: 'El email no es correcto'
                        }
                    }
                },
                mobile: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 1,
                        },
                        digits: {}
                    }
                },
                phone: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 1,
                        },
                        digits: {}
                    }
                },
                address: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 4,
                        }
                    }
                },
                mission: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 4,
                        }
                    }
                },
                vision: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 4,
                        }
                    }
                },
                about_us: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 4,
                        }
                    }
                },
                ruc: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 1,
                        },
                        digits: {},
                    }
                },
                layout: {
                    validators: {
                        notEmpty: {},
                    }
                },
                card: {
                    validators: {
                        notEmpty: {},
                    }
                },
                navbar: {
                    validators: {
                        notEmpty: {},
                    }
                },
                brand_logo: {
                    validators: {
                        notEmpty: {},
                    }
                },
                sidebar: {
                    validators: {
                        notEmpty: {},
                    }
                },
            },
        }
    )
        .on('core.element.validated', function (e) {
            // Validate Tabs
            var tab = e.element.closest('.tab-pane'),
                tabId = tab.getAttribute('id');
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
                $('a[href="#' + tabId + '"][data-toggle="tab"]').parent().find('i').removeClass('fa-times fa-check');
            } else {
                $('a[href="#' + tabId + '"][data-toggle="tab"]').parent().find('i').removeClass('fa-check').addClass('fa-times');
            }
            const iconPlugin = fv.getPlugin('icon');
            const iconElement = iconPlugin && iconPlugin.icons.has(e.element) ? iconPlugin.icons.get(e.element) : null;
            iconElement && (iconElement.style.display = 'none');
        })
        .on('core.validator.validated', function (e) {
            // Validate Tabs
            var tab = e.element.closest('.tab-pane'),
                tabId = tab.getAttribute('id');
            if (!e.result.valid) {
                // Query all messages
                const messages = [].slice.call(form.querySelectorAll('[data-field="' + e.field + '"][data-validator]'));
                messages.forEach((messageEle) => {
                    const validator = messageEle.getAttribute('data-validator');
                    messageEle.style.display = validator === e.validator ? 'block' : 'none';
                });
                $('a[href="#' + tabId + '"][data-toggle="tab"]').parent().find('i').removeClass('fa-check fa-times');
            }
        })
        .on('core.form.valid', function () {
            submit_formdata_with_ajax_form(fv);
        });
});


$(function () {

    $('.select2').select2({
        theme: 'bootstrap4',
        language: "es"
    });

    $('select[name="layout"]')
        .on('change.select2', function () {
            fv.revalidateField('layout');
        });

    $('select[name="template"]')
        .on('change.select2', function () {
            fv.revalidateField('template');
        });

    $('input[name="ruc"]').keypress(function (e) {
        return validate_form_text('numbers', e, null);
    });

    $('input[name="mobile"]').keypress(function (e) {
        return validate_form_text('numbers', e, null);
    });

    $('input[name="phone"]').keypress(function (e) {
        return validate_form_text('numbers', e, null);
    });
});