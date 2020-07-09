function insertTable1() {
    d3.json("/get-table1-data?source="+window.source).then(
    function tabulate(data) {
        var table = d3.select('#table_1').append('table')
        var thead = table.append('thead')
        var	tbody = table.append('tbody');
        //var columns = d3.keys(data)

        var table_data = data.slice(0,14)
        var quality_data = data.slice(14,16)
        var columns = Object.keys(d3.values(table_data)[0])
        window.columns = columns

        // append the header row
        thead.append('tr')
          .selectAll('th')
          .data(columns).enter()
          .append('th')
          .text(function (column,i) {
            return column;
          })
          .attr("class", (column,i) => {
            if (i === 0) { return "sticky-col"}
          });

        thead.append('tr')
          .selectAll('th')
          .data(columns).enter()
          .append('th')
          .attr("id", (column) => {return "table1_chart_" + column})
          .attr("class", (column,i) => {
            if (i === 0) { return "sticky-col"}
          });

        thead.append('tr')
          .selectAll('th')
          .data(columns).enter()
          .append('th')
          .attr("id", (column) => {return "table1_" + column})
          .attr("class", (column,i) => {
            if (i === 0) { return "sticky-col"}
          })
          .style("max-height", "none")
          .style("height", "100px");

        for (i = 0; i < columns.length; i++) {
            if (i!=0) {
                insert_hbarPlot(columns[i]);
                insert_vbarPlot('#table1_chart_' + columns[i],quality_data[0][columns[i]],quality_data[1][columns[i]]);
            }
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
          .attr("class", (d,i) => {
            if (i === 0) { return "sticky-col"}
          })

        // populate dropdown menu
        var selectGroup = d3.select("#myselect")
        for (i = 0; i < columns.length; i++) {
            selectGroup.append("option").text(columns[i])
        };

        $("#myselect").selectpicker("refresh");

    })
}


