def bubble_sort(scores, order='ascending'):
    n = len(scores)
    swap_count = 0

    for i in range(n):
        swapped = False  
        for j in range(0, n - i - 1):
            if (order == 'ascending' and scores[j] > scores[j + 1]) or (order == 'descending' and scores[j] < scores[j + 1]):
                # Swap the elements
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
                swap_count += 1
                swapped = True
        if not swapped:
            # If no swaps happened in this pass, the list is already sorted
            print(f"The list is already sorted in {order} order. No more sorting needed.")
            break

    return scores, swap_count

# Main Program
scores = list(map(int, input("Enter student scores separated by spaces: ").split()))

# Ascending Order
sorted_scores_asc, swaps_asc = bubble_sort(scores.copy(), 'ascending')
print("\nSorted Scores in Ascending Order:", sorted_scores_asc)
print("Number of swaps made:", swaps_asc)

# Descending Order
sorted_scores_desc, swaps_desc = bubble_sort(scores.copy(), 'descending')
print("\nSorted Scores in Descending Order:", sorted_scores_desc)
print("Number of swaps made:", swaps_desc)
