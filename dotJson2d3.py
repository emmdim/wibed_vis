#!/usr/bin/env python

import json
import http_server

lines = [line.rstrip('\n') for line in open('topology.json')]
lines = [json.loads(l) for l in lines]
#print lines
nodes = []
nodecount = 0
links = []
linkcount = 0
# First find all nodes to also set their ids
for l in lines:
    if "primary" in l:
        print "Node ",l
        nodes.append({"id":nodecount,"name":l["primary"],"group":nodecount})
        nodecount += 1
    elif "secondary" in l:
        print "Node: %s",l
        nodes.append({"id":nodecount,"name":l["secondary"],"group":(nodecount-1)})
        nodecount += 1
# Then find all links
for l in lines:
    if "router" in l:
        if "gateway" in l:
            pass
        else:
            print "Link ",l
            for n in nodes:
                if n["name"] == l["router"]:
                    nodeA = n["id"]
                elif n["name"] == l["neighbor"]:
                    nodeB = n["id"]
            links.append({"id":linkcount,"source":nodeA,"target":nodeB,"weight":l["label"]})
            linkcount += 1

jsTopo = "d3.json"
f = open(jsTopo,"w")
print>> f, "{\"graph\":[],\"nodes\":["
for item in nodes:
    if item == nodes[-1]:
        f.write("%s\n" % json.dumps(item))
    else:
        f.write("%s,\n" % json.dumps(item))
print>> f, "],"
print>> f, "\"links\":["
for item in links:
    if item == links[-1]:
        f.write("%s\n" % json.dumps(item))
    else:
        f.write("%s,\n" % json.dumps(item))
print>> f, "]}"
f.close()

http_server.load_url('test.html')
