# Circular-DNA-Alignment

**Comparing 2 Sequences**

When comparing 2 circular DNA sequences, it is possible that the linearized version of the same or of similar sequences have been sliced at different points. For example, given these two plasmids:

![image](https://user-images.githubusercontent.com/121813781/236218650-966dcd5a-6f7c-4bbc-a7da-ef098a314e6b.png)

They may have been alternatively sliced so that each reads differently:

![image](https://user-images.githubusercontent.com/121813781/236219477-b6988acf-befc-4e65-9d36-a7d052384d2b.png)

This program regonizes similar s of the DNA and reassmbles them linearly so that each linear strand has the same start point and end point: 

![image](https://user-images.githubusercontent.com/121813781/236220893-12c8c10d-d7a8-4519-b221-f657bb46c0a7.png)

The program works by first defining a start index and reading frame of the first sequence and seeing where an identical patterns exists within the second sequence. If more than once match is found, the reading frame automatically gets 1 base pair longer to increase specificity of the target region:

![image](https://user-images.githubusercontent.com/121813781/236236471-28b50a00-a8bd-40af-9ea1-cd126f59c9cd.png)

Once the match location has been found in the 2nd sequence, the 2nd sequence is cut at the match point and rearranged to match the order of the first sequence. 

![image](https://user-images.githubusercontent.com/121813781/236236558-0da3044d-7c53-49c1-8444-07fa29024688.png)

The program also check for similarity of the 2 sequences, outputting how many base pairs between sequences are not identical.
#
**Comparing More Than 2 Sequences**

Theoretically, the methods of this program may be used to compare 3 sequences, but only 2 at a time. Once a 2nd sequence has been respliced to match the first, either of the 2 now similarly aligned sequences may be compared to a 3rd sequence using the functionality of this program. 
