import readline from 'readline';
import axios from 'axios';
import llamaTokenizer from 'llama-tokenizer-js';

var rl = readline.createInterface(process.stdin, process.stdout);
rl.setPrompt('ohai!> ');
rl.prompt();

var messages = [
    {
      "role": "system",
      "content": "You are a helpful assistant."      
    }
];

function processInput(inputString) {
    messages.push({
        "role":"user",
        "content":inputString
    });
    var request = {
        "model": "mistral",
        "messages": messages
    };
    // console.log(request)
    calculateTokens(messages)
    axios.post('http://127.0.0.1:11434/v1/chat/completions', request)
        .then(function (response) {
            // handle success
            console.log("assistant> "+response.data.choices[0].message.content);
            messages.push(response.data.choices[0].message);   

            if (messages.length > 5) {
                messages.shift();
            } 
            calculateTokens(messages)
            rl.prompt();        
        })
}

function calculateTokens(messages) {
    var buffer = "";
    messages.forEach(element => {
        buffer = buffer + element.content
    });
    console.log("Tokens Used: " + llamaTokenizer.encode(buffer).length);

}



rl.on('line', function(line) {
    // console.log(line);
    switch(line.trim()) {
        case 'exit':
            rl.close();
            break;            
        default:
            processInput(line.trim());
        break;
    }
    // rl.prompt();
}).on('close', function() {
    console.log('kbai!')
    process.exit(0);
});