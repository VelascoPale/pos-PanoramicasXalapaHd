//function ajax for search clients in grd
$(document).ready(function () {

    function ajax_client(){
        $.ajax({
            url:'/dashboard/register/client/add',
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
                            output += `<button type='button' class='btn btn-info btn-sm' data-toggle='modal' data-target='#exampleModalScrollable' onclick='edit_client_grd("${client[0]}","${client[1]}","${client[2]}","${client[3]}","${client[4]}","${client[5]}","${client[6]}","${client[7]}","${event}")'>Editar</button>`;
                            output += "</td>";
                            output += "</tr>";
                            $('#table').html(output);
                        });
                    }

                });
                
            }
        });
    }

    $('#register-form').submit(function(event){
        event.preventDefault();
        ajax_client();
        document.getElementById('register-form').reset();
    });

});