$(function () {
    $('#data tbody').on('click', 'a[rel="search"]', function () {
        $('.tooltip').remove();
        var id = $(this).data('id');
        $('.nav-tabs a[href="#home"]').tab('show');
        $('#tblModules').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            ajax: {
                url: pathname,
                type: 'POST',
                data: {
                    action: 'search_modules', id: id
                },
                dataSrc: ""
            },
            columns: [
                { "data": "name"},
                { "data": "icon"},
                { "data": "image"},
                { "data": "type"},
                { "data": "is_vertical"},
                { "data": "is_visible"},
                { "data": "is_active"},
            ],
            columnDefs: [
                {
                    targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img class="img-fluid mx-auto d-block" src="'+data+'" width="20px" height="20px">';
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return (data != null) ? data.name : data;
                    }
                },
                {
                    targets: [1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<i class="'+data+'" aria-hidden="true"></i>';
                    }
                },
                {
                    targets: [4,5,6],
                    class: 'text-center',
                    orderable: false,
                    data: null,
                    render: function (data, type, row) {
                        if(data){
                            return '<i class="fa fa-check" aria-hidden="true"></i>';
                        }
                        return '<i class="fa fa-times" aria-hidden="true"></i>';
                    }
                },
            ]
        });
        $('#tblPermissions').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            ajax: {
                url: pathname,
                type: 'POST',
                data: {
                    action: 'search_permissions', id: id
                },
                dataSrc: ""
            },
            columns: [
                {"data": "id"},
                {"data": "name"},
                {"data": "codename"},
            ],
        });
        $('#myModalGroup').modal('show');
    });
});