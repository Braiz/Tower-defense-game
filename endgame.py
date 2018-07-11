global score
def endgame():
    print 'Game over!'
    print 'Your score was:'
    print score
    pygame.quit()
    options = raw_input('Enter your name or type cancel: ')
    if options == 'cancel':
        execfile('towerdefencegame.py')
        return
    else:
        scorefile = open('scores.txt','a')
        scorefile.write(options + "_")
        scorefile.write(str(score) +"\n")
        scorefile.close()
        execfile('towerdefencegame.py')
        return
endgame()
