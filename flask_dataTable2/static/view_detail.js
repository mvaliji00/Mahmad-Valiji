d3.json("/get-data").then(
function tabulate(data) {
    var table = d3.select('#table_1').append('table')
    var thead = table.append('thead')
    var	tbody = table.append('tbody');
    //var columns = d3.keys(data)

    var table_data = data.slice(0,14)
    var quality_data = data.slice(14,16)
    var columns = Object.keys(d3.values(table_data)[0])

    // append the header row
    thead.append('tr')
      .selectAll('th')
      .data(columns).enter()
      .append('th')
      .text(function (column) { return column; });

    thead.append('tr')
      .selectAll('th')
      .data(columns).enter()
      .append('th')
      .attr("id", (column) => {return "table1_chart_" + column});

    thead.append('tr')
      .selectAll('th')
      .data(columns).enter()
      .append('th')
      .attr("id", (column) => {return "table1_" + column})

    for (i = 0; i < columns.length; i++) {
        chartd3(columns[i]);
        //quality_data[0][columns[i]]
        bar('#table1_chart_' + columns[i],quality_data[0][columns[i]],quality_data[1][columns[i]]);
    }

    // create a row for each object in the data
    var rows = tbody.selectAll('tr')
      .data(d3.values(table_data))
      .enter()
      .append('tr')

    // create a cell in each row for each column
    var cells = rows.selectAll('td')
      .data(function (row) {
        return columns.map(function (column) {
          return {column: column, value: row[column]};
        });
      })
      .enter()
      .append('td')
      .text(function (d) { return d.value; })
      .attr("width", "100px");


    // populate dropdown menu
    var selectGroup = d3.select("#myselect")
    for (i = 0; i < columns.length; i++) {
        selectGroup.append("option").text(columns[i])
    };

    // refresh  dropdown menu
    $("#myselect").selectpicker("refresh");

    //.append("option").text("data1")
    //.append("option").text("data2");
})

