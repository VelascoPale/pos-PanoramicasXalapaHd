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
    document.getElementById('form_update').setAttribute('action', '/dashboard/register/user/patch/' + id);
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
    document.getElementById('form_update').setAttribute('action', '/dashboard/register/user/delete/' + id);
}


///Function for edit events 
function edit_event(id, eventName, level){

    document.getElementById('title_window').innerHTML = 'Editar evento';

    ///update data in form
    document.getElementById('idhallName').value = eventName;

       // check radius 
    if (level == 'SELLER') {
        // change propierties
        document.getElementById('idseller').checked = true;
    } else {
        document.getElementById('idadmin').checked = true;
    }


    // desactivate inputs
    document.getElementById('idhallName').disabled = false;

    // change url of form
    document.getElementById('form_update').setAttribute('action', '/dashboard/register/event/patch/' + id);

}

//// function for delete events
function delete_event(id ,eventName, level){

      // change title of window
    document.getElementById('title_window').innerHTML = 'Eliminar evento';
    document.getElementById('btn_form').innerHTML = 'Eliminar ';

    document.getElementById('idhallName').value = eventName;

    // desactivate inputs
    document.getElementById('idhallName').disabled = true;

        // check radius 
    if (level == 'SELLER') {
        // change propierties
        document.getElementById('idseller').checked = true;
    } else {
        document.getElementById('idadmin').checked = true;
    }

    // change url of form
    document.getElementById('form_update').setAttribute('action', '/dashboard/register/event/delete/' + id);

}

////function for update school
function edit_school(id, name, shift, generation, code, level){

    document.getElementById('title_window').innerHTML = 'Editar escuela';

    // update data in form 
    document.getElementById('idschoolName').value = name;
    document.getElementById('inputGroupSelect01').value = shift;
    document.getElementById('idgeneration').value = generation;
    document.getElementById('idcode').value = code;

      // check radius 
    if (level == 'SELLER') {
        // change propierties
        document.getElementById('idseller').checked = true;
    } else {
        document.getElementById('idadmin').checked = true;
    }


    // desactivate inputs
    document.getElementById('idschoolName').disabled = false;
    document.getElementById('inputGroupSelect01').disabled = false;
    document.getElementById('idgeneration').disabled = false;
    document.getElementById('idcode').disabled = false;


    // change url of form
    document.getElementById('form_update').setAttribute('action', '/dashboard/register/school/patch/' + id);
}

function delete_school(id, name, shift, generation, code, level) {

    // change title of window
    document.getElementById('title_window').innerHTML = 'Eliminar escuela';
    document.getElementById('btn_form').innerHTML = 'Eliminar ';

    // update data in form 
    document.getElementById('idschoolName').value = name;
    document.getElementById('inputGroupSelect01').value = shift;
    document.getElementById('idgeneration').value = generation;
    document.getElementById('idcode').value = code;

    // desactivate inputs
    document.getElementById('idschoolName').disabled = true;
    document.getElementById('inputGroupSelect01').disabled = true;
    document.getElementById('idgeneration').disabled = true;
    document.getElementById('idcode').disabled = true;
    

    // check radius 
    if (level == 'SELLER') {
        // change propierties
        document.getElementById('idseller').checked = true;
    } else {
        document.getElementById('idadmin').checked = true;
    }

    // change url of form
    document.getElementById('form_update').setAttribute('action', '/dashboard/register/school/delete/' + id);
}



function edit_client(id, name , lastname, telephone, group){
    document.getElementById('title_window').innerHTML = 'Editar cliente';

    // update data in form 
    document.getElementById('idname').value = name;
    document.getElementById('idlastname').value = lastname;
    document.getElementById('idtelephone').value = telephone;
    document.getElementById('idgroup').value = group;

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
    document.getElementById('idtelephone').disabled = false;
    document.getElementById('idgroup').disabled = false;


    // change url of form
    document.getElementById('form_update').setAttribute('action', '/dashboard/register/client/patch/' + id);

}