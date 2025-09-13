# Semantic Kernel Architecture Exercise

## Learning Objectives

This exercise will help you understand Semantic Kernel's core architecture and primary components:
- **The Kernel**: Central orchestration hub for AI services and functions
- **Semantic Skills (Prompt Functions)**: AI-powered functions using natural language prompts

## Exercise Overview

You will implement a specialized data analysis agent using Semantic Kernel that demonstrates the framework's key architectural components. The agent should be able to handle data analysis questions while rejecting queries outside its domain of expertise.

## Requirements

### Prerequisites
- Python 3.8+
- Azure OpenAI account with GPT-4 deployment
- Basic understanding of async/await patterns in Python

### Dependencies
Install the required packages:
```bash
pip install semantic-kernel python-dotenv
```

### Environment Setup
Create a `.env` file in your project root with the following variables:
```
AZURE_OPENAI_KEY=your_azure_openai_api_key
URL=your_azure_openai_endpoint_url
```

## Task Description

Implement a Python script that creates a specialized ChatCompletionAgent with the following specifications:

### 1. Kernel Setup
- Initialize a Semantic Kernel instance
- Configure and register an Azure OpenAI chat completion service
- Use GPT-4.1-mini deployment with API version "2024-12-01-preview"

### 2. Agent Configuration
Create a ChatCompletionAgent that:
- Specializes in data analysis expertise
- Can explain complex statistical analysis concepts
- Refuses to answer questions outside the data analysis domain
- Uses specific execution settings (temperature: 1.0, max_tokens: 300)

### 3. Testing Scenarios
Your implementation should handle these test prompts:
1. "What is the average of 11,22,33" (should answer)
2. "Summarize the plot of Romeo and Juliet" (should refuse)
3. "List the first 5 prime numbers" (should refuse) 
4. "Translate 'Good morning' into Spanish" (should refuse)
5. "Give me a statistical summary for this data: 233,555,9866,2345,77" (should answer)

## Expected Behavior

- **Data Analysis Questions**: The agent should provide helpful, detailed responses about statistical concepts and data analysis
- **Non-Data Questions**: The agent should politely decline to answer questions outside its specialized domain
- **Output Format**: Each test prompt should be clearly labeled with its number and the agent's response should be prefixed with "Agent says:"

## Key Concepts to Demonstrate

### Kernel Architecture
- How the Kernel serves as the central coordination point
- Service registration and management
- Integration between different SK components

### Agent Specialization
- Using instructions to create domain-specific AI agents
- How prompt engineering controls agent behavior
- Configuration of execution parameters

### Async Operations
- Proper use of async/await for SK operations
- Streaming responses from agents
- Event loop management

## Success Criteria

Your solution should:
1. Successfully initialize a Semantic Kernel with Azure OpenAI service
2. Create a specialized data analysis agent that follows its instructions
3. Demonstrate appropriate responses to both in-domain and out-of-domain queries
4. Use proper async patterns for all SK operations
5. Show clear understanding of SK's component architecture

## Extension Challenges

Once you complete the basic implementation, try these extensions:
1. Add memory integration to maintain conversation context
2. Create custom native functions for specific statistical calculations
3. Implement semantic functions using prompt templates
4. Add logging to trace kernel operations

## Architecture Notes

This exercise demonstrates several key Semantic Kernel concepts:
- **Service-Oriented Architecture**: How AI services are abstracted and registered
- **Agent Pattern**: Specialized AI agents with specific instructions and capabilities
- **Execution Settings**: Fine-tuning AI behavior through configuration
- **Async Streaming**: Real-time response generation and processing

Understanding these patterns will prepare you for building more complex AI applications with Semantic Kernel.