Implement two policies for finding an available agent for a new ticket.

Imagine a classic support system with incoming tickets and agents working on them.

Ticket:

    * id - unique identifier of the ticket (example: "4")
    * restrictions - list of skills required to process this ticket (example: ["French"])

Agent:

    * name - name of agent (example: "John")
    * skills - list of competences of this agent (example: ["English", "French"])
    * load - current number of tickets assigned to this agent (example: 2)

As a manager of our support system, I want to make sure that we are using an optimal algorithm to assign tickets to agents.

### Requirements

1) Finish the `Agent` and `Ticket` classes, implementing the `properties` needed.

2) Implement the method `find(self, ticket: Ticket, agents: List[Agent])` with the two following policies:

    * `class LeastLoadedAgent` - finds agent that is least loaded (skill matching is not obligatory).
    * `class LeastFlexibleAgent` - finds the least flexible of the available agents (the one with the fewest skills).

        Who is the least flexible agent?
        Let's compare two agents:

            Agent 1:
                * knows English
                * knows French

            Agent 2:
                * knows English

        Most of the cases are in English but there are some in French.
        And if the incoming ticket is in English, you want to assign it to `Agent 2` so as
        to be sure that the next French ticket will be assigned to an agent and will not be
        stacked.

        Agents should be sorted first by the number of skills they have, then by their load.

### Example

```python
ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
least_flexible_policy.find(ticket, [agent1, agent2])
```

#### Restrictions

  * One agent can handle a maximum of three tickets.
  * If no agent can be found by following our procedures then throw a `NoAgentFoundException`.
