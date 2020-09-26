$(document).ready(function () {
    $('#tblmaster').DataTable({
        "processing": true,
        "ajax": "/sopa",
        "columns": [
            { "data": "country_id" },
            { "data": "country" },
            { "data": "last_update" }
        ]
    });

});
