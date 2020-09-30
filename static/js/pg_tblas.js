$(document).ready(function () {
    $('#tblmasters').DataTable({
        "processing": true,
        "ajax": "/empleados/salsa",
        "columns":[
            {"data":"Id"},
            { "data":"First_Name"},
            {"data":"Last_Name"},
            {"data":"Email"},
            {"data":"Direccion"},
            {"data":"Distric"}
        ],
        "dom":'Bfrtilp',
        "buttons":[
            {
                "extend":'pdfHtml5',
                "text":'<i class="fas fa-file">PDF</i>',
                "titleAttr":'Exportar a PDF',
                "className":'btn btn-danger'
            },
            {
                "extend":'print',
                "text":'<i class="fas fa-print">Print</i>',
                "titleAttr":'Print',
                "className":'btn btn-info'
            },
        ]
    });

});
