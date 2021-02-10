#Get regions where there are reads < k bp
import pysam
import sys 
import os
import sys 
  
#get command line input
#n = len(sys.argv)
output_dir = sys.argv[1] + "/"
bam_file1 = sys.argv[2]
bam_file2 = sys.argv[3]
if_hg38_str = sys.argv[4]

if if_hg38_str == "True":
    if_hg38 = True
else:
    if_hg38 = False
#if_hg38 = True

avg_read_depth = sys.argv[5]


chr_list = ["1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15",
            "16", "17", "18", "19", "20",
            "21", "22", "X", "Y"]

#Get regions on ref where its not covered by at least one of the assembly

#chr_list = ["1"]

samfile = pysam.AlignmentFile(bam_file1, "rb")
g = open(output_dir + "assem1_non_cov_regions.bed", "w")
for chr_name in chr_list:
    #test
    #print(chr_name)
    #stop when parsed no_of_reads
    #no_of_reads = 400000
    cur_end = 0
    
    #loop through iter, index will not be reset
    if if_hg38:
        ref_name = "chr" + chr_name
    else:
        ref_name = chr_name
    iter = samfile.fetch(ref_name)
    
    for rec in iter:
        if rec.reference_start > cur_end:
            g.write(str(ref_name) + "\t")
            g.write(str(cur_end) + "\t")
            g.write(str(rec.reference_start))
            g.write("\n")
            cur_end = rec.reference_end
        else:
            if rec.reference_end > cur_end:
                cur_end = rec.reference_end

g.close()

samfile = pysam.AlignmentFile(bam_file2, "rb")
g = open(output_dir + "assem2_non_cov_regions.bed", "w")
for chr_name in chr_list:
    #test
    #print(chr_name)
    #stop when parsed no_of_reads
    #no_of_reads = 400000
    cur_end = 0
    
    #loop through iter, index will not be reset
    if if_hg38:
        ref_name = "chr" + chr_name
    else:
        ref_name = chr_name
    iter = samfile.fetch(ref_name)
    
    for rec in iter:
        if rec.reference_start > cur_end:
            g.write(str(ref_name) + "\t")
            g.write(str(cur_end) + "\t")
            g.write(str(rec.reference_start))
            g.write("\n")
            cur_end = rec.reference_end
        else:
            if rec.reference_end > cur_end:
                cur_end = rec.reference_end

g.close()

##################################################################
##################################################################

#Get regions where read depth > 2 * avg_read_depth

#For now, we filter calls by read depth


