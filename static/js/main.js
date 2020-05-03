function calculate_cost() {
    var _6x9 = parseInt(document.getElementById('_6x9').value);
    var _8x12 = parseInt(document.getElementById('_8x12').value);
    var cost_6x9 = 100;
    var cost_8x12 = 200;
    var final_cost = 0;

        // calculate final_cost
        if(_6x9 > 0 || _8x12 > 0){
            if(_8x12 == 1 && _6x9 > 0){
                final_cost = ((_6x9*(cost_6x9 - 30)) + (_8x12 * (cost_8x12)))
            }else if(_8x12 >= 2 && _6x9 > 0){
                final_cost = ((_6x9*(cost_6x9 - 30)) + (_8x12 * (cost_8x12 - 50)))
            }else if(_8x12> 0 || _6x9 > 0){
                final_cost = (cost_6x9 * _6x9) + (cost_8x12 * _8x12);
            }
        }else{
            final_cost = 0;
        }

        //print values in form
        if(_6x9 > 0 || _8x12 > 0){
            document.add.num_8x12.value = _8x12;
            document.add.num_6x9.value = _6x9;
            document.add.cost.value = final_cost;
        }else{
            document.add.num_8x12.value = '';
            document.add.num_6x9.value = '';
            document.add.cost.value = '';
        }
    
    //replace value in cost
    document.getElementById('cost_ind').innerHTML = "El costo del paquete es: $ " + final_cost;
}