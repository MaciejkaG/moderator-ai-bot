# moderator-ai-bot
This is a simple AI-based bot made using the `detoxify` library.<br>
It checks all messages and deletes those that are flagged as potentially toxic or inappropriate, then sends a message containing the results and potential reasons of the deletion.

The model must return a result of at least 0.7 in order for the message to be flagged as inappropriate.