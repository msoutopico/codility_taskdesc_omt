Create two policies for finding an available agent for a new ticket.

Imagine a classic support system with incoming tickets and agents working on them.

Ticket:

    * id - unique identifier of the ticket (example: 4).
    * restrictions - list of skills required to process this ticket (example: [French]).

Agent:

    * name - name of agent (example: John).
    * skills - list of skills of this agent (example: [English, French]).
    * load - current number of tickets assigned to this agent (example: 2).

As a manager of our support system, I want to make sure that we use an optimal algorithm to assign tickets to agents.

### Requirements

Finish the Agent and Ticket classes, using the properties needed.

Create the method find self ticket Ticket agents List Agent with the two following policies:

   * Least Loaded Agent - finds agent that is least loaded (skill matching is not required).
   * Least Flexible Agent - finds the least flexible of the available agents (the one with the fewest skills).

      Who is the least flexible agent?
      Let’s compare two agents:

            Agent 1:
                * knows English.
                * knows French.

            Agent 2:
                * knows English.

      Most of the cases are in English but there are some in French.
      If the incoming ticket is in English, you want to assign it to Agent 2.
      This way you are sure that the next French ticket will be assigned to an agent and will not be
      stacked.

      Agents should be sorted first by the number of skills they have, then by their load.

### Example

naw

#### Restrictions

* One agent can handle a maximum of three tickets.
* If no agent can be found by following our procedures, then throw a No Agent Found Exception.
