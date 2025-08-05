---
statblock: true
layout: "Daggerheart Adversary"
name: "Greater Earth Elemental"
tier: 3
type: "Bruiser"
description: "A living landslide of boulders and dust, as large as a house."
difficulty: "17"
thresholds: "22/40"
atk: +7
attack: "Boulder Fist"
range: "Very"
damage: "3d10+1 phy"
hp: 10
stress: 4
motives_and_tactics:
  - "Avalanche"
  - "knock over"
  - "pummel"
feats:
  - name: "Slow - Passive"
    desc: "When you spotlight the Elemental and they don’t have a token on their stat block, they can’t act yet. Place a token on their stat block and describe what they’re preparing to do. When you spotlight the Elemental and they have a token on their stat block, clear the token and they can act."
  - name: "Crushing Blows - Passive"
    desc: "When the Elemental makes a successful attack, the target must mark an Armor Slot without receiving its benefits (they can still use armor to reduce the damage). If they can’t mark an Armor Slot, they must mark an additional HP."
  - name: "Immovable Object - Passive"
    desc: "An attack that would move the Elemental moves them two fewer ranges (for example, Far becomes Very Close). When the Elemental takes physical damage, reduce it by 7."
  - name: "Rockslide - Action"
    desc: "Mark a Stress to create a rockslide that buries all the land in front of Elemental within Close range with rockfall. All targets in this area must make an Agility Reaction Roll (19). Targets who fail take 2d12+5 physical damage and become Vulnerable until their next roll with Hope. Targets who succeed take half damage."
  - name: "Momentum - Reaction"
    desc: "When the Elemental makes a successful attack against a PC, you gain a Fear."
---

```statblock
monster: Greater Earth Elemental
```