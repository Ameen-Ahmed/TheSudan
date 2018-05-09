function enter(e){
    this.style.fill = "red";
    this.style.opacity = .5;
}

function leave(e){
    this.style.fill = "transparent";
}


var allPaths = document.querySelectorAll("path");

for (let i=0; i < allPaths.length; i++){
    allPaths[i].addEventListener("mouseover", enter, false);
    allPaths[i].addEventListener("mouseleave", leave, false);
}
