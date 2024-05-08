import readline from 'readline';
import axios from 'axios';
import llamaTokenizer from 'llama-tokenizer-js';

// create the REPL shell
let rl = readline.createInterface(process.stdin, process.stdout);
rl.setPrompt('user> ');
rl.prompt();

// Message history list
// Each new request and response will be appended to it,
// and it's included in full at the beginning of each new request.
let messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
];

// called each time the user enters a line of text
function processInput(inputString) {
    //push the user's request onto the message history list
    messages.push({
        "role":"user",
        "content":inputString
    });

    let request = {
        "model": "mistral",
        "messages": messages
    };
    //calculateTokens will log how many tokens the entire history list is using
    calculateTokens(messages)
    //send the request to the LLM API
    axios.post('http://127.0.0.1:11434/v1/chat/completions', request)
        .then(function (response) {
            // handle success
            console.log("assistant> "+response.data.choices[0].message.content);

            //push the response onto the history list
            messages.push(response.data.choices[0].message);

            //calculateTokens will log how many tokens the entire history list is using
            calculateTokens(messages)
            rl.prompt();        
        })
}

function calculateTokens(messages) {
    let buffer = "";
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
    console.log('bye!')
    process.exit(0);
});