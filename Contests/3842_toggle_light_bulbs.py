def togglelightbulb(bulbs):
    bulb_state = set()

    for b in bulbs:
        if b in bulb_state:
            bulb_state.remove(b)
        else:
            bulb_state.add(b)

    return sorted(bulb_state)

print(togglelightbulb([23,32,12,23,91,90,12]))

