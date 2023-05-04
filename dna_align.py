import re
import sys


def comp_seq(window_len, seq1, compare_index=0, wl_dec=False,first=False):
    """
    window_len    = the length of the scanning window
    seq1          = file path for the first sequence
    compare_index = index of seq 1 string where the window will start
    wl_dec        = determines if window_len decreases
    first         = determines if this is the first time the function is called

    This function intakes a genome and generates sequence of a specified (window) length at a specified start index,
    and determines if the sequence is within another genome
    """

    #save the first window length
    if first:
        global memory_wl
        memory_wl=window_len

    #if needing to decrease window_len
    #decrease by 1, then save new smallest window len
    if wl_dec:
        window_len = memory_wl-1
        memory_wl = window_len
    
        #generate match location
        #if scanning window gets to the end of the sequence, 
        #decrease the window length and try again
    try:
        return seq_align(seq1[compare_index:compare_index+window_len],\
                        "seq2.txt",\
                        window_len,\
                        compare_index)
    except:
        print("No matches found. Decreasing window size.")
        comp_seq(memory_wl, seq1, compare_index=0, wl_dec=True)
        
def seq_align(cs, seq2, wl,ci):
    """
    cs      = the comparison sequence from seq1 
    seq2    = file path for the second sequence
    wl      = window_length, potentially modified from multiple matches
    ci      = compare_index, potentially modified from no matches

    This function compares the comparison sequence to the second genome and returns
    the match position
    """
 
    #read the 2nd sequence and convert to string
    with open(seq2, "r") as f2:
        seq2 = "".join(f2.readlines()[1:])

    #determine matches
    matches = re.finditer(cs, seq2)

    matches_list=[]
    for match in matches:
        matches_list.append(match.start())

    #if more than one match, increase the window size for greater specificity and re run
    if len(matches_list)>1:
        return comp_seq(wl+1,seq1,ci)
    
    #else if no matches, change the reading frame
    elif len(matches_list)==0:
        return comp_seq(wl,seq1,ci+1)
    
    #else if exactly one match, return the start index of that match
    elif len(matches_list)==1:
        return matches_list[0]
        
    else:
        print("No matches found within genome")
        sys.exit(0)

def reassembly(seq2,mi,csi):
    """
    seq2    = a string of sequence 2
    csi     = the comparison start index of seq1
    mi      = the determined match index within seq2

    This function rearranges sequence 2 align with sequence 1
    """
    cut = seq2[:mi-csi]
    seq2=seq2[mi-csi:]
    seq2+=cut
    return seq2

def similarity_score(s1,s2):

    differences = 0
    
    for i in range(len(seq2_reassembled)):
        if seq2_reassembled[i]!=seq1[i]:
            differences+=1
    
    return print("There were", differences, "between the sequences, making them",\
                  (len(seq2)-differences)/len(seq2)*100, r"% similar")

if __name__ == "__main__":

    #read the 1st sequence and convert to string
    global seq1
    with open("seq1.txt", "r") as f1:
        seq1 = "".join(f1.readlines()[1:])
    f1.close()
    with open("seq2.txt", "r") as f2:
        seq2 = "".join(f2.readlines()[1:])
    f2.close()

    #define the index where the scanning window will begin in sequence 1
    comparison_start_index = 1500    

    #determine where comparison start of seq 1index aligns with sequence 2
    match_index = comp_seq(100,seq1,comparison_start_index,first=True)
    print("Match found at index", match_index)

    #reassemble sequence 2 to match sequence 1
    seq2_reassembled = reassembly(seq2,match_index,comparison_start_index)

    #print metrics
    similarity_score(seq1,seq2_reassembled)



    

