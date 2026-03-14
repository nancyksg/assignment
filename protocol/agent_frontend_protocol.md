# Agent-to-Frontend Protocol

The AI agent communicates with the frontend using structured JSON messages.

The protocol enables the frontend to execute map operations and retrieve data layers.

## Message Format

{
  "message": "optional explanation for the user",
  "commands": [Command]
}

Each command instructs the frontend to perform a specific action.

## Command Schema

{
  "type": "string",
  "params": {}
}
