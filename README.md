
This script simulates a #multi-cloud #disaster recovery game using Terraform and GitOps principles. 
Players are tasked with responding to various disaster scenarios by selecting appropriate actions 
to mitigate the impact and recover cloud infrastructure. The game evaluates the player's 
decision-making skills in handling cloud resilience challenges.

```
Modules:
    - random: Used to randomly select disaster events and outcomes.
    - time: Used to introduce delays for better user experience.
```
Game_Features
    - Disaster Scenarios: Simulates real-world cloud failures such as region outages, database crashes, 
      and Kubernetes issues.
    - Terraform Actions: Provides options to rebuild infrastructure, restore state, and provision resources.
    - GitOps Actions: Offers actions like triggering syncs, rolling back deployments, and redeploying manifests.
    - Random Event Outcomes: Adds unpredictability to the game with success, partial recovery, or failure outcomes.
    - Scoring System: Tracks the player's performance based on selected actions and outcomes.
    - Budget Management: Simulates resource constraints by deducting costs for each action.
Gameplay:
    - The game consists of multiple rounds, each presenting a random disaster scenario.
    - Players choose one Terraform action and one GitOps action per round.
    - The game calculates the impact of the chosen actions and updates the score and budget.
    - At the end of the game, the player's performance is evaluated based on the final score.
Performance_Levels:
    - Cloud Hero: Excellent disaster recovery (Score >= 90).
    - Resilient Architect: Solid recovery strategy (Score >= 75).
    - Learning Engineer: Needs some improvements (Score >= 60).
    - Needs Improvement: Review disaster recovery strategies (Score < 60).

```
