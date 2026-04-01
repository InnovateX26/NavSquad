function startNavigation() {
    let s = document.getElementById("start").value;
    let e = document.getElementById("end").value;

    document.getElementById("routePage").classList.add("hidden");
    document.getElementById("navPage").classList.remove("hidden");

    steps = [
        "Start from " + s,
        "Go straight",
        "Follow campus road",
        "Reach " + e
    ];

    current = 0;
    showStep();
}