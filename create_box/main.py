


def create_box(height, width, character):
    box = '' 
    if height < 0:
        return ('Invalid Height')
    elif width < 0:
        return ('Invalid Width')
        
    for i in range(height):
        for j in range(width):
            box += character
        box += '\n'
    return box

def hollow_box(height, width, character):
    box = '' 
    if height < 0:
        return ('Invalid Height')
    elif width < 0:
        return ('Invalid Width')
    for i in range(height):
      for j in range(width):
        if i == 0 or i == height -1:
            box += character
        elif (i != 0 or i != height -1) and (j == 0 or j == width -1):
            box += character
        else:
            box += ' '
      box += '\n'
    return box


   
if __name__ == '__main__':
    print(create_box(3, 4, '@'))
    print(hollow_box(5, 5, '*'))

