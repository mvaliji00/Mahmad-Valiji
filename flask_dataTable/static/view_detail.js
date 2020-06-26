d3.json("/get-data").then(
function tabulate(data) {

		var table = d3.select('#table_1').append('table')
		var thead = table.append('thead')
		var	tbody = table.append('tbody');
		//var columns = d3.keys(data)
		var columns = Object.keys(d3.values(data)[0])

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
		  .attr("id", (column) => {return column})

		// create a row for each object in the data
		var rows = tbody.selectAll('tr')
		  .data(d3.values(data))
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
		    //.attr("id", "piechart")


       // chart("Amount")//.node().classList.add("piechart");

//       d3.select("#months")
//          .selectAll("option")
//          .data(columns)
//          .enter()
//          .append("option")
//          .attr("value", function(columns) { return columns; })
//          .text(function(columns) { return columns; });
//	    }
})