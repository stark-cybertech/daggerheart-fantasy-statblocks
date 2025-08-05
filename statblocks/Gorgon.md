---
statblock: true
layout: "Daggerheart Adversary"
name: "Gorgon"
tier: 2
type: "Solo"
description: "A snake-headed, scaled humanoid with a gilded bow, enraged that their peace has been disturbed."
difficulty: "15"
thresholds: "13/25"
atk: +4
attack: "Sinew Shortbow"
range: "Far"
damage: "2d20+3 mag"
hp: 9
stress: 3
experience:
  - "Instinct +3"
motives_and_tactics:
  - "Corner"
  - "hit-and-run"
  - "petrify"
  - "seek vengeance"
feats:
  - name: "Relentless (2) - Passive"
    desc: "The Gorgon can be spotlighted up to two times per GM turn. Spend Fear as usual to spotlight them."
  - name: "Suneater Arrows - Passive"
    desc: "When the Gorgon makes a successful standard attack, the target Glows until the end of the scene and can’t become Hidden. Attack rolls made against a Glowing target have advantage."
  - name: "Crown of Serpents - Action"
    desc: "Make an attack roll against a target within Melee range using the Gorgon’s protective snakes. On a success, mark Stress to deal 2d10+4 physical damage and the target must mark a Stress."
  - name: "Petrifying Gaze - Reaction"
    desc: "When the Gorgon takes damage from an attack within Close range, you can spend a Fear to force the attacker to make an Instinct Reaction Roll. On a failure, they begin to turn to stone, marking a HP and starting a Petrification Countdown (4). This countdown ticks down when the Gorgon is attacked. When it triggers, the target must make a death move. If the Gorgon is defeated, all petrification countdowns end."
  - name: "Death Glare - Reaction"
    desc: "When the Gorgon makes a successful attack against a PC, you gain a Fear."
---

```statblock
monster: Gorgon
```