'''
spam scam simulator based on day 24 'birthday invite challenge'
uses form letter and names files to generate pretend scam emails
'''

with open('./inputs/names.txt', 'r') as names:
    for name in names:
        name = name.strip()
        with open('./inputs/form_letter.txt', 'r') as f:
            form_letter = f.read().replace('[target]', name)
            with open(f'./outputs/{name}.txt', 'w') as out_file:
                out_file.write(form_letter)
                print(f'File for {name} has been written.')
