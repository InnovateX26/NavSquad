
let steps = [];
let current = 0;

function login() {
    let u = document.getElementById("user").value;
    let p = document.getElementById("pass").value;

    if(u && p){
        document.getElementById("loginPage").classList.add("hidden");
        document.getElementById("routePage").classList.remove("hidden");
    } 
    else {
        alert("Enter details!");
    }
}
