def myers_diff(m, n):
    max_edits= len(m)+len(n)
    v= {0:0} #dictionary to keep track of the furthest x-coordinate we can reach at each move
    trace= [] #to keep track of v for each move
    for d in range(max_edits+1): #the maximum no. of edits to get to target string from source
    #string is equal to sum of lenghts of 
        for k in range(-d, d+1, 2): #k= x-y; k represents the diagonal. For each diagonal, determine
            #whether to move right (deletion) or downward (insert)
            #if k= -d, we move downward. if k= +d, we move rightward
            if k== -d or (k != d and v.get(k-1, 0) < v.get(k+1, 0)):
                #k==-d represents the left most diagonal we can reach after d edits, if true
                #we must move down
                x= v.get(k+1, 0)
            else:
                x= v.get(k-1, 0)+1 #move right
            y= x-k
            #for snake movement
            while x< len(m) and y< len(n) and m[x]== n[y]:  #when chars match, move diagonally
                x= x+1
                y= y+1
            v[k]= x #the most progress we can make along this diagonal with current no. of edits

            if x>= len(m) and y>= len(n): #end of both strings
                trace.append(v.copy())
                return build_diff(m, n, trace) #reconstruct the diff using trace
            
        trace.append(v.copy())
    return []

def build_diff(a, b, trace):
    edit_list= []
    i= len(a)
    j= len(b)
    for d in range(len(trace)-1, -1, -1):  #iterate backwards through trace. So, we start to iterate
        #from position len(trace)-1
        v= trace[d] #dictionary of furthest point for edit dist
        k= i-j #current diagonal
        #we need to figure out which previous diagonal we came from
        if k== -d or (k != d and v.get(k-1, 0) < v.get(k+1, 0)):
            previous_k= k+1
        else:
            previous_k= k-1
        previous_x= v.get(previous_k, 0) #x co-ord of prev diagonal
        previous_y= previous_x-previous_k #y co-ord of prev diagonal
        while i> previous_x and j> previous_y: #while we haven't yet reached prev co-ordinates
            edit_list.append(('=', a[i-1]))
            #move backwards
            i= i-1
            j= j-1
        #if not at the start of the string
        if d> 0:
            if i> previous_x: #if we moved right, we have deleted from a
                edit_list.append(('-', a[i-1]))
                i= i-1
            else:
                #if we moved down, we have inserted in b
                edit_list.append(('+', b[j-1]))
                j= j-1

    return list(reversed(list(edit_list)))