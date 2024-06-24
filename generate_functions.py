import random

def generate_example(instruction, valeur_par_defaut):
    example_instruction = random.choice(instruction)
    example_valeur = random.choice(valeur_par_defaut)

    example = f"Par exemple, vous pouvez dire, {example_instruction} {example_valeur}"
    return example
