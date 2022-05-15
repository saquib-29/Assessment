'''
Question: The Team At Video Is Developing A Method To Divide Movies Into Groups Based On The Number Of Awards They Have Won. A Group Can Consist Of Any Number Of Movies, But The Difference In The Number Of Awards Won By Any Two Movies In The Group Must Not Exceed K. The Movies Can Be Grouped Together Irrespective Of Their Initial Order. Determine The Minimum Number Of
This problem has been solved!

See the answer
The team at Video is developing a method to divide movies into groups based on the number of awards they have won. A group can consist of any number of movies, but the difference in the number of awards won by any two movies in the group must not exceed k.
The movies can be grouped together irrespective of their initial order. Determine the minimum number of groups that can be formed such that each movie is in exactly one group.
Example
The numbers of awards per movie are awards = [1, 5, 4, 6, 8, 9, 21, and the maximum allowed difference is k = 3.

One way to divide the movies into the minimum number of groups is:

The first group can contain [2, 1], The maximum difference between awards of any two movies is 1 which does not exceed K.
The second group can contain [5, 4, 6], The maximum difference between awards of any two movies is 2 which does not exceed k.
The third group can contain [8,9]. The maximum difference between awards of any two movies is 1 which does not exceed k.
The movies can be divided into a minimum of 3 groups.

Function Description
Complete the function minimumGroups in the
editor below.
minimum Groups has the following parameters:
int awards[n]; the number of awards each movie has earned
int k: the maximum difference in awards counts
'''

def group(arr,k):
    count=1
    arr.sort()
    a=arr[0]
    for i in range(1,len(arr)):
        if (arr[i]-a)<=k:
            continue    
        else:
            count+=1
            a=arr[i]
    
    return (count)
arr=[1,5,4,6,8,9,13]
k=4
print(group(arr,k))


#Answer should be 3
#[[1,4,5],[6,8,9],13]