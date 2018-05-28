# -*- coding: latin-1 -*-
# kenning generator

# from several data files of OE-sounding words and phrases,
# generates 13 lines and picks one at random to tweet
# @beowbot

import random, string, tweepy
from kenningscredentials import *
import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def main():

    infile = open('ken-nouns.txt','r')
    ndata = infile.readlines()
    infile.close()

    infile = open('ken-verbs.txt','r')
    vdata = infile.readlines()
    infile.close()

    infile = open('ken-adj.txt','r')
    adata = infile.readlines()
    infile.close()

    infile = open('ken-nounx.txt','r')
    nxdata = infile.readlines()
    infile.close()

    infile = open('ken-verbs-pst.txt','r')
    vpdata = infile.readlines()
    infile.close()

    infile = open('ken-sent.txt','r')
    s1data = infile.readlines()
    infile.close()

    infile = open('ken-sent2.txt','r')
    s2data = infile.readlines()
    infile.close()

    nouns = [line[:-1] for line in ndata]
    verbs = [line[:-1] for line in vdata]
    adjs = [line[:-1] for line in adata]
    nounx = [line[:-1] for line in nxdata]
    verbpst = [line[:-1] for line in vpdata]
    sentpre = [line[:-1] for line in s1data]
    sentpost = [line[:-1] for line in s2data]

    lenn = len(nouns)
    lenv = len(verbs)
    lenvp = len(verbpst)
    lena = len(adjs)
    lennx = len(nounx)
    lenspre = len(sentpre)
    lenspost = len(sentpost)

    allkennings = []

    #And we wondered at the tear-raven, to all the men after the gem  coin
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              nouns[random.randrange(1, lenn)] +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)] + ',        ' + sentpre[random.randrange(1, lenspre)] +\
              nouns[random.randrange(1, lenn)] +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)]
    allkennings.append(ken)

    #The feud raged o'er the hand's Scyld. And within the hall, the being-misfortune
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              nouns[random.randrange(1, lenn)] +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)] + '.        ' + string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              nouns[random.randrange(1, lenn)] +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)]
    allkennings.append(ken)

    #Revenge's burn we heard , in the hall, where lay the back's Dane
    ken = string.capitalize(nouns[random.randrange(1, lenn)]) +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)] + ' ' + sentpost[random.randrange(1, lenspost)][:-1] +\
              ',        ' + sentpre[random.randrange(1, lenspre)] +\
              nouns[random.randrange(1, lenn)] +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)]
    allkennings.append(ken)

    #Ghost's spear we did not have , eater-mist the men had 
    ken = string.capitalize(nouns[random.randrange(1, lenn)]) +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)] + ' ' + sentpost[random.randrange(1, lenspost)][:-1] +\
              ',        ' + nouns[random.randrange(1, lenn)] +  nounx[random.randrange(1, lennx)] + \
              nouns[random.randrange(1, lenn)] + ' ' + sentpost[random.randrange(1, lenspost)]
    allkennings.append(ken)

    #The mountains sang of the kingless back, to all the men after the yellow fish
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              adjs[random.randrange(lena)] + ' ' + nouns[random.randrange(lenn)] + ',        ' +\
              sentpre[random.randrange(1, lenspre)] +\
              adjs[random.randrange(lena)] + ' ' + nouns[random.randrange(lenn)]
    allkennings.append(ken)

    #And answer the bright skull. So to the tall arrow
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              adjs[random.randrange(lena)] + ' ' + nouns[random.randrange(lenn)] + '.        ' +\
              string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              adjs[random.randrange(lena)] + ' ' + nouns[random.randrange(lenn)]
    allkennings.append(ken)

    #The road was littered with giant-fain bed, our children will sing of the life-red tears
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              nouns[random.randrange(lenn)] + '-' + adjs[random.randrange(lena)] + ' ' + \
              nouns[random.randrange(lenn)] + ',        ' + sentpre[random.randrange(1, lenspre)] +\
              nouns[random.randrange(lenn)] + '-' + adjs[random.randrange(lena)] + ' ' + \
              nouns[random.randrange(lenn)] + 's'
    allkennings.append(ken)

    #The stars shone upon the prowlers of swan, the earlmen attended the devoured promise
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              verbs[random.randrange(lenv)] + 'ers of ' \
              + nouns[random.randrange(lenn)] + ',        ' + \
              sentpre[random.randrange(1, lenspre)] +\
              verbpst[random.randrange(lenvp)] + ' '\
              + nouns[random.randrange(lenn)]
    allkennings.append(ken)

    #There came the  sonss watched, becalmed the mare amid the waves 
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) + ' '+ \
              nouns[random.randrange(lenn)] + 's ' + verbpst[random.randrange(lenvp)] + ',        ' + \
              verbpst[random.randrange(lenvp)] + ' the ' \
              + nouns[random.randrange(lenn)] + ' ' + sentpost[random.randrange(1, lenspost)]
    allkennings.append(ken)

    #We, kindly of spirit, the stole horses, moonlit jewel working we did not have 
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              verbpst[random.randrange(lenvp)] + ' ' + nouns[random.randrange(lenn)] + 's,        ' + \
              adjs[random.randrange(lena)] + ' ' + nouns[random.randrange(lenn)] \
              + ' ' + verbs[random.randrange(lenv)] + 'ing ' + \
              sentpost[random.randrange(1, lenspost)]
    allkennings.append(ken)

    #Flying with joy to the sold spirit. The road was littered with murderer of dream
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              verbpst[random.randrange(lenvp)] + ' ' \
              + nouns[random.randrange(lenn)] + '.        ' + \
              string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              verbs[random.randrange(lenv)] + 'er of ' \
              + nouns[random.randrange(lenn)]
    allkennings.append(ken)

    #This word-message we shout: the bending baits, to visit the begining banners
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) +\
              verbs[random.randrange(lenv)] + 'ing ' \
              + nouns[random.randrange(lenn)] + 's,        ' + \
              sentpre[random.randrange(1, lenspre)] +\
              verbs[random.randrange(lenv)] + 'ing ' \
              + nouns[random.randrange(lenn)] + 's'
    allkennings.append(ken)

    #The fiercest broke joints, and we said the king we did not have 
    ken = string.capitalize(sentpre[random.randrange(1, lenspre)]) + \
              verbpst[random.randrange(lenvp)] + ' ' \
              + nouns[random.randrange(lenn)] + 's,        and we ' + \
              verbpst[random.randrange(lenvp)] + ' the ' \
              + nouns[random.randrange(lenn)] + ' ' + sentpost[random.randrange(1, lenspost)]
    allkennings.append(ken)

    i = random.randrange(0, len(allkennings))
    line = allkennings[i] #choose random line from the ones just generated
    api.update_status(line)

main()
