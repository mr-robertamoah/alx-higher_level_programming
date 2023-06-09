#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - determine whether or not a linked list
* is palindrome or not
* Return: int (0 or 1)
*/
int is_palindrome(listint_t **head)
{
/**
 * 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
	int *stack = NULL;
	int size = 0, mid = 0, i = 0;
	listint_t *node = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	node = *head;
	while (node != NULL)
	{
		size++;
		node = node->next;
	}

	stack = malloc(sizeof(int) * size);
	node = *head;
	while (node != NULL)
	{
		stack[i] = node->n;
		i++;
		node = node->next;
	}

	if (size % 2 != 0)
		mid = (size + 1) / 2;
	else
		mid = size / 2;

	i = 0;
	while (i != mid)
	{
		if (stack[i] != stack[size - 1 - i])
		{
			free(stack);
			return (0);
		}
		i++;
	}

	free(stack);
	return (1);
}
