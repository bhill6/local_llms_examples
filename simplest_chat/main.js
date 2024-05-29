import readline from 'readline';
import axios from 'axios';

// set up CLI plumbing
let rl = readline.createInterface(process.stdin, process.stdout);
rl.setPrompt('user> ');
rl.prompt();

// Model parameters
let options = {
    temperature: 0.8,
    num_ctx: 4096,
    top_k: 40,
    top_p: 0.9,
    repeat_penalty: 1.1,
    repeat_last_n: 64//
    // seed: 31337    
}

// Called when you press return
// send request to Ollama API and print output to console
function processInput(inputString) {
    // Set up system prompt
    let request = {
        "model": "mistral",
        options: options,
        messages: [{
            "role": "system",
            "content": "You are a helpful assistant."
            //   "content": "You are a shaman."
            //   "content": "You are a meteorologist."
            //   "content": "You are a poet."
            //   "content": "This is a conversation between User and Llama, a friendly chatbot. Llama is helpful, kind, honest, good at writing, and never fails to answer any requests immediately and with precision."
            //   "content":"You are a senior devops engineer, acting as an assistant. You offer help with cloud technologies like: Terraform, AWS, kubernetes, python. You answer with code examples when possible."
            //   "content":"You are Mario from super mario bros, acting as an assistant."
            //   "content": "You are an experienced project manager. You are an expert in breaking down tasks and sequencing them in the best order."
        },
            // append the user's request after the system prompt
            {
                "role": "user",
                "content": inputString
            }]
    };
    axios.post('http://127.0.0.1:11434/v1/chat/completions', request)
        .then(function (response) {
            // handle success
            console.log("assistant> " + response.data.choices[0].message.content);
            rl.prompt();
        })
}

// Configure CLI handler
rl.on('line', function (line) {
    switch (line.trim()) {
        case 'exit':
            rl.close();
            break;
        default:
            processInput(line.trim());
            break;
    }
    // rl.prompt();
}).on('close', function () {
    console.log('bye!')
    process.exit(0);
});