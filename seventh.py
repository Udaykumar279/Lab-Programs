def macro_processor(input_file, output_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    MNT = {}  # Macro Name Table
    MDT = {}  # Macro Definition Table
    ALA = {}  # Argument List Array

    in_macro = False
    current_macro = ""
    temp_macro_lines = []

    # Pass 1: Store macro definitions
    for line in lines:

        tokens = line.strip().split()

        if not tokens:
            continue

        if 'MACRO' in tokens:
            in_macro = True
            current_macro = tokens[0]

            param_index = tokens.index('MACRO') + 1
            ALA[current_macro] = tokens[param_index:]

            temp_macro_lines = []
            continue

        if 'MEND' in tokens:
            in_macro = False

            MDT[current_macro] = temp_macro_lines[:]

            current_macro = ""
            temp_macro_lines = []
            continue

        if in_macro:
            temp_macro_lines.append(line.strip())

    # Pass 2: Expand macros
    with open(output_file, 'w') as out:

        for line in lines:

            tokens = line.strip().split()

            if not tokens:
                continue

            # Skip macro definitions
            if tokens[0] in MDT or 'MACRO' in tokens or 'MEND' in tokens:
                continue

            macro_name = tokens[0]

            if macro_name in MDT:

                args = [
                    arg.strip()
                    for arg in ' '.join(tokens[1:]).split(',')
                ]

                formal_params = ALA[macro_name]
                macro_body = MDT[macro_name]

                for macro_line in macro_body:

                    expanded_line = macro_line

                    for i in range(len(formal_params)):
                        expanded_line = expanded_line.replace(
                            formal_params[i],
                            args[i]
                        )

                    out.write('\t' + expanded_line + '\n')

            else:
                out.write(line)


# Run the macro processor
macro_processor('input.asm', 'output.asm')

# Display output
with open('output.asm', 'r') as result:
    print("\n--- Expanded Output (output.asm) ---\n")
    print(result.read())