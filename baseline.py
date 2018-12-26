# Load all the libraries
import numpy as np 
import pandas as pd 

def find_closest_point(p1,p2):
    """ Finds the euclidean distance between 2 points"""
    xa = p1[1,]
    ya = p1[2,]
    xb = p2[1,]
    yb = p2[2,]
    dist = np.sqrt((xa-xb)**2 + (ya-yb)**2)
    return dist

def nearest_point_in_array(ref_pt,arr):
    """ Finds the nearest point from the array relative to the reference point"""
    mindist = np.inf
    index = None
    for i in range(len(arr)):
        x = arr[i,0]
        if x != np.nan:
            dist = find_closest_point(ref_pt,arr[i,:])
            if dist < mindist:
                mindist = dist
                index = i
    return index,mindist

def baseline_model(start_pt,arrc,arrp,end_pt,verbose = False):
    """ Baseline model which utilizes nearest distance criteria"""
    l = len(arrc)
    l += len(arrp)
    start = start_pt
    route = [start_pt[0,]]
    path_dist = 0
    for i in range(l):
        # Run for all the arrays
        if len(arrc) != 0:
            indc,mindistc = nearest_point_in_array(start, arrc)
        if len(arrp) != 0:
            indp,mindistp = nearest_point_in_array(start, arrp)
        # Find which index is closer
        if (len(arrc) != 0) and (len(arrp) != 0):
            if i%10 == 0:
                route.append(arrp[indp,0])
                path_dist += mindistp
                start = arrp[indp,:]
                arrp = np.delete(arrp, indp, 0)
            elif (mindistc <= mindistp):
                route.append(arrc[indc,0])
                path_dist += mindistc
                start = arrc[indc,:]
                arrc = np.delete(arrc, indc, 0)
            elif (mindistc > mindistp):
                route.append(arrp[indp,0])
                path_dist += mindistp
                start = arrp[indp,:]
                arrp = np.delete(arrp, indp, 0)
        elif (len(arrc) == 0) and (len(arrp) != 0):
            route.append(arrp[indp,0])
            path_dist += mindistp
            start = arrp[indp,:]
            arrp = np.delete(arrp, indp, 0)
        elif (len(arrc) != 0) and (len(arrp) == 0):
            route.append(arrc[indc,0])
            path_dist += mindistc
            start = arrc[indc,:]
            arrc = np.delete(arrc, indc, 0)
        else:
            break
        if verbose:
            print('Step number is : ' + str(i) + '/'+str(l))

    # Returning back to north pole
    diste = find_closest_point(start,end_pt)
    route.append(end_pt[0,])
    path_dist += diste
    return route, path_dist
    