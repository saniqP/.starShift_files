
def star_shift(path):
    language = {
        '@*': 'a',       '#*': 'f',       '$*': 'k',        '%*': 'p',      '^*': 'u',      '&*': 'z',
        '@**': 'b',      '#**': 'g',      '$**': 'l',       '%**': 'q',     '^**': 'v',     '~': ' ',
        '@***': 'c',     '#***': 'h',     '$***': 'm',      '%***': 'r',    '^***': 'w',    '`': '\n',
        '@****': 'd',    '#****': 'i',    '$****': 'n',     '%****': 's',   '^****': 'x',
        '@*****': 'e',   '#*****': 'j',   '$*****': 'o',    '%*****': 't',  '^*****': 'y',
                }
    out_string = ''
    file = open(path, 'r')
    file_string = file.read().split('.')
    if file.name.split('.')[1] == 'starShift':
        for thisStr in file_string:
            if '!' in thisStr and '*' in thisStr:
                out_string += str(len(thisStr)-1)
                out_string += ' '
            elif thisStr == '!':
                out_string += '0'
                out_string += ' '
            else:
                for char in language:
                        if thisStr == char:
                            out_string += language.get(char)

    return out_string

def star_shift_write(text, path):
    output_string = ''
    file = open(path, 'a')
    language = {
        '@*': 'a', '#*': 'f', '$*': 'k', '%*': 'p', '^*': 'u', '&*': 'z',
        '@**': 'b', '#**': 'g', '$**': 'l', '%**': 'q', '^**': 'v', '~': ' ',
        '@***': 'c', '#***': 'h', '$***': 'm', '%***': 'r', '^***': 'w', '`': '\n',
        '@****': 'd', '#****': 'i', '$****': 'n', '%****': 's', '^****': 'x',
        '@*****': 'e', '#*****': 'j', '$*****': 'o', '%*****': 't', '^*****': 'y',
    }
    if file.name.split('.')[1] == 'starShift':
        for char in text:
            if char == ',':
                output_string += ".`"
            else:
                for key, value in language.items():
                    if char == value:
                        output_string += f".{key}"

    file.write(output_string)










