function insert_vbarPlot(id,valid,missing) {
    var global_width= 600
    plot_width = 600

    var datavars = [((valid/100)*global_width),((missing/100)*global_width)]
    var prev_width = [0, datavars[0]]
    var colors = ['#87CEFA', '#696969'];

    // chart for table 2
    if (id.includes('table2')){
        var svg = d3.select(id)
        .append('svg')
        .attr('width', 600)
        .attr('height', 10);
    }
    else {
        var svg = d3.select(id)
        .append('svg')
        .attr('height', 10);
    }

    svg.selectAll('rect')
    .data(datavars)
    .enter()
    .append('rect')
    .attr('width', function(d){
        return d;})
    .attr('x',function(d, i){
        return prev_width[i]; })
    .attr('fill', function(d, i){ return colors[i]; })
    .attr('y',0)
    .attr('height', 10);
}
