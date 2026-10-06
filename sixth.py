# --- Pass 1 ---

def pass1(assembly_code, optab):
    symbol_table = {}
    intermediate_code = []
    location_counter = 0

    for line_num, line in enumerate(assembly_code):
        parts = line.strip().split()

        if not parts:
            continue

        label = None
        opcode = parts[0]
        operands = []

        if ':' in opcode:
            # Label definition
            label = opcode[:-1]
            symbol_table[label] = location_counter

            opcode = parts[1]
            operands = parts[2:]
        else:
            operands = parts[1:]

        intermediate_code.append({
            'LC': location_counter,
            'opcode': opcode,
            'operands': operands
        })

        # Increment Location Counter
        if opcode in optab:
            location_counter += optab[opcode]['length']

        elif opcode in ['START', 'END', 'ORG', 'EQU', 'DS', 'DC']:

            if opcode == 'START' or opcode == 'ORG':
                location_counter = int(operands[0])

            elif opcode == 'DS':
                location_counter += int(operands[0])

            elif opcode == 'DC':
                location_counter += 1

        else:
            print(f"Error: Unknown opcode '{opcode}' at line {line_num + 1}")
            location_counter += 1

    return symbol_table, intermediate_code


# --- Pass 2 ---

def pass2(intermediate_code, symbol_table, optab):
    machine_code = []

    for instruction in intermediate_code:
        lc = instruction['LC']
        opcode = instruction['opcode']
        operands = instruction['operands']

        if opcode in optab:
            machine_opcode = optab[opcode]['machine_code']
            resolved_operands = []

            for operand in operands:
                if operand in symbol_table:
                    resolved_operands.append(
                        str(symbol_table[operand])
                    )
                else:
                    resolved_operands.append(
                        operand
                    )

            # Simplified machine code generation
            machine_code.append(
                f"{lc:04X}{machine_opcode} "
                f"{' '.join(resolved_operands)}"
            )

        elif opcode in ['START', 'END', 'ORG', 'EQU', 'DS', 'DC']:
            # Directives are handled in Pass 1
            pass

        else:
            machine_code.append(
                f"{lc:04X} ERROR: Cannot assemble '{opcode}'"
            )

    return machine_code


# --- Example Usage ---

if __name__ == "__main__":

    # Sample Assembly Code
    assembly_code = [
        "START 100",
        "LABEL1: ADD R1, R2",
        "MOV R3, R4",
        "JUMP LABEL2",
        "LABEL2: SUB R5, R6",
        "END"
    ]

    # Sample Opcode Table (OPTAB)
    optab = {
        "ADD": {
            "machine_code": "1A",
            "length": 1
        },
        "MOV": {
            "machine_code": "2B",
            "length": 1
        },
        "JUMP": {
            "machine_code": "3C",
            "length": 1
        },
        "SUB": {
            "machine_code": "4D",
            "length": 1
        }
    }

    print("--- Pass 1 Output ---")

    symbol_table, intermediate_code = pass1(
        assembly_code,
        optab
    )

    print("Symbol Table:", symbol_table)

    print("Intermediate Code:")

    for inst in intermediate_code:
        print(inst)

    print("\n--- Pass 2 Output ---")

    machine_code = pass2(
        intermediate_code,
        symbol_table,
        optab
    )

    print("Machine Code:")

    for mc in machine_code:
        print(mc)