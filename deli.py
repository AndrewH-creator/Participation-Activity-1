# WHY: Store the sandwiches that customers ordered.
sandwich_orders = ["turkey", "ham", "tuna", "chicken"]

# WHY: Store sandwiches after they are completed.
finished_sandwiches = []

# WHY: Keep making sandwiches until there are no orders left.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    # WHY: Move the completed sandwich to the finished list.
    finished_sandwiches.append(current_sandwich)

# WHY: Display all completed sandwiches.
print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(sandwich)
