//function ajax for search clients in grd
$(document).ready(function () {
    var event = document.getElementById('table_name').innerHTML;
    var table_initial = document.getElementById('table_initial');
    var new_table = document.getElementById('new_table');

    $("#search").keyup(function () {
        $("#table").html('');
        var search = document.getElementById('search').value;
        $.ajax({
            method: "GET",
            url: "/search_client/" + event,
            data: { text: document.getElementById('search').value },
            success: function (clients) {
                var output;
                clients.forEach(client => {
                    output += "<tr>";
                    output += "<td>" + client[1] + "</td>";
                    output += "<td class='no_visible'>" + client[2] + "</td>";
                    output += "<td class='no_visible'>" + client[3] + "</td>";
                    output += "<td class='no_visible'>" + client[4] + "</td>";
                    output += "<td class='no_visible'>" + client[5] + "</td>";
                    output += "<td class='no_visible'>" + client[6] + "</td>";
                    output += "<td class='no_visible'>" + client[7] + "</td>";
                    output += "<td>";
                    output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#exampleModalScrollable' onclick='edit_client_grd("${client[0]}","${client[1]}","${client[2]}","${client[3]}","${client[4]}","${client[5]}","${client[6]}","${client[7]}","${event}")'>Editar</button>`;
                    output += `<button type='button' class='btn btn-danger btn-sm ml-1' data-toggle='modal' data-target='#exampleModalScrollable' onclick='delete_client_grd("${client[0]}","${client[1]}","${client[2]}","${client[3]}","${client[4]}","${client[5]}","${client[6]}","${client[7]}","${event}")'>Eliminar</button>`;
                    output += "</td>";
                    output += "</tr>";
                });
                $('#table').html(output);
            }
        });
    });
});