function speak(text){
    let speech = new SpeechSynthesisUtterance(text);
    let voices = speechSynthesis.getVoices();
    for(let i=0; i<voices.length; i++){
        if(voices[i].name.toLowerCase().includes("female") || voices[i].name.toLowerCase().includes("google")){
            speech.voice = voices[i];
            break;
        }
    }
    window.speechSynthesis.speak(speech);
}