from subprocess import call

def PlayAudio(filename)
    filen = "/home/PokePiDex/" + filename
    call(["aplay", filen)