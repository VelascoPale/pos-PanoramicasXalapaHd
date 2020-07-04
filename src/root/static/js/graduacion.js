// functions for clients_grd pages
function add_orderGraduation(idSeller, idClient, idEvent, name, lastname) {

    // update data in form 
    document.getElementById('id_name').value = name;
    document.getElementById('id_lastname').value = lastname;
    document.getElementById('idSeller').value = idSeller;
    document.getElementById('idClient').value = idClient;
    document.getElementById('idEvent').value = idEvent;
    document.getElementById('id_mesa').value = '';
    document.getElementById('id_foto').value = '';
    document.getElementById('id_6x9').value = '';
    document.getElementById('id_8x12').value = '';
    document.getElementById('id_cost').value = '';
    document.getElementById('id_payment').value = '';

    // add attribs
    document.getElementById('id_name').setAttribute('readonly', 'readonly');
    document.getElementById('id_lastname').setAttribute('readonly', 'readonly');
    document.getElementById('id_cost').setAttribute('readonly', 'readonly');
    document.getElementById('select_status').setAttribute('disabled', 'disabled')
    document.getElementById('En_proceso').setAttribute('selected', 'selected');
    document.getElementById('Impresion').removeAttribute('selected');
    document.getElementById('Entregado').removeAttribute('selected');
    
}

function edit_orderGraduation(idSeller, idEvent, idClient, idOrder, name, lastname, id_table, num_photo, _6x9, _8x12, cost, payment, status) {

    // update data in form 
    document.getElementById('idSellerEdit').value = idSeller;
    document.getElementById('idClientEdit').value = idClient;
    document.getElementById('idEventEdit').value = idEvent;
    document.getElementById('idOrderEdit').value = idOrder;
    document.getElementById('id_nameEdit').value = name;
    document.getElementById('id_lastnameEdit').value = lastname;
    document.getElementById('id_mesaEdit').value = id_table
    document.getElementById('id_fotoEdit').value = num_photo;
    document.getElementById('id_6x9Edit').value = _6x9;
    document.getElementById('id_8x12Edit').value = _8x12;
    document.getElementById('id_costEdit').value = cost;
    document.getElementById('id_paymentEdit').value = payment;

    // disable inputs
    document.getElementById('id_nameEdit').setAttribute('readonly', 'readonly');
    document.getElementById('id_lastnameEdit').setAttribute('readonly', 'readonly');
    document.getElementById('id_costEdit').setAttribute('readonly', 'readonly');
    document.getElementById('select_statusEdit').removeAttribute('disabled')

    if (status == 'En_proceso') {
        document.getElementById('Impresion').removeAttribute('selected');
        document.getElementById('Entregado').removeAttribute('selected');
    } else if (status == 'Impresion') {
        document.getElementById('En_proceso').removeAttribute('selected');
        document.getElementById('Entregado').removeAttribute('selected');
    } else if (status == 'Entregado') {
        document.getElementById('En_proceso').removeAttribute('selected');
        document.getElementById('Impresion').removeAttribute('selected');
    }
    document.getElementById(`${status}`).setAttribute('selected', 'selected');

   
}

function addClientOrder(){
    document.getElementById('form_add').reset();
    document.getElementById('idClient').value = 0;

    document.getElementById('id_name').removeAttribute('readonly');
    document.getElementById('id_lastname').removeAttribute('readonly');
}

// functions of support
function calculate_cost() {
    var _6x9 = parseInt(document.getElementById('_6x9').value);
    var _8x12 = parseInt(document.getElementById('_8x12').value);
    var cost_6x9 = 100;
    var cost_8x12 = 200;
    var final_cost = 0;

    // calculate final_cost
    if (_6x9 > 0 || _8x12 > 0) {
        if (_8x12 == 1 && _6x9 > 0) {
            final_cost = ((_6x9 * (cost_6x9 - 30)) + (_8x12 * (cost_8x12)));
        } else if (_8x12 >= 2 && _6x9 > 0) {
            final_cost = ((_6x9 * (cost_6x9 - 30)) + (_8x12 * (cost_8x12 - 50)));
        } else if (_8x12 > 0 || _6x9 > 0) {
            final_cost = (cost_6x9 * _6x9) + (cost_8x12 * _8x12);
        }
    } else {
        final_cost = 0;
    }

    //print values in form
    if (_6x9 > 0 || _8x12 > 0) {
        document.getElementById('id_8x12').value = _8x12;
        document.getElementById('id_6x9').value = _6x9;
        document.getElementById('id_cost').value = final_cost;
    } else {
        document.getElementById('id_8x12').value = '';
        document.getElementById('id_6x9').value = '';
        document.getElementById('id_cost').value = '';
    }


    //replace value in cost
    document.getElementById('cost_ind').innerHTML = "El costo total es de: $ " + final_cost;
}

function reset_cost() {
    document.getElementById('_6x9').value = 0;
    document.getElementById('_8x12').value = 0;
    document.getElementById('cost_ind').innerHTML = 'El costo total es de: $ 0';
}

function sum_6x9() {
    var num_6x9 = parseInt(document.getElementById('_6x9').value);
    num_6x9 += 1;
    document.getElementById('_6x9').value = num_6x9;
    calculate_cost();
}

function rest_6x9() {
    var num_6x9 = parseInt(document.getElementById('_6x9').value);
    num_6x9 -= 1;
    if (num_6x9 < 0) {
        num_6x9 = 0;
    }
    document.getElementById('_6x9').value = num_6x9;
    calculate_cost();
}

function sum_8x12() {
    var num_8x12 = parseInt(document.getElementById('_8x12').value);
    num_8x12 += 1;
    document.getElementById('_8x12').value = num_8x12;
    calculate_cost();
}

function rest_8x12() {
    var num_8x12 = parseInt(document.getElementById('_8x12').value);
    num_8x12 -= 1;
    if (num_8x12 < 0) {
        num_8x12 = 0;
    }
    document.getElementById('_8x12').value = num_8x12;
    calculate_cost();
}