/**
 * Created by Peter_000 on 3/23/14.
 */

$(document).ready(function() {
    var listener = new window.keypress.Listener();

    function Logger(name){
        var logs = new Array();
        var logName = name;
        this.addKeypress = function add_keypress(keypress) {
            logs.push(keypress);
        }
        this.getLogs = function get_logs(){
            return logs;
        }
    }

    var theLog = new Logger('myTestLogger');

    logAnUp = function(){
        console.log("you pressed up");
        theLog.addKeypress('up')
    };

    logADown = function(){
        console.log("you pressed dow");
        theLog.addKeypress('down')
    };

    logARight = function(){
        console.log("you pressed right");
        theLog.addKeypress('right')
    };
    logALeft = function(){
        console.log("you pressed left");
        theLog.addKeypress('left')
    };

    printOutLog = function(){
        console.log(theLog.getLogs().toString())
    }

    // create simple example of how to store state

    listener.simple_combo("up", logAnUp);

    listener.simple_combo("down", logADown);

    listener.simple_combo("right", logARight);

    listener.simple_combo("left", logALeft);

    listener.simple_combo("i", printOutLog);

    // first step, call /new to get board

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
    //drawBoard(JSONBoard)
    function postToUrl(theUrl, boardStateJson, onSuccessFcn){
        // Abstracting the ajax call to POST to webservice as this
        // was somewhat fussy to get working.
        $.ajax({
        type: "POST",
        url: theUrl,
        data: JSON.stringify(boardStateJson, null, '\t'),
        contentType: 'application/json;charset=UTF-8',
        success: onSuccessFcn});
    }

    console.log(JSON.stringify(JSONBoard))
    postToUrl('/move/up', JSONBoard, function(result){drawBoard(result)})

    /*
    d3.json('/move/up',JSONBoard, function(jsonData) {
            drawBoardFcn(jsonData);
    });
    */

    function drawBoard(JSONBoard) {
        //console.log(JSONBoard)
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