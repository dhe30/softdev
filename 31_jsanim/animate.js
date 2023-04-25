//heading

var c = document.getElementById("playground");
//get dot button
var dotButton = document.getElementById("buttonCircle");
//stop button
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = '#7FFFD4';

//global var for use with animation frames
var requestID;

var clear = (e) => {
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
};

var radius = 0;
var growing = true;

var drawDot = () => {
    //clear
    clear();
    //repaint the circle
    ctx.beginPath();
    ctx.arc(c.clientWidth / 2, c.clientHeight / 2, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    if (growing){
        radius++;
    } else {
        radius--;
    }

    if (radius == (c.clientWidth / 2) || radius == 0){
        growing = !growing;
    }
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

//var stopIt = function
var stopIt = () => {
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener( "click", drawDot);
stopButton.addEventListener( "click", stopIt);