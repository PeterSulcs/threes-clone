/**
 * Created by Peter_000 on 3/23/14.
 */

$(document).ready(function() {
    var listener = new window.keypress.Listener();

    // key logger object:
    function Logger(name){
        var logs = new Array();
        var logName = name;
        this.addKeypress = function(keypress) {
            logs.push(keypress);
        }
        this.getLogs = function get_logs(){
            return logs;
        }
    }

    // Board State object:
    function BoardState(){
        var boardStateJson;
        this.setBoardState = function(boardState){
            boardStateJson = boardState;
            // Update D3 visualization:
            console.log("setting board state!");
            console.log(JSON.stringify(boardStateJson));
            drawBoard(boardStateJson);
        }
        this.getBoardState = function(){
            return boardStateJson;
        }
    }

    var theLog = new Logger('myTestLogger');
    var theBoard = new BoardState();

    // intial board:
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

    // get initial board
    initializeBoard(JSONBoard);
    theBoard.setBoardState(JSONBoard);

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

    moveUp = function(){
        console.log("you pressed up");
        theLog.addKeypress('up');
        postToUrl('/move/up', theBoard.getBoardState(), function(response){theBoard.setBoardState(response)});
    };

    moveDown = function(){
        console.log("you pressed down");
        theLog.addKeypress('down');
        postToUrl('/move/down', theBoard.getBoardState(), function(response){theBoard.setBoardState(response)});
    };

    moveRight = function(){
        console.log("you pressed right");
        theLog.addKeypress('right');
        postToUrl('/move/right', theBoard.getBoardState(), function(response){theBoard.setBoardState(response)});
    };

    moveLeft = function(){
        console.log("you pressed left");
        theLog.addKeypress('left');
        postToUrl('/move/left', theBoard.getBoardState(), function(response){theBoard.setBoardState(response)});
    };

    printOutLog = function(){
        console.log(theLog.getLogs().toString());
    };

    listener.simple_combo("up", moveUp);

    listener.simple_combo("down", moveDown);

    listener.simple_combo("right", moveRight);

    listener.simple_combo("left", moveLeft);

    listener.simple_combo("i", printOutLog);

    console.log(JSON.stringify(JSONBoard))
    //postToUrl('/move/up', JSONBoard, function(result){drawBoard(result)})

    /*
    d3.json('/move/up',JSONBoard, function(jsonData) {
            drawBoardFcn(jsonData);
    });
    */
    function initializeBoard(JSONBoard) {
        //console.log(JSONBoard)
        var svg = d3.select("#demo").append("svg:svg")
        .attr("width", 600)
        .attr("height", 600)
    }


    function drawBoard(JSONBoard) {
        var ncols = JSONBoard['ncols']
        var nrows = JSONBoard['nrows']
        var tiles = JSONBoard['tiles'].slice()

        var xPosFn = function(d) { return d.position.col }
        var yPosFn = function(d) { return d.position.row }
        var sizeFn = function(d) { return d.value*3 }

        var x = d3.scale.linear()
        .range([10, 280])
        .domain([0, ncols])

        var y = d3.scale.linear()
        .range([10, 280])
        .domain([0, nrows])

        var svg = d3.select("#demo > svg");
        svg.selectAll("rect").remove();

        var join = svg.selectAll("rect").data(tiles);

        //join.exit().remove();

        join.enter()
            .append("svg:rect")
            .attr("height", sizeFn)
            .attr("width", sizeFn)
            .attr("x", function(d) { return x(xPosFn(d)) })
            .attr("y", function(d) { return y(yPosFn(d)) })

        /*svg.selectAll("circle").data(tiles).transition()
        .attr("r", sizeFn)
        .attr("cx", function(d) { return x(xPosFn(d)) })
        .attr("cy", function(d) { return y(yPosFn(d)) })*/

        //svg.selectAll("circle").data(tiles).exit().remove();
    }

})