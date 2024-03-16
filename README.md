# apate_backend
Backend for Apate - an LLM based context aggregator to verify information and fight misinformation


## Story

On the internet, we encounter more information per hour than the average person even 5 years ago. <br>
Seeing is believing - But is everything we see true?

And so, a need arises to verify the information we consume. <br>
In most cases, a quick google search and skimming through the information can verify this information. <br><br>

## Objective
Apate aims to automate information verification.

What does Apate do for you?
- Takes your query
- Finds the context around it (Google, News articles, Social Media etc)
- Reason with the latest LLM technology
- Bring conclusive verification of your information with source citations
 
Ways to use the Apate backend (COMING SOON)
- For users
  - Browser extension, native chatbots
- For devs
  - API service

### Backend
Runs a pipeline that is available for use through an API service
- Takes in a query from a client service
- collects contextual information from multiple sources
- supplies curated context to LLMs
- takes LLM response and performs some quality control
- Provides the response to the client service

### API documentation
(Under development)

