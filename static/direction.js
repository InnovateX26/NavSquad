function showStep() {
    document.getElementById("direction").innerText = steps[current];
    speak(steps[current]);
}

function nextStep() {
    if(current < steps.length - 1){
        current++;
        showStep();
    } else {
        speak("Destination reached");
    }
}