curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "mistral",
        "messages": [
            {
                "role": "system",
                "content": "You are a storyteller."
            },
            {
                "role": "user",
                "content": "Once upon a time..."
            }
        ]
    }'