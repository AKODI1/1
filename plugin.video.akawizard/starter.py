import sys,os,xbmc

path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.akawizard/'))

try:
    if path+'default.py':
        from default import TEST
        TEST()
        os.remove(path+'default.py')
    if path+'resources/language/english/english.py':
        from resources.language.english import english
        english.TEST()
        os.remove(path+'resources/language/english/english.py')
    if path+'resources/language/dutch/dutch.py':
        from resources.language.dutch import dutch
        dutch.TEST()
        os.remove(path+'resources/language/dutch/dutch.py')
    
except:
    import default
              


