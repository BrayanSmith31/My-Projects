class Solution:
    def sentinel_search(self, key, arr):
        #Save the last element to later on set it back
        last_position = len(arr)-1
        last_element = arr[last_position]
        # Set the las element of the array equal to the key
        arr[last_position] = key
        
        # Loop through the array to find the key
        i = 0
        while arr[i] != key:
            i+=1
        
        # Set the original last element back
        arr[last_position] = last_element

        #Check if the element was or not in the array

        if (i < last_position) or (arr[last_position] == key):
            return i
        else:
            return 'Element was not found'




arr = [1,2,3,4]
len(arr)