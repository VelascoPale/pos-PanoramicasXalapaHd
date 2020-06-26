//function ajax for search clients in grd
$(document).ready(function () {

    function ajax_client(){
        $.ajax({
            url:'/dashboard/register/client/add',
            type:'POST',
            data:$('form').serialize(),
            success: function(clients){
                console.log(clients)
                $("#table").html('');
                var output;
                clients.forEach(client => {
                    console.log(client['name']);
                    output += "<tr>";
                    output += "<td>" + client['name'] + "</td>";
                    output += "<td class='no_visible'>" + client['lastname'] + "</td>";
                    output += "<td class='no_visible'>" + client['telephone'] + "</td>";
                    output += "<td class='no_visible'>" + client['email'] + "</td>";
                    output += "<td class='no_visible'>" + client['idSchool'] + "</td>";
                    output += "<td class='no_visible'>" + client['group'] + "</td>";
                    output += "<td>";
                    output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#exampleModalScrollable' onclick='edit_client_grd("${client[0]}","${client[1]}","${client[2]}","${client[3]}","${client[4]}","${client[5]}","${client[6]}","${client[7]}","${event}")'>Editar</button>`;
                    //output += `<button type='button' class='btn btn-danger btn-sm ml-1' data-toggle='modal' data-target='#exampleModalScrollable' onclick='delete_client_grd("${client[0]}","${client[1]}","${client[2]}","${client[3]}","${client[4]}","${client[5]}","${client[6]}","${client[7]}","${event}")'>Eliminar</button>`;
                    output += "</td>";
                    output += "</tr>";
                });
                $('#table').html(output);
            }
        });
    }

    function clear_form(){
        $('#clearForm').click(function(event){
            $('#register-form')[0].reset();
        });
    }

    $('#register-form').submit(function(event){
        event.preventDefault();
        clear_form();
        ajax_client();
    });

});