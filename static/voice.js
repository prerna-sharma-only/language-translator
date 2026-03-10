const micBtn = document.getElementById("micBtn");
const textInput = document.getElementById("textInput");

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = "en-US";

micBtn.onclick = () => {
recognition.start();
};

recognition.onresult = function(event){

const speechText = event.results[0][0].transcript;

textInput.value = speechText;

};