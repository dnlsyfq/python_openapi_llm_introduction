import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-6-luna",
    reasoning_effort="none",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Help me write a tweet for our new espresso roast."},
    ]
)

print(response)
/
ChatCompletion(
  id='chatcmpl-Eixlifwv51rKZBUJTiWiRqJSgBExU', 
  choices=[
    Choice(finish_reason='stop',
           index=0, 
           logprobs=None, 
           message=ChatCompletionMessage(content='One sip of our Ethiopian dark roast opens with bold, bittersweet cocoa and finishes with a bright, wine-like sparkle—proof that deep roast can still surprise you.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1794384890, model='gpt-6-luna', object='chat.completion', metadata=None, moderation=None, service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=36, prompt_tokens=32, total_tokens=68, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0, text_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=0, cached_tokens=0, image_tokens=None, text_tokens=None)))
/




output = response.choices[0].message.content

api_call_id = response.id

model_used = response.model

total_tokens = response.usage.total_tokens

ai_output = response.choices[0].message.content

