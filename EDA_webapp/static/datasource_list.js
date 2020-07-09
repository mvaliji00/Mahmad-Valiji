d3.json('/get-datasources').then(function(data){
    // assign data source file name to DOM variable
    window.source = data[0]

    //create a list of items in sidebar
    var ul = d3.select('#dataList').append('ul');

	ul.selectAll('a')
	.data(data)
	.enter()
	.append('a')
	.html(String)
    .on("click", function (d,i) {
        if (window.source !== d) {
            window.source = d

            var table1 = document.getElementById("table_1")//.removeChild();
            $('#table_1').empty()
            $('#table_2').empty()

            chartDataTable1()
            insertTable1()
            insertTable2()
        }

    })

    chartDataTable1()
    insertTable1()
    insertTable2()
})


