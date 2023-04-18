def FIFO(size, pages):
    # Create an array of zeros with length equal to size to simulate the memory array
    memory = [0] * size
    # Initialize index to 0 to keep track of the current index in the memory array
    index = 0

    # Iterate over the pages list using a for loop
    for i in range(len(pages)):
        # Initialize found to False to keep track of whether the page is already in memory
        found = False

        # Iterate over the memory array using another for loop
        for j in range(size):
            # Check if the current page is already in memory
            if memory[j] == pages[i]:
                # If it is, print a hit message and set found to True
                print("hit " + str(memory[j]))
                found = True
                # Break out of the inner loop since we don't need to check the rest of the memory array
                break

        # If the page is not found in memory
        if not found:
            # Print a miss message and add the page to memory at the current index
            print("miss " + str(pages[i]))
            memory[index] = pages[i]
            # Increment the index by 1 (with modulo size to wrap around to the beginning of the memory array if necessary)
            index = (index + 1) % size
    # Return None to indicate that the function has completed
    return None


def LRU(size, pages):
    memory = [-1] * size # create an array to represent the memory, initialized to -1
    index = 0 # initialize index to 0

    for x in range(len(pages)): # loop through each page in the pages array
        found = False # reset found flag for each page in pages array
        for y in range(size): # loop through each element in memory
            if pages[x] == memory[y]: # if page is already in memory
                found = True
                print(pages[x], "hit") # output hit message
                break

        if not found: # if page is not in memory
            print(pages[x], "miss") # output miss message
            leastPosition = 0 # initialize leastPosition to 0
            for i in range(size): # loop through each element in memory
                if memory[i] == -1: # if there is an empty slot in memory
                    index = i # update index to index of empty slot
                    break
                if pages[leastPosition] not in pages[x+1:]: # if a page does not appear in future pages
                    leastPosition = i # update leastPosition
            memory[index] = pages[x] # put current page into memory
            index = (index + 1) % size # update index

    # Return None to indicate that the function has completed
    return None

def OPT(size, pages):
    memory = pages[:size]  # initialize memory with first "size" number of pages
    found = False
    count = 0

    for i in range(size, len(pages)):  # start from the "size"th page, because the memory is already filled with the first "size" number of pages
        found = False
        for j in range(size):
            if pages[i] == memory[j]:  # if page is found in memory
                found = True
                print("HIT")
                break
        if not found:  # if page is not found in memory
            positions = [-1] * size
            for j in range(size):
                for k in range(i, len(pages)):
                    if memory[j] == pages[k]:  # if page is found in future
                        positions[j] = k  # store the position of the page in future in the corresponding position array
                        break
            maxP = 0
            for j in range(1, size):  # find the page that has the maximum future position
                if positions[j] > positions[maxP]:
                    maxP = j
            memory[maxP] = pages[i]  # replace the page with the maximum future position with the current page
            print("MISS")
            count = (count + 1) % size
    
    return None


def main():
    # a reference page numbers
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    size = 3
    # FIFO(size, pages)
    # LRU(size, pages)
    OPT(size,pages);

if __name__ == "__main__":
    main()
