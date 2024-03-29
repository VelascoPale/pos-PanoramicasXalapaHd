//function ajax for search clients in grd

$(document).ready(function () {

    function ajax_addOrder() {
        $.ajax({
            url: '/dashboard/event/form',
            type: 'POST',
            data: $('form').serialize(),
            success: function (response) {
                $("#table_order").html('');
                $("#table_client").html('');
                var output;
                var alert;
                var idSeller = document.getElementById('idseller').innerHTML;
                var idEvent = document.getElementById('tagEvent').innerHTML;
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
                    } else if (index == 1) {
                        item.forEach(client => {
                            output += "<tr>";
                            output += "<td id='idName" + client['idClient'] + "'>" + client['name'] + "</td>";
                            output += "<td id='idLast" + client['idClient'] + "'>" + client['lastname'] + "</td>";
                            output += "<td class='no_visible'>" + client['telephone'] + "</td>";
                            output += "<td class='no_visible'> " + client['email'] + "</td>";
                            output += "<td>";
                            output += `<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#addOrder" onclick="add_orderGraduation('${idSeller}','${client['idClient']}','${idEvent}','${client['name']}','${client['lastname']}');">Agregar pedido</button>`;
                            output += "</td>";
                            output += "</tr>";
                        });
                        $('#table_client').html(output);
                        output = '';
                    } else if (index == 2) {
                        item.forEach(order => {
                            output += "<tr>";
                            output += "<td>" + document.getElementById('idName' + order['idClient']).innerHTML + "</td>";
                            output += "<td>" + document.getElementById('idLast' + order['idClient']).innerHTML + "</td>";
                            output += "<td class='no_visible'>" + order['numTable'] + "</td>";
                            output += "<td class='no_visible'>" + order['numPhoto'] + "</td>";
                            output += "<td class='no_visible'>" + order['_6x9'] + "</td>";
                            output += "<td class='no_visible'>" + order['_8x12'] + "</td>";
                            output += "<td class='no_visible'>" + order['cost'] + "</td>";
                            output += "<td class='no_visible'>" + order['payment'] + "</td>";
                            output += "<td>";
                            output += `<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#editOrder" onclick="edit_orderGraduation('${order['idSeller']}','${order['idEvent']}','${order['idClient']}','${order['idOrderGraduation']}','${order['idClient']}','${order['idClient']}','${order['numTable']}','${order['numPhoto']}','${order['_6x9']}','${order['_8x12']}','${order['cost']}','${order['payment']}','${order['status']}');">Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            document.getElementById('idSeller').innerHTML = order['idSeller'];
                        });
                        document.getElementById('form_add').reset();
                        $('#table_order').html(output);
                    }
                });

            }
        });
    }

    $('#form_add').submit(function (event) {
        event.preventDefault();
        ajax_addOrder();
        document.getElementById('close_modalAdd').click();
    });

    function ajax_editOrder() {
        $.ajax({
            url: '/dashboard/event/form',
            type: 'PATCH',
            data: $('form').serialize(),
            success: function (response) {
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
                            output += "<tr>";
                            output += "<td>" + document.getElementById('idName' + order['idClient']).innerHTML + "</td>";
                            output += "<td>" + document.getElementById('idLast' + order['idClient']).innerHTML + "</td>";
                            output += "<td class='no_visible'>" + order['numTable'] + "</td>";
                            output += "<td class='no_visible'>" + order['numPhoto'] + "</td>";
                            output += "<td class='no_visible'>" + order['_6x9'] + "</td>";
                            output += "<td class='no_visible'>" + order['_8x12'] + "</td>";
                            output += "<td class='no_visible'>" + order['cost'] + "</td>";
                            output += "<td class='no_visible'>" + order['payment'] + "</td>";
                            output += "<td>";
                            output += `<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#editOrder" onclick="edit_orderGraduation('${order['idSeller']}','${order['idEvent']}','${order['idClient']}','${order['idOrderGraduation']}','${order['idClient']}','${order['idClient']}','${order['numTable']}','${order['numPhoto']}','${order['_6x9']}','${order['_8x12']}','${order['cost']}','${order['payment']}','${order['status']}');">Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            $('#table_order').html(output);
                        });
                    }
                });

            }

        });

    }

    $('#form_send').submit(function (event) {
        event.preventDefault();
        ajax_editOrder();
        document.getElementById('close_modalEdit').click();
    });

    $("#search_client").keyup(function () {
        var name = document.getElementById('search_client').value;
        var event = document.getElementById('tagEvent').innerHTML;
        $.ajax({
            type: "GET",
            url: '/dashboard/event/form/search',
            data: { event, name },
            success: function (response) {
                $("#table_order").html('');
                $("#table_client").html('');
                var output;
                var alert;
                var idSeller = document.getElementById('idseller').innerHTML;
                var idEvent = document.getElementById('tagEvent').innerHTML;
                response.forEach(function each(item, index) {
                    if (index == 0) {
                        item.forEach(client => {
                            output += "<tr>";
                            output += "<td id='idName" + client['idClient'] + "'>" + client['name'] + "</td>";
                            output += "<td id='idLast" + client['idClient'] + "'>" + client['lastname'] + "</td>";
                            output += "<td class='no_visible'>" + client['telephone'] + "</td>";
                            output += "<td class='no_visible'> " + client['email'] + "</td>";
                            output += "<td>";
                            output += `<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#addOrder" onclick="add_orderGraduation('${idSeller}','${client['idClient']}','${idEvent}','${client['name']}','${client['lastname']}');">Agregar pedido</button>`;
                            output += "</td>";
                            output += "</tr>";
                        });
                        $('#table_client').html(output);
                        output = '';
                    } else if (index == 1) {
                        item.forEach(order => {
                            output += "<tr>";
                            output += "<td>" + order['name'] + "</td>";
                            output += "<td>" + order['lastname'] + "</td>";
                            output += "<td class='no_visible'>" + order['numTable'] + "</td>";
                            output += "<td class='no_visible'>" + order['numPhoto'] + "</td>";
                            output += "<td class='no_visible'>" + order['_6x9'] + "</td>";
                            output += "<td class='no_visible'>" + order['_8x12'] + "</td>";
                            output += "<td class='no_visible'>" + order['cost'] + "</td>";
                            output += "<td class='no_visible'>" + order['payment'] + "</td>";
                            output += "<td>";
                            output += `<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#editOrder" onclick="edit_orderGraduation('${order['idSeller']}','${order['idEvent']}','${order['idClient']}','${order['idOrderGraduation']}','${order['name']}','${order['lastname']}','${order['numTable']}','${order['numPhoto']}','${order['_6x9']}','${order['_8x12']}','${order['cost']}','${order['payment']}','${order['status']}');">Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            document.getElementById('idSeller').innerHTML = order['idSeller'];
                        });
                        document.getElementById('form_add').reset();
                        $('#table_order').html(output);
                    }
                });

            }
        });
    });

});

function filter_sales() {

    var filter = document.getElementById('filter_sales').value;

    $.ajax({
        url: '/dashboard/event/form' + filter,
        type: 'GET',
        success: function (response) {
            $('#table_order').html('');
            var idSeller = document.getElementById('idseller').innerHTML;
            var output;
            var num6x9 = 0, num8x12 = 0;
            if (filter.endsWith('my')) {
                response.forEach(order => {
                    output += "<tr>";
                    output += "<td>" + document.getElementById('idName' + order['idClient']).innerHTML + "</td>";
                    output += "<td>" + document.getElementById('idLast' + order['idClient']).innerHTML + "</td>";
                    output += "<td class='no_visible'>" + order['numTable'] + "</td>";
                    output += "<td class='no_visible'>" + order['numPhoto'] + "</td>";
                    output += "<td class='no_visible'>" + order['_6x9'] + "</td>";
                    output += "<td class='no_visible'>" + order['_8x12'] + "</td>";
                    output += "<td class='no_visible'>" + order['cost'] + "</td>";
                    output += "<td class='no_visible'>" + order['payment'] + "</td>";
                    output += "<td>";
                    output += `<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#editOrder" onclick="edit_orderGraduation('${order['idSeller']}','${order['idEvent']}','${order['idClient']}','${order['idOrderGraduation']}','${order['idClient']}','${order['idClient']}','${order['numTable']}','${order['numPhoto']}','${order['_6x9']}','${order['_8x12']}','${order['cost']}','${order['payment']}','${order['status']}');">Editar</button>`;
                    output += "</td>";
                    output += "</tr>";
                    document.getElementById('idSeller').innerHTML = order['idSeller'];
                    if (idSeller == order['idSeller']) {
                        num8x12 += order['_8x12'];
                        num6x9 += order['_6x9'];
                    }
                });
                output += "<tr>";
                output += "<td colspan='4'> TOTAL DE VENTAS: </td>";
                output += "<td class='no_visible'>" + num6x9 + "</td>";
                output += "<td class='no_visible'>" + num8x12 + "</td>";
                output += "<td colspan='3' class='no_visible'> </td>";
                output += "</tr>";
            }else{
                response.forEach(order => {
                    output += "<tr>";
                    output += "<td>" + document.getElementById('idName' + order['idClient']).innerHTML + "</td>";
                    output += "<td>" + document.getElementById('idLast' + order['idClient']).innerHTML + "</td>";
                    output += "<td class='no_visible'>" + order['numTable'] + "</td>";
                    output += "<td class='no_visible'>" + order['numPhoto'] + "</td>";
                    output += "<td class='no_visible'>" + order['_6x9'] + "</td>";
                    output += "<td class='no_visible'>" + order['_8x12'] + "</td>";
                    output += "<td class='no_visible'>" + order['cost'] + "</td>";
                    output += "<td class='no_visible'>" + order['payment'] + "</td>";
                    output += "<td>";
                    output += `<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#editOrder" onclick="edit_orderGraduation('${order['idSeller']}','${order['idEvent']}','${order['idClient']}','${order['idOrderGraduation']}','${order['idClient']}','${order['idClient']}','${order['numTable']}','${order['numPhoto']}','${order['_6x9']}','${order['_8x12']}','${order['cost']}','${order['payment']}','${order['status']}');">Editar</button>`;
                    output += "</td>";
                    output += "</tr>";
                    document.getElementById('idSeller').innerHTML = order['idSeller'];
                });
            }
            document.getElementById('form_add').reset();
            $('#table_order').html(output);
        }
    });
}