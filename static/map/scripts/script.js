function enter(e){
    this.style.fill = "red";
    this.style.opacity = .5;
    let element = document.getElementById("info-" + this.getAttribute("id"));
    element.classList.remove("hidden");
}

function leave(e){
    this.style.fill = "transparent";
    let element = document.getElementById("info-" + this.getAttribute("id"));
    element.classList.add("hidden");
}

let allPaths = document.querySelectorAll("path");

for (let i=0; i < allPaths.length; i++){
    allPaths[i].addEventListener("mouseover", enter, false);
    allPaths[i].addEventListener("mouseleave", leave, false);
}