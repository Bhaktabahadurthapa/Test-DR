import random
import time

# Disaster scenarios
disaster_events = [
    "AWS Region Failure",
    "Azure Database Crash",
    "Terraform State Corruption",
    "GCP Network Outage",
    "Kubernetes Pod CrashLoopBackOff",
    "GitOps Repository Sync Failure",
]

# Terraform actions
terraform_actions = {
    "Rebuild Infrastructure": 20,
    "Restore Terraform State from Backup": 15,
    "Provision Multi-Region Resources": 18,
    "Skip Action (Risky)": -10,
}

# GitOps actions
gitops_actions = {
    "Trigger GitOps Sync": 15,
    "Rollback Deployment": 12,
    "Redeploy Application Manifests": 18,
    "Do Nothing (Risky)": -15,
}

# Initialize game state
score = 0
budget = 100
rounds = 5

print("Welcome to Cloud Resilience Challenge!")
print("Simulating Multi-Cloud Disaster Recovery with Terraform & GitOps")
print(f"Initial Budget: ${budget}")
print(f"Rounds to Play: {rounds}\n")

time.sleep(1)

for round_number in range(1, rounds + 1):
    print(f"\n--- Round {round_number} ---")
    disaster = random.choice(disaster_events)
    print(f"Disaster Event: {disaster}\n")
    
    # Player chooses Terraform action
    print("Terraform Actions:")
    for index, (action, points) in enumerate(terraform_actions.items(), start=1):
        print(f"{index}. {action} (Impact: {points} points)")
    terraform_choice = int(input("Choose Terraform Action (Enter number): "))
    terraform_action = list(terraform_actions.keys())[terraform_choice - 1]
    terraform_points = list(terraform_actions.values())[terraform_choice - 1]
    score += terraform_points
    budget -= 10  # Action cost simulation
    print(f"Terraform Action Selected: {terraform_action} | Points: {terraform_points}\n")

    # Player chooses GitOps action
    print("GitOps Actions:")
    for index, (action, points) in enumerate(gitops_actions.items(), start=1):
        print(f"{index}. {action} (Impact: {points} points)")
    gitops_choice = int(input("Choose GitOps Action (Enter number): "))
    gitops_action = list(gitops_actions.keys())[gitops_choice - 1]
    gitops_points = list(gitops_actions.values())[gitops_choice - 1]
    score += gitops_points
    budget -= 10  # Action cost simulation
    print(f"GitOps Action Selected: {gitops_action} | Points: {gitops_points}\n")

    # Random event outcome
    random_event = random.choice(["Success", "Partial Recovery", "Failure"])
    if random_event == "Success":
        score += 10
        print("Event Outcome: Successful Recovery! (+10 points)")
    elif random_event == "Partial Recovery":
        score += 5
        budget -= 5
        print("Event Outcome: Partial Recovery. (+5 points, -$5 budget)")
    else:
        score -= 10
        budget -= 10
        print("Event Outcome: Recovery Failed! (-10 points, -$10 budget)")

    print(f"Current Score: {score} | Remaining Budget: ${budget}\n")
    time.sleep(1)

# Final scoring
print("\n=== Game Over ===")
print(f"Final Score: {score}")
print(f"Final Budget Remaining: ${budget}")

# Outcome evaluation
if score >= 90:
    print("Performance: Cloud Hero! Excellent disaster recovery.")
elif score >= 75:
    print("Performance: Resilient Architect. Solid recovery strategy.")
elif score >= 60:
    print("Performance: Learning Engineer. Needs some improvements.")
else:
    print("Performance: Needs Improvement. Review your disaster recovery strategies!")

print("Thank you for playing Cloud Resilience Challenge!")
