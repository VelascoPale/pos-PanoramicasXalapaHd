// funcions for register_members page
function edit_user(id, name, lastname, adress, level) {

    // change title of window
    document.getElementById('title_window').innerHTML = 'Editar usuario';

    // update data in form 
    document.getElementById('idname').value = name;
    document.getElementById('idlastname').value = lastname;
    document.getElementById('idadress').value = adress;

    // check radius 
    if (level == 'SELLER') {
        // change propierties
        document.getElementById('idseller').checked = true;
    } else {
        document.getElementById('idadmin').checked = true;
    }

    // desactivate inputs
    document.getElementById('idname').disabled = false;
    document.getElementById('idlastname').disabled = false;
    document.getElementById('idadress').disabled = false;
    document.getElementById('idpassword').disabled = false;
    document.getElementById('idseller').disabled = false;
    document.getElementById('idadmin').disabled = false;

    // change url of form
    document.getElementById('form_update').setAttribute('action', '/update_member/' + id);

}

function delete_user(id, name, lastname, adress, level) {

    // change title of window
    document.getElementById('title_window').innerHTML = 'Eliminar usuario';
    document.getElementById('btn_form').innerHTML = 'Eliminar ';

    // update data in form 
    document.getElementById('idname').value = name;
    document.getElementById('idlastname').value = lastname;
    document.getElementById('idadress').value = adress;

    // desactivate inputs
    document.getElementById('idname').disabled = true;
    document.getElementById('idlastname').disabled = true;
    document.getElementById('idadress').disabled = true;
    document.getElementById('idpassword').disabled = true;
    document.getElementById('idseller').disabled = true;
    document.getElementById('idadmin').disabled = true;

    // check radius 
    if (level == 'SELLER') {
        // change propierties
        document.getElementById('idseller').checked = true;
    } else {
        document.getElementById('idadmin').checked = true;
    }

    // change url of form
    document.getElementById('form_update').setAttribute('action', '/delete_member/' + id);

}



