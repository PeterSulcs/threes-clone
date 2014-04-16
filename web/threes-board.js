/**
 * Created by Peter_000 on 4/16/2014.
 */

function Tile(value, row, col, id) {
    this.value = value;
    this.row = row;
    this.col = col;
    this.id = id;
}

Tile.prototype.toString = function() {
    return "[object Tile: (" + this.row + "," + this.col + ") value: " + this.value + " id: " + this.id + "]";
};

function Board(nrows, ncols) {
    var nrows = nrows;
    var ncols = ncols;
}

var a_tile = new Tile(4,1,1,0);
var b_tile = new Tile(8,2,3,2);

process.stdout.write(a_tile.toString());
process.stdout.write(b_tile.toString());
