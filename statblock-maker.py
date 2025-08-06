import re


def parse(path):

    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.lstrip('\ufeff')

    results = {}

    for line in content.splitlines():

        # get Title
        if line.startswith('# '):

            # Title
            pattern_name = r'^\#(?!\#)\s*(.+)$'
            results['name'] = re.search(pattern_name, line).group(1).title()

        # get Tier & Type
        elif line.startswith('***Tier'):

            # Tier
            pattern_tier = r'^\*\*\*Tier\s+(\d+)'
            results['tier'] = re.search(pattern_tier, line).group(1)

            # Type
            pattern_type = r'^\*\*\*Tier\s+\d+\s+(\w+)'
            results['type'] = re.search(pattern_type, line).group(1)

        # get Motives and Tactics
        elif line.startswith('**Motives & Tactics'):

            pattern_motives = r'\*\*Motives\s*&\s*Tactics:\*\*\s*(.+)'

            results['motives'] = []
            motives = re.search(pattern_motives, line).group(1)
            motives = motives.split(',')

            for motive in motives:
                results['motives'].append(motive.strip())

        # get Stats
        elif line.startswith('> **Difficulty'):

            pattern_difficulty = r'\*\*Difficulty:\*\*\s*(\d+)'
            results['difficulty'] = re.search(pattern_difficulty, line).group(1)

            pattern_thresholds = r'\*\*Thresholds:\*\*\s*([\d/\w]+)'
            results['thresholds'] = re.search(pattern_thresholds, line).group(1)

            pattern_hp = r'\*\*HP:\*\*\s*(\d+)'
            results['hp'] = re.search(pattern_hp, line).group(1)

            pattern_stress = r'\*\*Stress:\*\*\s*(\d+)'
            results['stress'] = re.search(pattern_stress, line).group(1)

        # get Attack
        elif line.startswith('> **ATK'):

            pattern_atk = r'\*\*ATK:\*\*\s*([+-]?\d+)'
            results['atk'] = re.search(pattern_atk, line).group(1)

            line = line.split('|')

            pattern_attack = r'\*\*(.*):\*\*'
            results['attack'] = re.search(pattern_attack, line[1]).group(1)

            pattern_range = r'\*\*.*:\*\*\s*(\w*\s*\w*)'
            results['range'] = re.search(pattern_range, line[1]).group(1).strip()

            results['damage'] = line[2].strip(' ')

        # get Experience
        elif line.startswith('> **Experience'):

            pattern_experience = r'\*\*Experience:\*\*\s*(.+)'
            experiences = re.search(pattern_experience, line).group(1)

            results['experience'] = []

            experiences = experiences.split(',')
            for experience in experiences:
                results['experience'].append(experience.strip())

        # get description
        elif line.startswith('*'):

            results['description'] = line.strip().removesuffix('*').removeprefix('*')


        elif line.startswith('## FEATURES'):
            break

    feature_names = []
    feature_descriptions = []

    for line in content[content.find('## FEATURES'):].splitlines():

        if line.startswith('# FEATURES'):
            continue
        elif line.startswith('***'):

            pattern_featurename = r'\*\*\*(.*):\*\*\*'
            feature_names.append(re.search(pattern_featurename, line).group(1))

            pattern_featuredesc = r'\*\*\*.*\*\*\*\s*(.*)'
            feature_descriptions.append(re.search(pattern_featuredesc, line).group(1))

    results['feature_names'] = feature_names
    results['feature_descriptions'] = feature_descriptions

    return results



def createNote(path, stats: dict):

    output =f"""---
statblock: true
layout: "Daggerheart Adversary"
name: "{stats['name']}"
tier: {stats['tier']}
type: "{stats['type']}"
description: "{stats['description']}"
difficulty: "{stats['difficulty']}"
thresholds: "{stats['thresholds']}"
atk: {stats['atk']}
attack: "{stats['attack']}"
range: "{stats['range']}"
damage: "{stats['damage']}"
hp: {stats['hp']}
stress: {stats['stress']}
"""

    if ('experience' in stats.keys()):
        output = output + f"experience:\n"
        for experience in stats['experience']:
            output = output + f"  - \"{experience}\"\n"

    output = output + "motives_and_tactics:\n"
    for motive in stats['motives']:
        output = output + f"  - \"{motive}\"\n"

    output = output + "feats:\n"
    for i in range (0, len(stats['feature_names'])):
        output = output + f"  - name: \"{stats['feature_names'][i]}\"\n"
        output = output + f"    desc: \"{stats['feature_descriptions'][i]}\"\n"

    output = output + "---\n"
    output = output + "\n"
    output = output + "```statblock\n"
    output = output + f"monster: {stats['name']}\n"
    output = output + "```"
        
    #print(output)
    with open (f"statblocks/{path}", 'w') as file:
        file.write(output)





import os

for adversary in os.listdir('adversaries'):
    print(f"parsing {adversary}")
    createNote(adversary, parse('adversaries/' + adversary))

with open (f"statblocks/statblocks.md", 'w') as file:
    output = "# Statblocks\n"
    for statblock in os.listdir('statblocks'):
        output = output + f"- [[{statblock.removesuffix('.md')}]]\n"
    
    file.write(output)