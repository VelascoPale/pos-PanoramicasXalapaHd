// functions for clients_grd page
function add_orderGraduation(idSeller,idClient, idEvent, name, lastname) {

    // change title of window
    document.getElementById('title_window').innerHTML = 'Agregar pedido';
    document.getElementById('btn_form').innerHTML = 'Agregar ';

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

    // disable inputs
    document.getElementById('id_name').setAttribute('readonly','readonly');
    document.getElementById('id_lastname').setAttribute('readonly','readonly');
    document.getElementById('id_cost').setAttribute('readonly','readonly');

}

function edit_client_grd(id, name, id_table, num_photo, _6x9, _8x12, cost, payment, event) {

    // change title of window
    document.getElementById('title_window').innerHTML = 'Editar pedido';
    document.getElementById('btn_form').innerHTML = 'Actualizar';

    // update data in form 
    document.getElementById('id_name').value = name;
    document.getElementById('id_mesa').value = id_table
    document.getElementById('id_foto').value = num_photo;
    document.getElementById('id_6x9').value = _6x9;
    document.getElementById('id_8x12').value = _8x12;
    document.getElementById('id_cost').value = cost;
    document.getElementById('id_payment').value = payment;

    // disable inputs
    document.getElementById('id_6x9').setAttribute('readonly','readonly');
    document.getElementById('id_8x12').setAttribute('readonly','readonly');
    document.getElementById('id_cost').setAttribute('readonly','readonly');

    // change url of form
    document.getElementById('form_update').setAttribute('action', '/update_client/' + event + '/' + id)

}

function delete_client_grd(id, name, id_table, num_photo, _6x9, _8x12, cost, payment, event) {

    // change title of window
    document.getElementById('title_window').innerHTML = 'Eliminar pedido';
    document.getElementById('btn_form').innerHTML = 'Eliminar ';

    // update data in form 
    document.getElementById('id_name').value = name;
    document.getElementById('id_mesa').value = id_table
    document.getElementById('id_foto').value = num_photo;
    document.getElementById('id_6x9').value = _6x9;
    document.getElementById('id_8x12').value = _8x12;
    document.getElementById('id_cost').value = cost;
    document.getElementById('id_payment').value = payment;

    // disable inputs
    document.getElementById('id_name').disabled = true;
    document.getElementById('id_mesa').disabled = true;
    document.getElementById('id_foto').disabled = true;
    document.getElementById('id_6x9').disabled = true;
    document.getElementById('id_8x12').disabled = true;
    document.getElementById('id_cost').disabled = true;
    document.getElementById('id_payment').disabled = true;

    // change url of form
    document.getElementById('form_update').setAttribute('action', '/delete_client/' + event + '/' + id)

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

function sum_6x9(){
    var num_6x9 = parseInt(document.getElementById('_6x9').value);
    num_6x9 += 1;
    document.getElementById('_6x9').value = num_6x9;
    calculate_cost();
}

function rest_6x9(){
    var num_6x9 = parseInt(document.getElementById('_6x9').value);
    num_6x9 -= 1;
     if (num_6x9 < 0){
        num_6x9=0;
    }
    document.getElementById('_6x9').value = num_6x9;
    calculate_cost();
}

function sum_8x12(){
    var num_8x12 = parseInt(document.getElementById('_8x12').value);
    num_8x12 += 1;
    document.getElementById('_8x12').value = num_8x12;
    calculate_cost();
}

function rest_8x12(){
    var num_8x12 = parseInt(document.getElementById('_8x12').value);
    num_8x12 -= 1;
     if (num_8x12 < 0){
        num_8x12=0;
    }
    document.getElementById('_8x12').value = num_8x12;
    calculate_cost();
}