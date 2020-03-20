from subprocess import call

import msgfunc as prnt


def refresh_all(xresources, wallpaper_path, wallpaper):
    prnt.prnt('-n', 'Refreshing i3 and xrdb and setting wallpaper')
    if wallpaper != '':
        call(['nitrogen', '--set-zoom-fill', wallpaper_path+wallpaper])
    call(['xrdb', xresources])
    call(['i3-msg', 'restart'])
    prnt.prnt('-s', 'Done!')
