// Automatic Slider

// var slide = document.getElementsByClassName("slide")

// function AutoSlider(){

//     if(slide[1].style.opacity == "0"){
//         slide[1].style.opacity = "1"
//         slide[1].style.visibility = "visible"
//     }

//     else if(slide[2].style.opacity == "0"){
//         slide[2].style.opacity = "1"
//         slide[2].style.visibility = "visible"
//     }

//     else if(slide[3].style.opacity == "0"){

//         slide[3].style.opacity = "1"
//         slide[3].style.visibility = "visible"
//     }
    
//     else{

//         slide[0].style.opacity = "1"
//         slide[0].style.visibility = "visible"

//         slide[1].style.opacity = "0"
//         slide[1].style.visibility = "hidden"


//         slide[2].style.opacity = "0"
//         slide[2].style.visibility = "hidden"


//         slide[3].style.opacity = "0"
//         slide[3].style.visibility = "hidden"

//     }
// }
// setInterval(AutoSlider, 2000)






// dropdown menu

let results = document.querySelector(".results")
let menu = document.querySelector(".menu")

results.onclick = function(){
    if (menu.style.opacity == "1"){
        menu.style.opacity  = "0"
    }
    else {
        menu.style.opacity  = "1"
    }
        
}


// show result

// btn = document.querySelector("button")
// table = document.querySelector("table")


// btn.onclick = function(){
//     if (table.style
// }


