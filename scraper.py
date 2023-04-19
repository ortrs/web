#!/usr/bin/env python3
# ondasolas
"""
This is an HTML scraper
"""
__author__ = "Orlando Torres"
__copyright__ = "Copyright 2023, ondasolas"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.0.0"
__status__ = "Release"

import argparse
import json
import re

if __name__ == "__main__":
    a_links = []
    title_links = []
    p_links = []
    img_links = []
    descr = []

    new_entry = {}

    parser = argparse.ArgumentParser(description='Process HTML file to JSON.')
    parser.add_argument('file', type=argparse.FileType('r'), help='filename to process')
    args = parser.parse_args()
    f = open('art_database_photo.json','r')
    data = json.load(f)
    #for i in data['artwork']['pieces']:
    #    print(i)
    for i in args.file.readlines():
        
        if(i.lstrip().startswith('<a')):
            i.lstrip().split()[1]
            try:
                a_links.append(i.lstrip().split('"')[1])
            except IndexError as e:
                print("Self-link, fixing")
                a_links.append("img/art_2018/0000-00-00_Black_1000x705.jpg")
        if(i.lstrip().startswith('<h2')):
            tag = 'h2'
            reg_str = "<" + tag + ">(.*?)</" + tag + ">"
            res = re.findall(reg_str, i.lstrip())
            title_links.append(res[0])
        if(i.lstrip().startswith('<p')):
            tag = 'p'
            reg_str = "<" + tag + ">(.*?)</" + tag + ">"
            res = re.findall(reg_str, i.lstrip())
            p_links.append(res[0])
        if(i.lstrip().startswith('<img')):
            img_links.append(i.lstrip().split('"')[1])
    print("finished!")
    print(a_links)
    for i,j in enumerate(a_links):
        print(i)
        print(a_links[i].split('/'))
        print(len(a_links))
        print(len(title_links))
        d = {"year":a_links[i].split('/')[2].split('-')[0], 
             "date":a_links[i].split('/')[2].split('_')[0], 
             "extension":a_links[i].split('.')[1],
             "title":title_links[i],
             "size":p_links[i],
             "px":a_links[i].split('.')[0].split('_')[-1],
             "thumb":img_links[i],
             "img":a_links[i]
            }
        print(d)
        data['artwork']['pieces'].append(d)
        
        print(a_links[i],title_links[i],p_links[i],img_links[i])
    print(data)
    f = open('art_database_photo.json','w')
    json.dump(data, f, indent = 4)