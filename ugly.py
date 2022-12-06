import sys
import os

# ugly: contents: [str] -> [str]
def ugly(contents):
    def ruin(expr, parsed_exprs):
        for key, val in parsed_exprs.items():
            if key in expr:
               return ruin(expr.replace(key, val), parsed_exprs)
        return expr

    parsed_exprs = dict()

    # No comments
    no_comment_contents = [x for x in contents if not x.startswith('#')]

    # Parse out LHS RHS
    for line in no_comment_contents:
        if ' = ' in line:
            splits = line.split(' = ')
            if len(splits) == 2:
                lhs, rhs = splits[0].strip(), splits[1].strip()
                parsed_exprs[lhs] = f"({rhs})"

    # Kick out all exprs with = in them
    # For the ones remaining, recursively fill in the gaps
    uglies = []
    for line in no_comment_contents:
        trimmed_line = line.strip()
        if ' = ' not in trimmed_line and len(trimmed_line) > 0:
            uglies.append(ruin(trimmed_line, parsed_exprs) + '\n')

    return uglies

# args: old_file new_file
def main(argv):
    old_file = argv[1]
    new_file = argv[2]

    with open(old_file, 'r') as f:
        old_file_contents = f.readlines()

    new_file_contents = ugly(old_file_contents)

    with open(new_file, 'w') as f:
        f.writelines(new_file_contents)

if __name__ == "__main__":
    main(sys.argv)