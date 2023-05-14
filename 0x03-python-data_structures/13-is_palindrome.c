#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_list(listint_t *node)
{
	listint_t *head;
	listint_t *tmp;

	head = NULL;
	tmp = node;
	while (tmp != NULL)
	{
		tmp = node->next;
		node->next = NULL;
		add_nodeint_end(&head, node->n);
	}
	return (head);
}

/**
* is_palindrome - 
*
*/
int is_palindrome(listint_t **head)
{
/**
 * 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
	listint_t *node;
	listint_t *second_node;
	listint_t *tmp;

	if (*head == NULL)
		return (1);

	node = *head;
	while (node != NULL)
	{
		second_node = reverse_list(node);
		tmp = second_node;
		while (tmp != NULL)
		{
			if (tmp->n != node->n)
			{
				free_listint(second_node);
				return (0);
			}
			tmp = tmp->next;
		}
		node = node->next;
	}
	free_listint(second_node);
	return (1);
}
