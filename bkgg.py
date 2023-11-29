import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
bkgg=platform.architecture()[0]
if bkgg=="32bit":__import__("bkgg32")
elif bkgg=="64bit":__import__("bkgg64")
