# LangChain Fundamentals

### Prompt Templates
Prompt Templates allow you to dynamically insert variables into prompts.

Example:
```python
prompt = ChatPromptTemplate.from_template(
    "Write a summary about {topic}"
)
```
```python
template = "Write a short paragraph about {topic}"
prompt_template_name = PromptTemplate(input_variables=['topic'],template=template)
print(prompt_template_name.format(topic="photosynthesis"))
```
### Simple LLM Chain
A chain that formats a prompt and calls an LLM.

Example:
```python
prompt = PromptTemplate.from_template("Write a slogan for {topic}")
#chain = LLMChain(llm=llm,prompt=prompt)
chain = prompt | llm
response = chain.invoke("climate change awareness")
print(response.content)
```
### Sequential Chain
One chain's output is used as another chain's input.

Example:
```python
sequential_chain = SequentialChain(
    chains=[company_chain, slogan_chain],
    input_variables=["product"],
    output_variables=["company_name", "slogan"],
    verbose=True
)
```

### Conversational Memory
Allows a chatbot to remember previous messages.

#### Conversational Buffer Memory

```python
memory = ConversationBufferMemory(return_messages=True)
```
```python
conversation = ConversationChain(llm=llm,memory=memory,verbose=True)
print(conversation.predict(input="Hi, my name is Sana."))
print(conversation.predict(input="What is my name?"))
print(conversation.predict(input="What did I just ask you?"))
```

#### Conversation Summary Memory
Conversation summary condenses past interactions into concise summaries that the model can reference.
This helps maintain context over long conversations.


***Note:*** Many features have been recently deprecated 
