//function ajax for search clients in grd
$(document).ready(function () {

    function ajax_addOrder() {
        $.ajax({
            url: '/dashboard/event/form',
            type: 'POST',
            data: $('form').serialize(),
            success: function (response) {
                //console.log(response)
                $("#table_order").html('');
                var output;
                var alert;
                response.forEach(function each(item, index) {
                    if (index == 0) {
                        alert = '';
                        alert += `<div class="alert ${item['type']} alert-dismissible fade show mt-3 fixed-bottom col-6 col-lg-6" role="alert" id="alerts">`;
                        alert += `${item['text']}`;
                        alert += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">';
                        alert += '<span aria-hidden="true">&times;</span>';
                        alert += '</button>';
                        alert += '</div>';
                        $('#alerts').html(alert);
                    } else {
                        item.forEach(order => {
                            console.log(order);
                            output += "<tr>";
                            output += "<td>" + order['idclient'] + "</td>";
                            output += "<td class='no_visible'>" + order['idclient'] + "</td>";
                            output += "<td class='no_visible'>" + order['numTable'] + "</td>";
                            output += "<td class='no_visible'>" + order['numPhoto'] + "</td>";
                            output += "<td class='no_visible'>" + order['_6x9'] + "</td>";
                            output += "<td class='no_visible'>" + order['_8x12'] + "</td>";
                            output += "<td class='no_visible'>" + order['cost'] + "</td>";
                            output += "<td class='no_visible'>" + order['payment'] + "</td>";
                            output += "<td>";
                            output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#exampleModalScrollable' onclick='edit_client_grd("${order[0]}","${order[1]}","${order[2]}","${order[3]}","${order[4]}","${order[5]}","${order[6]}","${order[7]}","${event}")'>Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            $('#table_order').html(output);
                        });
                    }
                });

            }
        });
    }

    $('#form_add').submit(function(event) {
        event.preventDefault();
        ajax_addOrder();
        document.getElementById('close_modal').click();
    });

    function ajax_editOrder(){
        $.ajax({
            url: '/dashboard/event/form/patch',
            type: 'POST',
            data: $('form').serialize(),
            success: function (response) {
                //console.log(response)
                $("#table_order").html('');
                var output;
                var alert;
                response.forEach(function each(item, index) {
                    if (index == 0) {
                        alert = '';
                        alert += `<div class="alert ${item['type']} alert-dismissible fade show mt-3 fixed-bottom col-6 col-lg-6" role="alert" id="alerts">`;
                        alert += `${item['text']}`;
                        alert += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">';
                        alert += '<span aria-hidden="true">&times;</span>';
                        alert += '</button>';
                        alert += '</div>';
                        $('#alerts').html(alert);
                    } else {
                        item.forEach(order => {
                            console.log(order);
                            output += "<tr>";
                            output += "<td>" + order['idclient'] + "</td>";
                            output += "<td class='no_visible'>" + order['idclient'] + "</td>";
                            output += "<td class='no_visible'>" + order['numTable'] + "</td>";
                            output += "<td class='no_visible'>" + order['numPhoto'] + "</td>";
                            output += "<td class='no_visible'>" + order['_6x9'] + "</td>";
                            output += "<td class='no_visible'>" + order['_8x12'] + "</td>";
                            output += "<td class='no_visible'>" + order['cost'] + "</td>";
                            output += "<td class='no_visible'>" + order['payment'] + "</td>";
                            output += "<td>";
                            output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#exampleModalScrollable' onclick='edit_client_grd("${order[0]}","${order[1]}","${order[2]}","${order[3]}","${order[4]}","${order[5]}","${order[6]}","${order[7]}","${event}")'>Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            $('#table_order').html(output);
                        });
                    }
                });

            }

        });
    }

    $('#form_send').submit(function(event) {
        event.preventDefault();
        ajax_editOrder();
        document.getElementById('close_modal').click();
    });

    /*    $("#search").keyup(function () {
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
    */

});