
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var stack = new CanvasStack();
var layer1 = stack.createLayer();
var ctx1 = document.getElementById(layer1).getContext("2d");

ctx1.fillRect(0, 0, 100, 100);



