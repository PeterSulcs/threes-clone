/**
 * Created by Peter_000 on 3/23/14.
 */
$(document).ready(function() {
    // first step, call http://127.0.0.1:5000/new to get board
    /*
    JSONBoard = {
        "nrows": 4,
        "tiles": [
            {"position": {"col": 2, "row": 0}, "value": 1},
            {"position": {"col": 3, "row": 2}, "value": 1},
            {"position": {"col": 0, "row": 1}, "value": 1},
            {"position": {"col": 0, "row": 2}, "value": 2},
            {"position": {"col": 2, "row": 2}, "value": 1},
            {"position": {"col": 1, "row": 0}, "value": 1},
            {"position": {"col": 0, "row": 3}, "value": 2}],
        "next_tile": {"value": 3},
        "ncols": 4
    }
    drawBoard(JSONBoard)
    */
    d3.json('/new',function(jsonData) {
            drawBoard(jsonData);
    });

    function drawBoard(JSONBoard) {
        console.log(JSONBoard)
        var ncols = JSONBoard['ncols']
        var nrows = JSONBoard['nrows']
        var tiles = JSONBoard['tiles'].slice()

        var xPosFn = function(d) { return d.position.col }
        var yPosFn = function(d) { return d.position.row }
        var sizeFn = function(d) { return d.value*3 }

        var x = d3.scale.linear()
        .range([10, 280])
        .domain(d3.extent(tiles, xPosFn))

        var y = d3.scale.linear()
        .range([10, 280])
        .domain(d3.extent(tiles, yPosFn))

        var svg = d3.select("#demo").append("svg:svg")
        .attr("width", 600)
        .attr("height", 600)

        svg.selectAll("circle").data(tiles).enter()
        .append("svg:circle")
        .attr("r", sizeFn)
        .attr("cx", function(d) { return x(xPosFn(d)) })
        .attr("cy", function(d) { return y(yPosFn(d)) })
    }
})