//function ajax for search clients in grd
$(document).ready(function () {

    function ajax_client(){
        $.ajax({
            url:'/dashboard/register/client',
            type:'POST',
            data:$('form').serialize(),
            success: function(response){
                //console.log(response)
                $("#table").html('');
                var output;
                var alert;
                response.forEach(function each(item, index){
                    if (index==0){
                        alert = '';
                        alert += `<div class="alert ${item['type']} alert-dismissible fade show mt-3 fixed-bottom col-6 col-lg-6" role="alert" id="alerts">`;
                        alert += `${item['text']}`;
                        alert += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">';
                        alert += '<span aria-hidden="true">&times;</span>';
                        alert += '</button>';
                        alert += '</div>';
                        $('#alerts').html(alert);
                    }else{
                        item.forEach(client => {
                            output += "<tr>";
                            output += "<td>" + client['name'] + "</td>";
                            output += "<td class='no_visible'>" + client['lastname'] + "</td>";
                            output += "<td > <a href='https://wa.me/+52" + client['telephone'] + "?text=Panoramicas Xalapa'>" + client['telephone'] + "</a> </td>";
                            output += "<td class='no_visible'>" + client['email'] + "</td>";
                            output += "<td class='no_visible'>" + client['idSchool'] + "</td>";
                            output += "<td class='no_visible'>" + client['group'] + "</td>";
                            output += "<td>";
                            output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#formClients' onclick='edit_client("${client['idClient']}","${client['name']}","${client['lastname']}","${client['telephone']}","${client['email']}","${client['idSchool']}","${client['group']}")'>Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            $('#table').html(output);
                        });
                    }

                });
                
            }
        });
    }

    $('#form_client').submit(function(event){
        event.preventDefault();
        ajax_client();
        document.getElementById('form_client').reset();
        document.getElementById('close_modal').click();
        
    });

    function ajax_updateClient(){
        $.ajax({
            url:'/dashboard/register/client',
            type:'PATCH',
            data:$('form').serialize(),
            success: function(response){
                //console.log(response)
                $("#table").html('');
                var output;
                var alert;
                response.forEach(function each(item, index){
                    if (index==0){
                        alert = '';
                        alert += `<div class="alert ${item['type']} alert-dismissible fade show mt-3 fixed-bottom col-6 col-lg-6" role="alert" id="alerts">`;
                        alert += `${item['text']}`;
                        alert += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">';
                        alert += '<span aria-hidden="true">&times;</span>';
                        alert += '</button>';
                        alert += '</div>';
                        $('#alerts').html(alert);
                    }else{
                        item.forEach(client => {
                            console.log(client);
                            output += "<tr>";
                            output += "<td>" + client['name'] + "</td>";
                            output += "<td class='no_visible'>" + client['lastname'] + "</td>";
                            output += "<td > <a href='https://wa.me/+52" + client['telephone'] + "?text=Panoramicas Xalapa'>" + client['telephone'] + "</a> </td>";
                            output += "<td class='no_visible'>" + client['email'] + "</td>";
                            output += "<td class='no_visible'>" + client['idSchool'] + "</td>";
                            output += "<td class='no_visible'>" + client['group'] + "</td>";
                            output += "<td>";
                            output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#formUpdateClients' onclick='edit_client("${client['idClient']}","${client['name']}","${client['lastname']}","${client['telephone']}","${client['email']}","${client['idSchool']}","${client['group']}")'>Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            $('#table').html(output);
                        });
                    }

                });
                
            }
        });
    }

    $('#form_update_client').submit(function(event){
        event.preventDefault();
        ajax_updateClient();
        document.getElementById('form_update_client').reset();
        document.getElementById('close_modalEdit').click();
    });

     $("#search_client").keyup(function () {
            var name = document.getElementById('search_client').value;
            $.ajax({
                method: "GET",
                url: '/dashboard/register/client/'+ name,
                data: {name},
                success: function (responde) {
                    $("#table_client").html('');
                    var output;
                    responde.forEach(client => {
                        console.log(client)
                        output += "<tr>";
                        output += "<td>" + client['name'] + "</td>";
                        output += "<td class='no_visible'>" + client['lastname'] + "</td>";
                        output += "<td > <a href='https://wa.me/+52" + client['telephone'] + "?text=Panoramicas Xalapa'>" + client['telephone'] + "</a> </td>";
                        output += "<td class='no_visible'>" + client['email'] + "</td>";
                        output += "<td>";
                        output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#formClients' onclick='edit_client("${client['idClient']}","${client['name']}","${client['lastname']}","${client['telephone']}","${client['email']}","${client['idSchool']}","${client['group']}")'>Editar</button>`;
                        output += "</td>";
                        output += "</tr>";
                        
                    });
                    $('#table_client').html(output);
                }
            });
        });
  
   

});

function filter(){

    var school = document.getElementById('filter_school').value;
    var group =document.getElementById('filter_group').value;
    
    $.ajax({
        url:'/dashboard/register/client/'+ school+'/'+group,
        data: {school},group,
        type: 'GET',
        success: function(response){
            $('#table').html('');
            var output;
            response.forEach(client => {
                output += "<tr>";
                output += "<td>" + client['name'] + "</td>";
                output += "<td class='no_visible'>" + client['lastname'] + "</td>";
                output += "<td > <a href='https://wa.me/+52" + client['telephone'] + "?text=Panoramicas Xalapa'>" + client['telephone'] + "</a> </td>";
                output += "<td class='no_visible'>" + client['email'] + "</td>";
                output += "<td class='no_visible'>" + client['idSchool'] + "</td>";
                output += "<td class='no_visible'>" + client['group'] + "</td>";
                output += "<td>";
                output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#formClients' onclick='edit_client("${client['idClient']}","${client['name']}","${client['lastname']}","${client['telephone']}","${client['email']}","${client['idSchool']}","${client['group']}")'>Editar</button>`;
                output += "</td>";
                output += "</tr>";
                $('#table').html(output);
            });
        }
    });
}



     



