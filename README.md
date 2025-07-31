### What is RAG(Retrieval Augmented Generation)
A LLM can answer only those questions which are based on training data. However, LLM can increase its knowledge by accessing external data via a technique called RAG.
`LLM is kind of one architecture that assist LLM with external knowledge`

### Can we call RAG as a Agent
No. Anthropic defines all AI based system in two categories.
 1. WorkFlow : These are the systems where LLM and tools are orchestrated through predefined paths. For example: Tool Augumented chatbot or consider
    HR system chatbot where in it can answer question related to how many leaves an employee is having.In this scenario, LLM might have access to Company data base and can refer
    employee specific data. Here chatbot is simple one and just answering the questions, not doing any planning or decision or actions.

 2. Agents on the other hand, are the system where LLM dynamically direct their own process and tool usage, maintain control to accomplish a task. Apart of having LLM(brain), agent has got the power
 of doing planning, making decision, take actions and has access to memory. So, agent can do specific complex task.


|          Type           | Reactive | Tool Usage | Reasoning | Planning | Proactivity |
|:-----------------------:|:--------:|:----------:|:---------:|:--------:|:-----------:|
|           RAG           |    ✅     |     ❌      |     ❌     |    ❌     |      ❌      |
 | Tool Augumented Chatbot |    ✅     |     ✅      |     ❌     |    ❌     |      ❌      |
|          Agent          |    ✅     |     ✅      |     ✅     |    ✅     |      ✅      |


### Langgraph
Generally, Agent's reliability goes down when agent's has given more control.

A simple agent with less access control is more reliable whereas autonomous agent which has more access control
becomes less reliasble. This is where langgraph comes into the picture. Langgraph framework has some ways to increase
the reliablity of autonomous agent.

`Langgraph is a frmework that helps to build reliable autonomous agent`

 There are other framework parallel to Langgraph:
 
1. Agno (Lighweight & fast)
2. Google ADK (Tight GCP integration & Multiagent)
3. Crew AI
4. Microsoft AutoGen (Tight Azure integration & Multiagent)

Where as Langgraph provides more flexible framework to build highly customizable complex agents.

### Langchain vs Langgraph

Langchain framework is ideal for building AI system that is liner in nature kind of multi steps linear work flow

Step1 ---> Step2------>Step3-------->Step4-------->LLM---->End

When to use Langgraph then ? When we need to build AI system that must have some sort of autonomy i.e ability to make decisions
kind of graph work flow.

| Feature    | Langchain   | LangGraph |
|:-----------|:------------|:----------|
|Purpose|Toolkit to build LLM apps(chain,tools, agents) | Framework to manage complex workflow with state|
|Style | Linear or reactive chains | Graph based, supports loops, reteries, memory|
| Best use case| Simple chatbots, RAG apps and tool usage | Mutli step workflow, agent with memory, conditions path|
|State Handling | Stateless or partially statefull | Fully Stateful; rememebers and transitions based on logic|

