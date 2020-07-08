window.onload = function (){
    var button = document.getElementById("applyButton")


    button.addEventListener('click',function ()
        {
            var selection = $('#myselect').val()
            $(window.hidden).show()
            var columns = window.columns
            window.hidden = []

            for (var i = 0; i < selection.length; i++) {
                var index =  columns.findIndex(rank => rank === selection[i])

                //remove from detail tab
                var table = document.getElementById('table_1');
                var row = table.querySelectorAll('tr')

                var rowLength = row.length;
                var cellLength = row[index].cells.length;

                for(var y=0; y<rowLength; y+=1){
                    var cell = row[y].cells[index];
                    $(cell).hide()
                    window.hidden.push(cell)
                }


                //remove from column tab
                table = 'table'+index
                $(table).hide()
                window.hidden.push($(table)[0])
            }

//            var index = [];
//            for (var i = 0; i < selection.length; i++) {
//                index.push(columns.findIndex(rank => rank === selection[i]));
//            }
        }
    );



    //// working code
    //var table = document.getElementById('table_1');
    //var row = table.querySelectorAll('tr')
    //
    //var rowLength = row.length;
    //var cellLength = row[0].cells.length;
    //
    //for(var y=0; y<rowLength; y+=1){
    //    var cell = row[y].cells[0];
    //    console.log(cell)cell.remove()//$(cell).hide()
    //}
}

