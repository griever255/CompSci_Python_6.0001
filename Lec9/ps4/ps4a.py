# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Base case if sequence is a single character, there's only 1 way to order it
    if len(sequence) == 1:
        return [sequence]                           # return a singleton list containing sequence
    # Recursive case
    else:
        output_list = []                            # Initialize the list of output permutations
        first_char = sequence[0]                    # Hold out the first character
        permlist = get_permutations(sequence[1:])   # List of all permutation of remaining letters
        for perm in permlist:                       # For each permutation string
            for i in range(len(sequence)):          # Step through the index,
                plist = list(perm)                  # first convert to a list, then
                plist.insert(i, first_char)         # insert the first letter at each index
                pstring = "".join(plist)            # then convert back to a string
                output_list.append(pstring)         # and add the string to the output list of permutations
        return sorted(output_list)
            

        
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = "abc"
    print("Input:", example_input)
    print("Expected Output:", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("Actual Output:  ", get_permutations(example_input))

    example_input = "cat"
    print("Input:", example_input)
    print("Expected Output:", ['act', 'atc', 'cat', 'cta', 'tac', 'tca'])
    print("Actual Output:  ", get_permutations(example_input))

    example_input = "dog"
    print("Input:", example_input)
    print("Expected Output:", ['dgo', 'dog', 'gdo', 'god', 'odg', 'ogd'])
    print("Actual Output:  ", get_permutations(example_input))

