window.onload = function (){
    var applyButton = document.getElementById("applyButton")

    applyButton.addEventListener('click',function ()
        {
            var selection = $('#myselect').val()
            $(window.hidden).show()
            var columns = window.columns
            window.hidden = []

            myArray = columns.filter( function( item ) {
              return !selection.includes(item );
            } );

            for (var i = 0; i < myArray.length; i++) {
                var index =  columns.findIndex(rank => rank === myArray[i])

                //remove from detail tab
                var table = document.getElementById('table_1');
                var row = table.querySelectorAll('tr')

                var rowLength = row.length;
                //var cellLength = row[index].cells.length;

                for(var y=0; y<rowLength; y+=1){
                    var cell = row[y].cells[index+1];
                    $(cell).hide()
                    window.hidden.push(cell)
                }

                //remove from column tab
                table = 'table'+index
                $(table).hide()
                window.hidden.push($(table)[0])
            }
        }
    );

    var clearButton = document.getElementById("clearButton")
    let dropdownAllUnselected = false;

    clearButton.addEventListener('click',function ()
        {
            if (!dropdownAllUnselected) {
                $("#myselect").selectpicker('deselectAll');
                clearButton.innerText = 'Select All';
            }
            else {
                $("#myselect").selectpicker('selectAll');
                clearButton.innerText = 'Clear';
            }
            dropdownAllUnselected = !dropdownAllUnselected;
        }
    )
}

