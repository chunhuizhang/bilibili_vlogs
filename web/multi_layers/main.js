let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

var win_height = window.innerHeight;
var win_width = window.innerWidth;

canvas.height = win_height;
canvas.width = win_width;
console.log(canvas.width, canvas.height);

canvas.style.background = "#bbf";


class Circle {
    constructor(context, xpos, ypos, radius, color) {
        this.context = context;
        this.xpos = xpos;
        this.ypos = ypos;
        this.radius = radius;
        this.color = color;
    }
    draw() {
        this.context.beginPath();
        this.context.arc(this.xpos, this.ypos, this.radius, 0, Math.PI*2, this.color);
        this.context.strokeStyle = "grey";
        this.context.lineWidth = 15;
        this.context.fillStyle = this.color;
        this.context.fill();
        this.context.stroke();
        this.context.closePath();
    }
    clickCircle(xmouse, ymouse) {
        const distance = Math.sqrt((xmouse - this.xpos) * (xmouse - this.xpos) + (ymouse - this.ypos) * (ymouse - this.ypos));
        if (distance <= this.radius) {
            return true;
        }
        return false;
    }
    changeColor (newColor) {
        this.color = newColor;
        this.draw();
    }
}


let circle = new Circle(ctx, 200, 200, 100, "blue");
circle.draw(ctx);
canvas.addEventListener("click", (event) => {
//    console.log(event);
//    console.log("clicked canvas");
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    if (circle.clickCircle(x, y)) {
        circle.changeColor("red");
    } else {
        circle.changeColor("blue");
    }
//    console.log(rect);
});
