function insert_hbarPlot (id) {
    var data = window.chartData[id]
    var sliceNumber = Object.values(data).findIndex(rank => rank === "")/2

    if (sliceNumber != -0.5 && sliceNumber <= 10) {
        var values = Object.values(data).slice(0,sliceNumber)
        var freq = Object.values(data).slice(sliceNumber,sliceNumber*2)
    }
    else  {
        var values = Object.values(data).slice(0,10)
        var freq = Object.values(data).slice(10,20)
    }

    // index of
    var dataset = freq
    //Width and height
    var w = 300;
    var h = 100;
    var barPadding = 1;

    id2 = '#table1_' + id
    //Create SVG element
    var svg = d3.selectAll(id2)
                .append("svg")
                .attr("width", w)
                .attr("height", h);

    svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("width", 20)
    .attr("height", 100)
    .attr("x", function(d, i) {
        return i * (w / dataset.length-barPadding);
    })
    .attr("y", function(d) {
        return h - d;  //Height minus data value
    })
    .attr("height", function(d) {
        return d*100;  //Just the data value
    })
    .attr("fill", '#87CEFA');
}

