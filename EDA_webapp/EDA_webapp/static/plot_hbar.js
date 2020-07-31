function insert_hbarPlot (id) {
    var data = window.chartData[id]
    var sliceNumber = Object.values(data).findIndex(rank => rank === "")/2

    if (sliceNumber != -0.5 && sliceNumber <= 10) {
        var label = Object.values(data).slice(0,sliceNumber)
        var freq = Object.values(data).slice(sliceNumber,sliceNumber*2)
    }
    else  {
        var label = Object.values(data).slice(0,10)
        var freq = Object.values(data).slice(10,20)
    }

    dataset = []
    for (var i = 0; i < freq.length; i++) {
        dataset.push({"value" : freq[i], "label": label[i]})
    }

    //Width and height
    var w = 300;
    var h = 100;
    var barPadding = 1;

    id2 = '#table1_' + id;
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
        d1 = d.values
        return i * (w / dataset.length-barPadding);
    })
    .attr("y", function(d) {
        return h - d.value;  //Height minus data value
    })
    .attr("height", function(d) {
        return d.value*100;  //Just the data value
    })
    .attr("fill", '#87CEFA')
    .on("mouseover", function(d) {
        tooltip.html("Category: " + d.label)
        tooltip.style("opacity", 1)
    })
    .on("mousemove", function(d){
        tooltip.style("left", (d3.event.pageX) + "px")
        tooltip.style("top", (d3.event.pageY - 28) + "px");
    })
    .on("mouseleave", function(d) {
        tooltip.style("opacity", 0)
    })

    var tooltip = d3.selectAll(id2)
        .append('div')
        .style("opacity", 0)
        .attr("class", "tooltip")

}

