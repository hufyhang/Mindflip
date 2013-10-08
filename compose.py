#!/usr/bin/python
# Composer for Mindflip
# Copyright 2013, Feifei HANG
#

TEMPLATE_PLACE_TAG = '<!MINDFLIP_REPLACE_TAG!>'

INDEX_FILE = 'index.html'
INDEX_TEMPLATE = '_templates/index.html'
RESEARCH_SPOTLIGHT = '_resources/research.html'
WEB_CLIPS = '_resources/clips.html'

def readInIndexTemplate():
    indexTemplateFile = open(INDEX_TEMPLATE, 'r')
    indexTemplate = indexTemplateFile.read()
    indexTemplateFile.close()
    return indexTemplate

def readInResearchSpotlight():
    researchFile = open(RESEARCH_SPOTLIGHT, 'r')
    research = researchFile.read()
    researchFile.close()
    return research

def readInClips():
    clipsFile = open(WEB_CLIPS, 'r')
    clips = clipsFile.read()
    clipsFile.close()
    return clips

def merge(_indexTemplate, *_resources):
    buf = ''
    
    for index in range(0, len(_resources)):
        buf += _resources[index] + '\n'

    return _indexTemplate.replace(TEMPLATE_PLACE_TAG, buf)

def compose():
    html = merge(readInIndexTemplate(), readInResearchSpotlight(), readInClips())
    targetFile = open(INDEX_FILE, 'w+')
    targetFile.write(html)
    targetFile.close()
    print html

if __name__ == '__main__':
    compose()

