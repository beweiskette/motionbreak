def minimize(events, reproduces):
    """Deletion minimisation with a bounded maximum of eight input events."""
    current = list(events)
    index = 0
    while index < len(current):
        candidate = current[:index] + current[index + 1:]
        if reproduces(candidate):
            current = candidate
            index = 0
        else:
            index += 1
    return current
